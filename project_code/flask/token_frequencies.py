from cmath import log, log10
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk import FreqDist, ngrams
from numpy import exp, pi, sqrt
import numpy
from text_functions import stop_word_removal
import matplotlib.pyplot as plt


def word_freq_table(input_text: str) -> dict:
    """Scored words returns a dict of every word against the amount of times that word was counted, divided by the total word count"""
    word_tokens = stop_word_removal(input_text)
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


def tf_idf_combine(term_frequencies, inverse_frequencies) -> dict:
    """A high weight in tf-idf is reached by a high term frequency (in the given document)
    and a low document frequency of the term in the whole collection of documents;
    the weights hence tend to filter out common terms.
    tf-idf(t,d,D) = tf(t,d)*idf(t,D)"""
    tf_idf = dict()
    for key in term_frequencies.keys() & inverse_frequencies.keys():
        tf_idf[key] = term_frequencies[key] * inverse_frequencies[key]
    return tf_idf


def position_score(sentences):
    """Creates a bell curve score for sentences to give value to positioning in document
    centers bell curve around 33% of document length to give most value near start with decreasing at end"""
    sentence_list = list(sentences)
    bell_center = round((len(sentence_list) / 3) * 2)
    sentence_length_list_positions = [x for x in range(bell_center)]

    mean = numpy.mean(sentence_length_list_positions)
    std = numpy.std(sentence_length_list_positions)
    bell_height = (
        1
        / (std * numpy.sqrt(2 * numpy.pi))
        * numpy.exp(-((sentence_length_list_positions - mean) ** 2) / (2 * std**2))
    ).tolist()

    bell_sentence_length_delta = len(sentence_list) - bell_center
    for x in range(bell_sentence_length_delta):
        bell_height.append(0)
    newdict = dict()
    for x in range(len(sentence_list)):
        newdict[x] = bell_height[x]

    return bell_height

    # print(bell_height)
    # print(y_out)
    # # Plotting the bell-shaped curve
    # plt.style.use("seaborn")
    # plt.figure(figsize=(6, 6))
    # plt.plot(sentence_length_list_positions, bell_height, color="black", linestyle="dashed")

    # plt.scatter(sentence_length_list_positions, bell_height, marker="o", s=25, color="red")
    # plt.show()


def combine_position_tf_idf(tf_idf, bell_height):

    return


def token_dists(input_text: str) -> FreqDist:
    word_tokens = stop_word_removal(input_text)
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
