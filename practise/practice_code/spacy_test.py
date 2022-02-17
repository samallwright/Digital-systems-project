import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Apple is looking at buying U.K. startup for $1 billion")
doc = nlp("microsoft wants to sell american company for £20 million")

for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)
    
doc = nlp("Text summarization is a task in the field of natural language processing that con- sists of summarizing a text with a shorter and concise text.")

for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)