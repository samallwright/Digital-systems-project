from nltk import sent_tokenize, word_tokenize
from text_functions import get_text, stop_word_removal


def similarity_graph(sentence_tokens) -> list:
    """Compare similarity between sentences to create ranking
    table between every sentence against every sentence"""

    matrix = []
    for sentence_i in sentence_tokens:
        scores = []
        for sentence_k in sentence_tokens:
            if sentence_i != sentence_k:
                score = words_in_common(sentence_i, sentence_k)
                scores.append(score)
        matrix.append(scores)
    return matrix


def words_in_common(sentence_one, sentence_two) -> int:
    """Finds amount of words in common"""

    counter = 0
    sentence_one = stop_word_removal(sentence_one)
    sentence_two = stop_word_removal(sentence_two)
    for word_one in sentence_one:
        for word_two in sentence_two:
            if word_one == word_two:
                counter += 1
    return counter


def graph_density(matrix, sentence_tokens) -> list:
    """creates density score of similar words against sentence length"""

    density_dicts = []
    for sentence_list in matrix:
        position = 0  # this is needed because index stops once it finds first occurence, doesnt actually track position in array
        sentence_densities = dict()
        for sentence in sentence_list:  # number representing similarity cardinality
            if sentence != 0:
                length = len(word_tokenize(sentence_tokens[position]))
                sentence_densities[position] = sentence / length
            else:
                sentence_densities[position] = 0
            position += 1
        density_dicts.append(sentence_densities)
    return density_dicts


def maximum_similarity(density_matrix: list) -> list:
    """gets highest similarity sentence for each sentence from graph"""

    most_similar_sentences = []
    for sentence in density_matrix:
        max_sentence = max(
            sentence.items(), key=lambda k: k[1]
        )  # creates tuples from dict values for sentence, returns max from result of lambda k which passes density(k[1]) as key
        most_similar_sentences.append(max_sentence)
    return most_similar_sentences


def weakest_links(sentence_scores):
    """filters highest similarity sentences above baseline"""
    similar_sentences = set()
    for sentence in sentence_scores:
        if sentence[1] >= 0.05:
            similar_sentences.add(sentence[0])
    return similar_sentences
