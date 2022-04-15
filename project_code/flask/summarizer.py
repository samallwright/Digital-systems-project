from token_frequencies import (
    word_freq_table,
    inverse_document_frequency,
    tf_idf_combine,
)
from word_weight import select_criteria_sentences, sentence_scoring
from nltk.tokenize import word_tokenize, sent_tokenize
from graph_model import (
    graph_density,
    maximum_similarity,
    similarity_graph,
    weakest_links,
)
from text_functions import get_text


def summarizer(title, content, prerequisite):
    sentence_tokens = sent_tokenize(content)
    word_tokens = word_tokenize(content)

    tf_idf = tf_idf_combine(
        word_freq_table(content),
        inverse_document_frequency(sentence_tokens, word_tokens),
    )

    # sentence scoring returns sentences and their scores from tfidf
    # call graphing next to give score for removal

    matrix = similarity_graph(sentence_tokens)
    density = graph_density(matrix, sentence_tokens)
    most_similar = maximum_similarity(density)
    similar_sentences = weakest_links(most_similar)

    weighted_sentences = sentence_scoring(sentence_tokens, tf_idf)
    filtered_sentences = word_removal(similar_sentences, weighted_sentences)

    summary = select_criteria_sentences(filtered_sentences, prerequisite)

    # summary = select_criteria_sentences(
    #     sentence_scoring(sentence_tokens, tf_idf),
    #     prerequisite,
    # )
    return summary


def word_removal(similar_sentences, weighted_sentences):
    list_words = list(weighted_sentences)
    filtered_weighted_sentences = {
        sentence: weight
        for (sentence, weight) in weighted_sentences.items()
        if list_words.index(sentence) not in similar_sentences
    }
    # print(len(weighted_sentences, len(filtered_weighted_sentences)))
    return filtered_weighted_sentences


# input = get_text()
# wokens = word_tokenize(input)
# stokens = sent_tokenize(input)
# matrix = similarity_graph(stokens)
# density = graph_density(matrix, stokens)
# tf_idf = tf_idf_combine(
#     word_freq_table(input), inverse_document_frequency(stokens, wokens)
# )
# weighted_sentences = sentence_scoring(stokens, tf_idf)
# most_similar = maximum_similarity(density)
# similar_sentences = weakest_links(most_similar)
# filtered_sentences = word_removal(similar_sentences, weighted_sentences)
# summary = select_criteria_sentences(filtered_sentences, 3)
# print(summary)
