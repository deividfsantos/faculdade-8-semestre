from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForTokenClassification

tokenizer = AutoTokenizer.from_pretrained("vladjr/bert_ner_tf_pln")
model = AutoModelForTokenClassification.from_pretrained("vladjr/bert_ner_tf_pln", from_tf=True)

nlp = pipeline("ner", model=model, tokenizer=tokenizer, aggregation_strategy="simple")


example = """PROCEDURE

The case originated in an application (no. 36244/06) against the Kingdom of Denmark lodged with the Court under Article 34 of the Convention for the Protection of Human Rights and Fundamental Freedoms (“the Convention”) by a Danish national, Mr Henrik Hasslund (“the applicant”), on 31 August 2006."""

ner_results = nlp(example)

for result in ner_results:
    print(result)


print(ner_results)