import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from open_test_text import get_text
from stop_word import stop_word_vomit

input_text = stop_word_vomit(get_text())
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
