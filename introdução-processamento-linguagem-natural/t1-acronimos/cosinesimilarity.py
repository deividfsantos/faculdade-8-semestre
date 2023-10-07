from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
import csv
import pandas as pd


def calculate_cosine(X, Y):
    # tokenization 
    X_list = word_tokenize(X)  
    Y_list = word_tokenize(Y) 

    # sw contains the list of stopwords 
    sw = stopwords.words('english')  
    l1 =[]
    l2 =[]
    
    # remove stop words from the string 
    X_set = {w for w in X_list if not w in sw}  
    Y_set = {w for w in Y_list if not w in sw} 

    # form a set containing keywords of both strings  
    rvector = X_set.union(Y_set)  

    for w in rvector: 
        if w in X_set: l1.append(1)
        else: l1.append(0) 
        if w in Y_set: l2.append(1) 
        else: l2.append(0)
    c = 0
    
    # cosine formula  
    for i in range(len(rvector)): 
            c+= l1[i]*l2[i] 
    cosine = c / float((sum(l1)*sum(l2))**0.5) 
    # print("similarity: ", cosine) 
    return cosine

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

dataset_phrase_index = 1
dataset_category_index = 2
adp_phrase_index = 0


# Compare the phrase from the ADP dataset with all the Phrases from our dataset to find the best category based on the average similarity.
for adp_row in data_from_adp[1:]:
    best_category = data[1][dataset_category_index]
    best_value = 0

    current_category = data[1][dataset_category_index]
    count = 0
    similarity = 0
    for data_set_row in data[1:]:
        if current_category != data_set_row[dataset_category_index]:
            med = (similarity/count)
            if best_value < med:
                best_category = data_set_row[dataset_category_index]
                best_value = med
            count = 0
            similarity = 0
            current_category = data_set_row[dataset_category_index]

        cosine = calculate_cosine(adp_row[adp_phrase_index], data_set_row[dataset_phrase_index])
        similarity += cosine
        count += 1

    print(best_category + ": " + adp_row[adp_phrase_index])
