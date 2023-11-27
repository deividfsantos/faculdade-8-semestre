import json
import spacy
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline

nlp_spacy = spacy.load("en_core_web_sm")
stop_words = spacy.lang.en.stop_words.STOP_WORDS 
caminho_arquivo = 'echr_train.json'

tokenizer = AutoTokenizer.from_pretrained("vladjr/bert_ner_tf_pln")
model = AutoModelForTokenClassification.from_pretrained("vladjr/bert_ner_tf_pln", from_tf=True)


def remove_stop_words(sentence): 
  doc = nlp_spacy(sentence) 
  filtered_tokens = [token for token in doc if not token.is_stop] 
  
  return ' '.join([token.text for token in filtered_tokens]).lower()



with open(caminho_arquivo, 'r') as file:
    data = json.load(file)

sum_precision = 0
total_count = 0

for i in range(len(data)-2):
    annotator1_mentions = data[i]

    commons_entities = []
    vladner_entities = []
    dataset_entities = []
    error_dataset_entities = []
    text = annotator1_mentions['text']

    nlp = pipeline("ner", model=model, tokenizer=tokenizer, aggregation_strategy="simple")


    # doc = [token for token in doc if not token.is_stop] 

    sentences = nlp_spacy(text)

    for sent in sentences.sents:
        ner_results = nlp(sent.text)

        # print(text)
        for result in ner_results:
            # print('result: ', result)
            clean_entity = remove_stop_words(result['word'])
            vladner_entities.append(clean_entity)
            # print('clean entity: ', clean_entity)

    annotations = annotator1_mentions['annotations']
    similar_count = 0


    for key, value in annotations.items():
        annotations = value


    for mention in annotations['entity_mentions']:
        span_text = remove_stop_words(mention['span_text'])
        # print('mention: ', span_text)
        if span_text in vladner_entities and span_text not in commons_entities:
            commons_entities.append(span_text)
            similar_count += 1
            # print("Common", span_text)
        if span_text not in dataset_entities:
            dataset_entities.append(span_text)
        if span_text not in vladner_entities and span_text not in error_dataset_entities:
            error_dataset_entities.append(span_text)
            # print("Error Entity: ", span_text)

    # print("Error dataset entities: ", len(error_dataset_entities))
    # print("Dataset entities: ", len(dataset_entities))
    # print("Vladner entities: ", len(vladner_entities))
    # print("Common entities: ", similar_count)

    precision = similar_count * 100 / len(dataset_entities)
    sum_precision += precision
    total_count += 1
    print("Precision: ", precision)

print("Complete average: ", sum_precision/total_count)

# Complete average:  70.30070063211593