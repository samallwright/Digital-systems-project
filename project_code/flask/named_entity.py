import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from text_functions import get_text
from text_functions import stop_word_removal

input_text = stop_word_removal(word_tokenize(get_text()))
word_tokens = word_tokenize(input_text)

tagged = nltk.pos_tag(word_tokens)

entities = nltk.chunk.ne_chunk(tagged)
sentence_string = sent_tokenize(input_text)


# print(tagged)
# print(entities)
# print(sentence_string)


# stitching sentences with top ten word
# also important infrquent words
# how to select important infrequent

# any sentence with top 3 words in, + any sentence with 10 least common words in, ordered

# word pairs? (bigrams and trigrams)
