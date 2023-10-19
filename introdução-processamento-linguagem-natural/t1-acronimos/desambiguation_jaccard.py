import csv

def calculate_jaccard_distance(x, y):
    set1 = set(x.split())
    set2 = set(y.split())
    intersection = len(set1.intersection(set2))
    union = len(set1) + len(set2) - intersection
    return intersection / union


def convert_to_acronym(sentence):
    words = sentence.split()
    acronym = ""
    for word in words:
        acronym += word[0].upper()
    return acronym.upper().replace("&", "").replace("/", "")


def clean_expansions(input_resolution, best_expansion):
    cleaned_input_expansion = input_resolution.replace("&", "and").replace("/", "")
    cleaned_best_expansion = best_expansion.replace("&", "and").replace("/", "")
    return cleaned_input_expansion, cleaned_best_expansion


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
            cosine = calculate_jaccard_distance(input[input_sentence_index], dataset_row[dataset_sentence_index])
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

# def disambiguate(data, input):
#     input_sentence = input[0]
#     input_acronym = input[1].replace("[", "").replace("]", "")
#     input_resolution = input[2].replace("[", "").replace("]", "")
#
#     dataset_sentence_index = 1
#     dataset_category_index = 2
#     input_sentence_index = 0
#
#     best_expansion = ""
#     best_average = 0
#     similarity = 0
#     count = 0
#     current_expansion = ""
#     for dataset_row in data:
#         running_expansion = dataset_row[dataset_category_index]
#         acronym = convert_to_acronym(running_expansion)
#         # Bug: it does not execute for last acronym because of this condition. The acronyms changes before
#         # calculating new average
#         if input_acronym == acronym:
#             if best_expansion == "":
#                 best_expansion = running_expansion
#                 current_expansion = running_expansion
#             # print(running_expansion + "   " + str(similarity))
#             if current_expansion != running_expansion:
#                 # print(running_expansion + "   " + str(similarity / count) + "   " + str(count) + "   " + str(
#                 #     similarity))
#                 current_average = similarity / count
#                 if best_average < current_average:
#                     best_average = current_average
#                     best_expansion = current_expansion
#                 similarity = 0
#                 count = 0
#                 current_expansion = running_expansion
#             similarity += calculate_cosine(input[input_sentence_index], dataset_row[dataset_sentence_index])
#             count += 1
#     if best_expansion != "":
#         print("Result: " + str(
#             input_resolution == best_expansion) + " - Sentence: " + input_sentence + " - Expected Category: " + input_resolution + " - Ouput Category: " + best_expansion)
