from cmath import log, log10
from multiprocessing.sharedctypes import Value
from pickle import FRAME
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk import FreqDist, ngrams
from text_functions import get_text
from stop_word import stop_word_removal


def word_freq_table(input_text: str) -> dict:
    word_tokens = word_tokenize(stop_word_removal(input_text))
    word_frequency = dict()
    for token in word_tokens:
        if token not in word_frequency.keys():
            word_frequency[token] = 1
        else:
            word_frequency[token] += 1
    word_sum = len(word_tokens)
    scored_words = {key: value / word_sum for (key, value) in word_frequency.items()}

    return scored_words


def inverse_document_frequency(sentences, word_tokens) -> dict:
    # idf = log(num_of_sentences/num_of_sentences_with_word)
    sentence_count_for_word = dict()
    for sentence in sentences:
        for word in word_tokens:
            if word.lower() in sentence.lower():
                if word in sentence_count_for_word:
                    sentence_count_for_word[word] += 1
                else:
                    sentence_count_for_word[word] = 1

    # sentence_count_for_word[word] = log10(
    #     len(sentences) / sentence_count_for_word[word]
    # )
    # print(sentence_count_for_word)
    # sentence_count_for_word = {
    #     key: log10(len(sentences) / sentence_count_for_word[value])
    #     for (key, value) in sentence_count_for_word.items()
    # }
    length = len(sentences)
    dictfun = dict()
    for word, frequency in sentence_count_for_word.items():
        dictfun[word] = log10(length / frequency)

    print(dictfun)


# inverse_document_frequency(sent_tokenize(get_text()), word_tokenize(get_text()))


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
# words in title
# how to select important infrequent
# any sentence with top 3 words in, + any sentence with 10 least common words in, ordered
# word pairs? (bigrams, trigrams, phrases)
