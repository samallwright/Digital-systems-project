import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from open_test_text import get_text
from token_freq import basic_table

input_text = get_text()


def sentences(input_text: str) -> any:
    return sent_tokenize(input_text)


def weighting(sentence_tokens, frequency_table) -> dict:
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


def select_criteria_sentences(weighted_sentences: dict) -> list:
    sentences = [
        sentences
        for sentences in weighted_sentences
        if weighted_sentences[sentences] >= 1.5
    ]
    return sentences


# print(weighting(sentences(input_text), basic_table(input_text)))
# print(
#     select_criteria_sentences(
#         weighting(sentences(input_text), basic_table(input_text))
#     )
# )
