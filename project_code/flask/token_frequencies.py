from cmath import log, log10
from multiprocessing.sharedctypes import Value
from pickle import FRAME
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk import FreqDist, ngrams
from text_functions import get_text, stop_word_removal


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
    """idf = log(num_of_sentences/num_of_sentences_with_word)"""
    sentence_count_for_word = dict()
    for sentence in sentences:
        for word in word_tokens:
            if word.lower() in sentence.lower():
                if word in sentence_count_for_word:
                    sentence_count_for_word[word] += 1
                else:
                    sentence_count_for_word[word] = 1
    length = len(sentences)
    inverse_freq = dict()
    for word, frequency in sentence_count_for_word.items():
        inverse_freq[word] = log10(length / frequency)
    return inverse_freq


def tf_idf_combine(term_frequencies, inverse_frequencies):
    """A high weight in tf–idf is reached by a high term frequency (in the given document)
    and a low document frequency of the term in the whole collection of documents;
    the weights hence tend to filter out common terms.
    tf-idf(t,d,D) = tf(t,d)*idf(t,D)"""

    tf_idf = dict()
    for key in term_frequencies.keys() & inverse_frequencies.keys():
        # print(term_frequencies[key])
        # print(inverse_frequencies[key])
        tf_idf[key] = term_frequencies[key] * inverse_frequencies[key]

    return tf_idf


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
# print(word_freq_table(input_text))
# print(token_dists(input_text).items())
# print(top_ten(token_dists(input_text)))
# print(bottom_10(token_dists(input_text)))
# print(single_occurrence(token_dists(input_text)))
# print(bigrams(token_dists(input_text)))
# print(trigrams(token_dists(input_text)).items())
# print(inverse_document_frequency(sent_tokenize(input_text), word_tokenize(input_text)))
# print(
#     tf_idf(
#         word_freq_table(input_text),
#         inverse_document_frequency(
#             sent_tokenize(input_text), word_tokenize(input_text)
#         ),
#     )
# )
