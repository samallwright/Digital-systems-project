from turtle import position
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from numpy import sort

from text_functions import get_text
from token_freq import basic_table

# input_text = get_text()


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


def select_criteria_sentences(weighted_sentences: dict, prerequisite: int) -> list:
    prerequisite = prerequisite_percentage(weighted_sentences, prerequisite)
    sentences = [
        sentences
        for sentences in weighted_sentences
        if weighted_sentences[sentences] >= prerequisite
    ]
    return sentences


def prerequisite_percentage(weighted_sentences: dict, prerequisite: int) -> int:
    # 0=none, 1= 25%cutm, 2=50%cut, 3=75%cut
    quartile = get_quartile(weighted_sentences)
    sorted_importance = sort(list(weighted_sentences.values()))
    prerequisite_position = sorted_importance[quartile * prerequisite]
    print(prerequisite, quartile, prerequisite_position)
    return prerequisite_position


def get_quartile(sents: dict) -> int:
    size = len(list(sents.values()))
    while size % 4 != 0:
        size -= 1
    return int(size / 4)


# print(weighting(sentences(input_text), basic_table(input_text)))
# print(
#     select_criteria_sentences(
#         weighting(sentences(input_text), basic_table(input_text))
#     )
# )
# print(
#     prerequisite_percentage(
#         weighting(sentences(input_text), basic_table(input_text)), 0
#     )
# )
