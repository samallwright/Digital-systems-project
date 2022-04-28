from cue_words import cue_word_combine, find_cue_words, cue_score
from token_frequencies import (
    inverse_document_frequency,
    tf_idf_combine,
    position_score,
    combine_position_tf_idf,
    token_dists,
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


def summarizer(title, content, query, stigma, prerequisite):
    sentence_tokens = sent_tokenize(content)
    matrix = similarity_graph(sentence_tokens)
    density = graph_density(matrix, sentence_tokens)
    most_similar = maximum_similarity(density)
    similar_sentences = weakest_links(most_similar)

    word_tokens = word_tokenize(content)
    tf_idf = tf_idf_combine(
        token_dists(content),
        inverse_document_frequency(sentence_tokens, word_tokens),
    )

    weighted_sentences = sentence_scoring(sentence_tokens, tf_idf)
    bell_height = position_score(sentence_tokens)
    luhn_sentences = combine_position_tf_idf(weighted_sentences, bell_height)
    cue_frequencies = find_cue_words(title, query, stigma, sentence_tokens)
    cue_density = cue_score(cue_frequencies, sentence_tokens)
    edmunson_sentences = cue_word_combine(luhn_sentences, cue_density)

    filtered_sentences = word_removal(similar_sentences, edmunson_sentences)
    summary = select_criteria_sentences(filtered_sentences, prerequisite)
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
# # print(tf_idf)
# bell_height = position_score(stokens)
# # print(bell_height)

# weighted_sentences = sentence_scoring(stokens, tf_idf)

# luhn_sentences = combine_position_tf_idf(weighted_sentences, bell_height)
# # print(luhn)
# most_similar = maximum_similarity(density)
# similar_sentences = weakest_links(most_similar)
# filtered_sentences = word_removal(similar_sentences, luhn_sentences)
# summary = select_criteria_sentences(filtered_sentences, 3)
# print(summary)


# normal textrank is look at low similarity sentences, decide arbitrary amount of lowest to include
# my version is remove most similar

# options:
# comparison between sentences, tournament style selection judging with score
# remove all sentences with similarity
# remove sentences with similarity over threshold of similarity
# rank sentences based on number of other sentences found to be similar with
# ^^^^most similar get removed
