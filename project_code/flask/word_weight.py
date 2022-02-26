import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from open_test_text import get_text
from token_freq import basic_table

input_text = get_text()


def sentences(input_text: str):
    return sent_tokenize(input_text)


def weighting(sentence_tokens, frequency_table):
    weight = dict()
    for sentence in sentence_tokens:
        wordcount_without_stop = 0
        for word_weight in frequency_table:
            if word_weight in sentence.lower():
                wordcount_without_stop += 1
                if sentence in weight:
                    weight[sentence] += frequency_table[word_weight]
                else:
                    weight[sentence] = frequency_table[word_weight]

    return weight


print(weighting(sentences(input_text), basic_table(input_text)))
