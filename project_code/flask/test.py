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
    text = get_text()
    sents = sent_tokenize(text)
    freqs = find_cue_words("Venus test text title", "query", "stigma", sents)
    score = cue_score(freqs, sents)

    assert type(score) == dict
    for pos, density in score.items():
        if score[pos] != 0:
            assert len(word_tokenize(sents[0])) != 0
            density = freqs[pos] / len(word_tokenize(sents[pos]))
            assert score[pos] == density


def test_cue_word_combine():
    luhn_sentences = {"sentence": 1}
    score = {0: 2}

    result = cue_word_combine(luhn_sentences, score)
    assert type(result) == dict
    for sentence, value in result.items():
        assert sentence == "sentence"
        assert value == 3
        assert value == luhn_sentences["sentence"] + score[0]


def test_words_in_common():
    result = words_in_common("dummy sentence one", "dummy sentence two")
    assert result == 2


def test_similarity_graph():
    text = [
        "sentence one for similarity. ",
        "sentence two is different. ",
        "sentence three more so but still different. ",
    ]
    result = similarity_graph(text)
    assert type(result) == list
    assert result[0] == [1, 1]
    assert result[1] == [1, 2]
    assert result[2] == [1, 2]


def test_graph_density():
    sents = [
        "sentence one for similarity. ",
        "sentence two is different. ",
        "sentence three more so but still different. ",
    ]
    matrix = [[1, 1], [1, 2], [1, 2]]

    result = graph_density(matrix, sents)
    assert type(result) == list
    assert type(result[0]) == dict
    pos, density = result[0].items()
    assert density == (1, 0.2)
    pos, density = result[1].items()
    assert density == (1, 0.4)
    pos, density = result[2].items()
    assert density == (1, 0.4)


def test_maximum_similarity():
    result = maximum_similarity([{1: 0.2}, {1: 0.4}, {1: 0.4}])
    max_sentence = max(result.items(), key=lambda k: k[1])
    assert max_sentence == 0


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
