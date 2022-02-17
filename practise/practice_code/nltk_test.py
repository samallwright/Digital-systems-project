import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import treebank

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('treebank')

sentence = """At eight o'clock on Thursday morning
... Arthur didn't feel very good."""

sentence = """I wonder just how capable is nltk at natural language?"""

tokens = nltk.word_tokenize(sentence)

tagged = nltk.pos_tag(tokens)

entities = nltk.chunk.ne_chunk(tagged)

print(tokens)

print(tagged)

print(entities)


t = treebank.parsed_sents('wsj_0001.mrg')[0]
t.draw()



sentence_string = """ Muad'Dib learned rapidly because his first training was in how to learn.
... And the first lesson of all was the basic trust that he could learn.
... It's shocking to find how many people do not believe they can learn,
... and how many more believe learning to be difficult. """

sent_tokenize(sentence_string)