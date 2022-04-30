from re import A

from pyparsing import original_text_for
from summarizer import summarizer, word_removal
from token_frequencies import (
    token_dists,
    inverse_document_frequency,
    tf_idf_combine,
    position_score,
    combine_position_tf_idf,
)
from word_weight import (
    sentence_scoring,
    sentences,
    get_quartile,
    prerequisite_percentage,
    quartile,
    select_criteria_sentences,
)
from cue_words import find_cue_words, cue_score, cue_word_combine
from graph_model import (
    words_in_common,
    similarity_graph,
    graph_density,
    maximum_similarity,
    weakest_links,
)
from text_functions import word_stemming, stop_word_removal, get_text
from nltk import word_tokenize, sent_tokenize

# pytest test.py


# def run_unit_state_tests():
#     unit_list = [
#         test_word_stemming,
#         test_stop_word_removal,
#         test_summarizer,
#         test_token_dists,
#         test_inverse_document_frequency,
#         test_tf_idf_combine,
#         test_position_score,
#         test_combine_position_tf_idf,
#         test_find_cue_words,
#         test_cue_score,
#         test_cue_word_combine,
#         test_words_in_common,
#         test_similarity_graph,
#         test_graph_density,
#         test_maximum_similarity,
#         test_weakest_links,
#         test_word_removal,
#         test_sentence_scoring,
#         test_sentences,
#         test_get_quartile,
#         test_prerequisite_percentage,
#         test_quartile,
#         test_select_criteria_sentences,
#     ]
#     for test in unit_list:
#         result = test()
#         print(f"{test.__name__} : {result}")


def test_always_pass():
    assert True


def test_always_fail():
    assert False


def test_word_stemming():
    original_text = get_text()
    text_tokens = word_tokenize(original_text)
    stems = word_stemming(text_tokens)
    result = stems["detection"]
    comparison = "detect"
    assert result == comparison


def test_stop_word_removal():
    original_text = "To test or not to test"
    result = stop_word_removal(original_text)

    assert result == ["test", "test"]


def test_summarizer_types():
    original_text = get_text()
    summary, rouge, removed, percentage, speed = summarizer(
        "Venus test text title", original_text, "query words", "stigma words", 0, 10
    )
    assert type(summary) == str
    assert type(rouge) == str
    assert type(removed) == int
    assert type(percentage) == float
    assert type(speed) == float


def test_summary():
    original_text = get_text()
    summary, _, removed, *_ = summarizer(
        "Venus alien life test title",
        original_text,
        "query words",
        "stigma words",
        0,
        10,
    )
    assert int(removed) >= 1
    assert len(summary) < len(original_text)


def test_token_dists():
    original_text = get_text()
    scores = token_dists(original_text)
    test_scores = {
        "Possible": 0.010498687664041995,
        "life": 0.0026246719160104987,
        "Venus": 0.0026246719160104987,
        "discovery": 0.0026246719160104987,
        "bacteria": 0.0026246719160104987,
    }
    for word in test_scores.keys():
        assert scores[word] == test_scores[word]


def test_inverse_document_frequency():
    text = get_text()
    sents = sent_tokenize(text)
    words = word_tokenize(text)
    scores = inverse_document_frequency(sents, words)
    test_scores = {
        "Possible": 1.0479235523171828 + 0j,
        "life": 0.34895354798116396 + 0j,
        "Venus": 0.4836521218786201 + 0j,
        "discovery": 0.9809767626865695 + 0j,
        "bacteria": 1.8260748027008262 + 0j,
    }
    for word in test_scores.keys():
        assert scores[word] == test_scores[word]


# text = get_text()
# print(inverse_document_frequency(sent_tokenize(text), word_tokenize(text)))


def test_tf_idf_combine():
    text = get_text()
    sents = sent_tokenize(text)
    words = word_tokenize(text)
    tf_scores = token_dists(text)
    idf_scores = inverse_document_frequency(sents, words)
    result = tf_idf_combine(tf_scores, idf_scores)
    test_scores = {
        "Possible": 0.011001822071571472 + 0j,
        "life": 0.0009158885773783831 + 0j,
        "Venus": 0.001269428141413701 + 0j,
        "discovery": 0.002574742159282335 + 0j,
        "bacteria": 0.004792847251183271 + 0j,
    }
    assert type(result) == dict
    for word in test_scores.keys():
        assert result[word] == test_scores[word]


def test_position_score_types():
    result = position_score(sent_tokenize(get_text()))

    assert type(result) == dict
    assert type(list(result.items())[0]) == tuple
    assert type(list(result.items())[0][0]) == int
    assert type(list(result.items())[0][1]) == float


def test_position_score_curve():
    result = position_score(sent_tokenize(get_text()))
    assert len(list(result.items())) == len(list(sent_tokenize(get_text())))
    assert list(result.items())[0][1] == list(result.items())[-1][1]


def test_combine_position_tf_idf_types():
    text = get_text()
    sents = sent_tokenize(text)
    words = word_tokenize(text)
    tf_idf = tf_idf_combine(
        token_dists(text),
        inverse_document_frequency(sents, words),
    )
    weights = sentence_scoring(sents, tf_idf)
    curve = position_score(sents)
    result = combine_position_tf_idf(weights, curve)

    assert type(result) == dict
    assert type(list(result.items())[0][0]) == str
    assert type(list(result.items())[0][1]) == float


def test_combine_position_tf_idf_value():
    text = get_text()
    sents = sent_tokenize(text)
    words = word_tokenize(text)
    tf_idf = tf_idf_combine(
        token_dists(text),
        inverse_document_frequency(sents, words),
    )
    weights = sentence_scoring(sents, tf_idf)
    curve = position_score(sents)
    result = combine_position_tf_idf(weights, curve)
    assert (
        list(result.values())[0]
        == list(weights.values())[0].real + list(curve.values())[0]
    )


def test_type_cue_words():
    sents = sent_tokenize(get_text())
    cue_freq = find_cue_words("Venus test text title", "query", "stigma", sents)
    assert type(cue_freq) == dict
    assert type(list(cue_freq.keys())[0]) == int
    assert type(list(cue_freq.keys())[1]) == int


def test_find_cue_words():
    sents = sent_tokenize(get_text())
    cue_freq = find_cue_words("Venus test text title", "query", "stigma", sents)
    assert list(cue_freq.keys())[0] == 0
    assert list(cue_freq.values())[0] == 1


def test_cue_score():
    cue_score
    result = False
    assert result


def test_cue_word_combine():
    cue_word_combine
    result = False
    assert result


def test_words_in_common():
    words_in_common
    result = False
    assert result


def test_similarity_graph():
    similarity_graph
    result = False
    assert result


def test_graph_density():
    graph_density
    result = False
    assert result


def test_maximum_similarity():
    maximum_similarity
    result = False
    assert result


def test_weakest_links():
    weakest_links
    result = False
    assert result


def test_word_removal():
    word_removal
    result = False
    assert result


def test_sentence_scoring():
    sentence_scoring
    result = False
    assert result


def test_sentences():
    sentences
    result = False
    assert result


def test_get_quartile():
    get_quartile
    result = False
    assert result


def test_prerequisite_percentage():
    prerequisite_percentage
    result = False
    assert result


def test_quartile():
    quartile
    result = False
    assert result


def test_select_criteria_sentences():
    select_criteria_sentences
    result = False
    assert result


# run_unit_state_tests()
