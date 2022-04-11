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
    t0 = time.perf_counter()
    for static_sentence in sentence_tokens:
        print(sentence_tokens.index(static_sentence))
        for moving_sentence in sentence_tokens:
            if static_sentence != moving_sentence:
                score = common_words(static_sentence, moving_sentence)
                matrix[sentence_tokens.index(static_sentence)].append(score)
    t1 = time.perf_counter() - t0
    print("time elapsed:", t1 / 60)


def common_words(sentence_one, sentence_two):
    counter = 0
    sentence_one = stop_word_removal(sentence_one)
    sentence_two = stop_word_removal(sentence_two)
    for one_word in sentence_one:
        for two_word in sentence_two:
            # print(one_word, two_word, "MATCH" if one_word == two_word else "")
            if one_word == two_word:
                counter += 1

    print(sentence_one, sentence_two, str(counter))
    return counter


matrix = [[], []]

# list of sentence x against y,z,...


def dot_product(A, B):
    return sum(a * b for a, b in zip(A, B))


def cosign_similarity(a, b):
    return dot_product(a, b) / ((dot_product(a, a) ** 0.5) * (dot_product(b, b) ** 0.5))


input = get_text()

similarity_graph(sent_tokenize(input))
