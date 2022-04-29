from numpy import sort


# from text_functions import get_text


def sentence_scoring(sentence_tokens, scored_words: dict) -> dict:
    """Combines scores from word frequency/word total to score
    every sentence in document"""
    weighted_sentences = dict()
    for sentence in sentence_tokens:
        for word in scored_words:
            if word.lower() in sentence.lower():
                if sentence in weighted_sentences:
                    weighted_sentences[sentence] += scored_words[word]
                else:
                    weighted_sentences[sentence] = scored_words[word]
    return weighted_sentences


def select_criteria_sentences(
    weighted_sentences: dict, prerequisite: int, size: int
) -> str:
    if size != 0:
        selection = sentences(weighted_sentences, size)
    else:
        selection = quartile(weighted_sentences, prerequisite)
    return str("".join(selection)), len(weighted_sentences), len(selection)


def quartile(weighted_sentences: dict, prerequisite: int) -> list:
    quartile_position = prerequisite_percentage(weighted_sentences, prerequisite)
    sentences = [
        sentences_scores
        for sentences_scores in weighted_sentences
        if weighted_sentences[sentences_scores] >= quartile_position
    ]
    return sentences


def prerequisite_percentage(weighted_sentences: dict, prerequisite: int) -> int:
    """0=none, 1= 25%cutm, 2=50%cut, 3=75%cut"""
    quartile = get_quartile(weighted_sentences)
    sorted_importance = sorted(list(weighted_sentences.values()))
    prerequisite_position = sorted_importance[quartile * prerequisite]
    return prerequisite_position


def get_quartile(sents: dict) -> int:
    size = len(list(sents.values()))
    while size % 4 != 0:
        size -= 1
    return int(size / 4)


def sentences(weighted_sentences: dict, size: int) -> list:
    sorted_importance = sorted(list(weighted_sentences.values()))
    size_score = sorted_importance[-size]
    sentences = [
        sentence
        for sentence, score in weighted_sentences.items()
        if score >= size_score
    ]
    return sentences


# input_text = get_text()
# print(sentence_scoring(sent_tokenize(input_text), word_freq_table(input_text)))
# print(
#     prerequisite_percentage(
#         sentence_scoring(sent_tokenize(input_text), word_freq_table(input_text)), 3
#     )
# )
# print(
#     select_criteria_sentences(
#         sentence_scoring(sent_tokenize(input_text), word_freq_table(input_text)), 3
#     )
# )
# tf_idf = tf_idf_combine(
#     word_freq_table(input_text),
#     inverse_document_frequency(sent_tokenize(input_text), word_tokenize(input_text)),
# )
# print(sentence_scoring(sent_tokenize(input_text), tf_idf))


# 1) number of times a word appears in
# the article, (2) the number of words in the sentence that also appear
# in the title of the article, or in section headings, (3) position of the
# sentence in the article and in the section, (4) the number of sen-
# tence words matching a pre-compiled list of cue words such as “In
# sum”
