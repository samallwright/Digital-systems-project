from token_frequencies import (
    word_freq_table,
    inverse_document_frequency,
    tf_idf_combine,
)
from word_weight import select_criteria_sentences, sentence_scoring
from nltk.tokenize import word_tokenize, sent_tokenize


def summarizer(title, content, prerequisite):
    sentence_tokens = sent_tokenize(content)
    word_tokens = word_tokenize(content)

    tf_idf = tf_idf_combine(
        word_freq_table(content),
        inverse_document_frequency(sentence_tokens, word_tokens),
    )
    summary = select_criteria_sentences(
        sentence_scoring(sentence_tokens, tf_idf),
        prerequisite,
    )

    return summary
