## Resultados das entidades do NER

Para cada texto do dataset echr_test.json, usamos as duas ferramentas abaixo para buscar todas as entidades e comparar se essas entidades estavam mapeadas no dataset. Isso nos diz o quão compatível são essas ferramentas com o dataset.

* vladjr/bert_ner_tf_pln: 68.15%
CODE  Average:  0.03
ORG  Average:  58.96
DEM  Average:  60.44
PERSON  Average:  61.22
DATETIME  Average:  95.27
LOC  Average:  74.89
QUANTITY  Average:  30.56
MISC  Average:  11.37

* Spacy: 74.97%
CODE  Average:  61.79%
ORG  Average:  73.87%
DEM  Average:  66.01%
PERSON  Average:  38.66%
DATETIME  Average:  96.58%
LOC  Average:  86.37%
QUANTITY  Average:  30.12%
MISC  Average:  21.45%