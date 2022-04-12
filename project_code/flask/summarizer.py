from token_frequencies import (
    word_freq_table,
    inverse_document_frequency,
    tf_idf_combine,
)
from word_weight import select_criteria_sentences, sentence_scoring
from nltk.tokenize import word_tokenize, sent_tokenize
from graph_model import graph_density, similarity_score, similarity_graph
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

    summary = select_criteria_sentences(
        sentence_scoring(sentence_tokens, tf_idf),
        prerequisite,
    )
    return summary


input = get_text()
wokens = word_tokenize(input)
stokens = sent_tokenize(input)
matrix = similarity_graph(stokens)
density = graph_density(matrix, stokens)
tf_idf = tf_idf_combine(
    word_freq_table(input), inverse_document_frequency(stokens, wokens)
)
similarity_score(density, sentence_scoring(stokens, tf_idf))
