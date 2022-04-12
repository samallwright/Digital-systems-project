from tracemalloc import stop
from nltk import sent_tokenize, word_tokenize
from text_functions import get_text, stop_word_removal
import time


def similarity_graph(sentence_tokens):
    """Compare similarity between sentences to create ranking
    table between every sentence against every sentence
    """
    matrix = []
    for sentence_i in sentence_tokens:
        scores = []
        for sentence_k in sentence_tokens:
            if sentence_i != sentence_k:
                score = common_words(sentence_i, sentence_k)
                scores.append(score)
        matrix.append(scores)
    return matrix


def common_words(sentence_one, sentence_two):
    counter = 0
    sentence_one = stop_word_removal(sentence_one)
    sentence_two = stop_word_removal(sentence_two)
    for one_word in sentence_one:
        for two_word in sentence_two:
            if one_word == two_word:
                counter += 1
    return counter


def graph_density(matrix, sentence_tokens):
    """creates density score of similar words against sentence length"""
    matrict = []
    for sentence_list in matrix:  # list of numbers in list of lists
        counter = 0  # this is needed because index stops once it finds first occurence, doesnt actually track position in array
        # print(sentence_list)
        sentence_num = dict()
        for sentence in sentence_list:  # number representing similarity cardinality
            # print(sentence)
            if sentence != 0:
                # print(sentence_tokens[counter])
                length = len(word_tokenize(sentence_tokens[counter]))
                # print(sentence / length)  # this is word in common / words in comparison sentence = density
                sentence_num[counter] = sentence / length
            else:
                sentence_num[counter] = 0
            counter += 1
        matrict.append(sentence_num)
    return matrict


def similarity_score(density_matrix: list, weighted_sentences: dict):
    # compare most common sentence for current sentence
    # whichever has lower weighting has sentence from weighted senences removed is removed
    new_sentences = dict()
    counter = 0
    for sentence in density_matrix:
        if sentence != 0:
            if counter != 0:  # filter out no commonality
                print(sentence, prev_sentence)

                prev_sentence = sentence
            else:
                prev_sentence = sentence
        counter += 1
    return


def weakest_link(A_score, B_score):

    return


def dot_product(A, B):
    return sum(a * b for a, b in zip(A, B))


def cosign_similarity(a, b):
    return dot_product(a, b) / ((dot_product(a, a) ** 0.5) * (dot_product(b, b) ** 0.5))


# input = get_text()
# t0 = time.perf_counter()
# stokens = sent_tokenize(input)
# matrix = similarity_graph(stokens)
# t1 = time.perf_counter() - t0
# print("time elapsed: %fs" % (t1))
# density = graph_density(matrix, stokens)
# for sentence in density:
#     print(sentence.items())
