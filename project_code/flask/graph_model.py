from tracemalloc import stop
from nltk import sent_tokenize, word_tokenize
from text_functions import get_text, stop_word_removal
import time


def similarity_graph(sentence_tokens):
    """Compare similarity between sentences to create ranking,
    table between every sentence against every sentence

    """
    # for sentence in sentence_tokens:
    #     print(sentence_tokens.index(sentence))
    #     # print(f"{sentence}")
    #     if sentence_tokens.index(sentence) != 0:
    #         common_words(previous_sentence, sentence)
    #         previous_sentence = sentence
    #     else:
    #         previous_sentence = sentence
    # return

    # graphing
    matrix = []

    for static_sentence in sentence_tokens:
        scores = []
        for moving_sentence in sentence_tokens:
            # print(
            #     f"comparing {sentence_tokens.index(static_sentence)} against{sentence_tokens.index(moving_sentence)}"
            # )
            if static_sentence != moving_sentence:
                score = common_words(static_sentence, moving_sentence)
                # print(score)
                scores.append(score)
        matrix.append(scores)
    print(matrix)


def common_words(sentence_one, sentence_two):
    counter = 0
    sentence_one = stop_word_removal(sentence_one)
    sentence_two = stop_word_removal(sentence_two)
    for one_word in sentence_one:
        for two_word in sentence_two:
            if one_word == two_word:
                counter += 1
    return counter


def dot_product(A, B):
    return sum(a * b for a, b in zip(A, B))


def cosign_similarity(a, b):
    return dot_product(a, b) / ((dot_product(a, a) ** 0.5) * (dot_product(b, b) ** 0.5))


input = get_text()
t0 = time.perf_counter()
similarity_graph(sent_tokenize(input))
t1 = time.perf_counter() - t0
print("time elapsed: %fs" % (t1))
