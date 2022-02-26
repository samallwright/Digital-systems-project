from pickle import FRAME
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import FreqDist, ngrams
from open_test_text import get_text
from stop_word import stop_word_removal


def basic_table(input_text: str) -> dict:
    word_tokens = word_tokenize(stop_word_removal(input_text))
    word_frequency = dict()
    for token in word_tokens:
        if token not in word_frequency.keys():
            word_frequency[token] = 1
        else:
            word_frequency[token] += 1
    maxi = max(word_frequency.values())
    word_cool = {key: value / maxi for (key, value) in word_frequency.items()}
    # for word in word_frequency.keys():
    #     word_frequency[word] = word_frequency[word] / maxi
    return word_cool


def token_dists(input_text: str) -> FreqDist:
    word_tokens = word_tokenize(stop_word_removal(input_text))
    token_dist = FreqDist(word.lower() for word in word_tokens)
    return token_dist


def top_ten(tokens: FreqDist) -> list:
    return tokens.most_common(10)


def bottom_10(tokens: FreqDist) -> list:
    return tokens.most_common()[-10:]


def single_occurrence(tokens: FreqDist) -> list:
    list = tokens.most_common()[-1000:]
    new_list = []
    for tuple in list:
        if tuple[1] == 1:
            new_list.append(tuple)
    return new_list


def bigrams(tokens: FreqDist) -> dict:
    return dict(FreqDist(ngrams(tokens, 3)))


def trigrams(tokens: FreqDist) -> dict:
    return dict(FreqDist(ngrams(tokens, 3)))


# input_text = get_text()
# print(basic_table(input_text))
# print(token_dists(input_text))
# print(top_ten(token_dists(input_text)))
# print(bottom_10(token_dists(input_text)))
# print(single_occurrence(token_dists(input_text)))
# print(bigrams(token_dists(input_text)))
# print(trigrams(token_dists(input_text)).items())


# stitching sentences with top ten word
# also important infrquent words
# how to select important infrequent
# any sentence with top 3 words in, + any sentence with 10 least common words in, ordered
# word pairs? (bigrams and trigrams)
