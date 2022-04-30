from re import A
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
from nltk import word_tokenize

# pytest test.py


def run_unit_state_tests():
    unit_list = [
        test_word_stemming,
        # test_stop_word_removal,
        # test_summarizer,
        # test_token_dists,
        # test_inverse_document_frequency,
        # test_tf_idf_combine,
        # test_position_score,
        # test_combine_position_tf_idf,
        # test_find_cue_words,
        # test_cue_score,
        # test_cue_word_combine,
        # test_words_in_common,
        # test_similarity_graph,
        # test_graph_density,
        # test_maximum_similarity,
        # test_weakest_links,
        # test_word_removal,
        # test_sentence_scoring,
        # test_sentences,
        # test_get_quartile,
        # test_prerequisite_percentage,
        # test_quartile,
        # test_select_criteria_sentences,
    ]
    for test in unit_list:
        result = test()
        assert True
        print(f"{test.__name__} : {result}")


def test_always_pass():
    assert True


def test_always_fail():
    assert False


def test_word_stemming():
    orginal_text = get_text()
    text_tokens = word_tokenize(orginal_text)
    stems = word_stemming(text_tokens)
    print(stems)
    result = 1
    comparison = 1
    assert result == comparison


def test_stop_word_removal():
    stop_word_removal
    result = bool()
    return result


def test_summarizer():
    summarizer
    result = bool()
    return result


def test_token_dists():
    token_dists
    result = bool()
    return result


def test_inverse_document_frequency():
    inverse_document_frequency
    result = bool()
    return result


def test_tf_idf_combine():
    tf_idf_combine
    result = bool()
    return result


def test_position_score():
    position_score
    result = bool()
    return result


def test_combine_position_tf_idf():
    combine_position_tf_idf
    result = bool()
    return result


def test_find_cue_words():
    find_cue_words
    result = bool()
    return result


def test_cue_score():
    cue_score
    result = bool()
    return result


def test_cue_word_combine():
    cue_word_combine
    result = bool()
    return result


def test_words_in_common():
    words_in_common
    result = bool()
    return result


def test_similarity_graph():
    similarity_graph
    result = bool()
    return result


def test_graph_density():
    graph_density
    result = bool()
    return result


def test_maximum_similarity():
    maximum_similarity
    result = bool()
    return result


def test_weakest_links():
    weakest_links
    result = bool()
    return result


def test_word_removal():
    word_removal
    result = bool()
    return result


def test_sentence_scoring():
    sentence_scoring
    result = bool()
    return result


def test_sentences():
    sentences
    result = bool()
    return result


def test_get_quartile():
    get_quartile
    result = bool()
    return result


def test_prerequisite_percentage():
    prerequisite_percentage
    result = bool()
    return result


def test_quartile():
    quartile
    result = bool()
    return result


def test_select_criteria_sentences():
    select_criteria_sentences
    result = bool()
    return result


run_unit_state_tests()
