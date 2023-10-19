import csv

import spacy.cli

# spacy.cli.download("en_core_web_lg")
nlp = spacy.load("en_core_web_lg")


def calculate_similarity_spacy(x, y):
    input_sentence = nlp(x)
    dataset_sentence = nlp(y)

    input_sentence_no_stop_words = nlp(' '.join([str(t) for t in input_sentence if not t.is_stop]))
    dataset_sentence_no_stop_words = nlp(' '.join([str(t) for t in dataset_sentence if not t.is_stop]))
    return input_sentence_no_stop_words.similarity(dataset_sentence_no_stop_words)


def convert_to_acronym(sentence):
    words = sentence.split()
    acronym = ""
    for word in words:
        acronym += word[0].upper()
    return acronym.upper().replace("&", "").replace("/", "")


def clean_expansions(input_resolution, best_expansion):
    clean_input_expansion = input_resolution.replace("&", "and").replace("/", "")
    clean_best_expansion = best_expansion.replace("&", "and").replace("/", "")
    return clean_input_expansion, clean_best_expansion


def disambiguate(data, input):
    input_sentence = input[0]
    input_acronym = input[1].replace("[", "").replace("]", "").replace("&", "").replace("/", "")
    input_resolution = input[2].replace("[", "").replace("]", "")

    dataset_sentence_index = 1
    dataset_category_index = 2
    input_sentence_index = 0

    best_expansion = ""
    best_average = 0
    similarity = 0
    count = 0
    for dataset_row in data:
        running_expansion = dataset_row[dataset_category_index]
        acronym = convert_to_acronym(running_expansion)
        if input_acronym == acronym:
            if best_expansion == "":
                best_expansion = running_expansion
            cosine = calculate_similarity_spacy(input[input_sentence_index], dataset_row[dataset_sentence_index])
            similarity += cosine
            count += 1
            # print(running_expansion + " " + str(count) + "   " + str(similarity) + "  " + str(cosine))
            if count == 200:
                current_average = similarity / count
                if best_average < current_average:
                    best_average = current_average
                    best_expansion = running_expansion
                similarity = 0
                count = 0
    if best_expansion != "":  # If best_expansion = "" means there is no acronym in our dataset
        clean_input_expansion, clean_best_expansion = clean_expansions(input_resolution, best_expansion)
        print("Result: " + str(
            clean_input_expansion == clean_best_expansion) + " - Sentence: " + input_sentence + " - Expected Category: " + input_resolution + " - Ouput Category: " + best_expansion)
    return input_resolution, best_expansion


data = []
with open("dataset4.csv", 'r') as file:
    csvreader = csv.reader(file, delimiter="\t")
    for line in csvreader:
        data.append(line)

data_from_adp = []
with open("acronyms_data.csv", 'r') as file:
    csvreader = csv.reader(file, delimiter=";")
    for line in csvreader:
        data_from_adp.append(line)

# input = ["We used PR to launch our new product to great success.", "PR", "Public Relations"]

# input = ["ER compliance is an important factor to consider before investing in any finance related product.", "[ER]",
#          "[Earnings Report]"]
# input = ["ER managers should strive to maintain an accurate, detailed history of employee relations.", "[ER]",
#          "[Employee Relations]"]
# input = ["Our ATS platform is designed to store employee records securely.", "[ATS]", "[Applicant Tracking System]"]
# input = ["The SME Fund provides access to funds that SMEs enterprises would otherwise not have access to.", "[SME]",
#          "[Small and Medium-sized Enterprises]"]
# input = ["Financing for M&A deals is becoming increasingly important in order to reach targeted goals.", "[M&A]",
#          "[Mergers and Acquisitions]"]
# success = disambiguate(data[1:], input)

success_count = 0
fail_count = 0
for input in data_from_adp[1:]:
    input_resolution, best_expansion = disambiguate(data[1:], input)
    if best_expansion != "":
        clean_input_expansion, clean_best_expansion = clean_expansions(input_resolution, best_expansion)
        if clean_input_expansion == clean_best_expansion:
            success_count += 1
        else:
            fail_count += 1

total = success_count + fail_count

success_percent = (success_count / total) * 100
fail_percent = (fail_count / total) * 100

print(f"Success finding results: {success_count} {success_percent:.2f}%")
print(f"Failures finding results: {fail_count} {fail_percent:.2f}%")
