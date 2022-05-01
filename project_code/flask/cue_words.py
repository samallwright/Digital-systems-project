from nltk import word_tokenize

from text_functions import stop_word_removal


def find_cue_words(title: str, query: str, stigma: str, content: str) -> dict:
    """uses cue and query words to influence weighting for summarisation"""
    cue_words = set(word for word in stop_word_removal(title + " " + query))
    stigma_words = set(word.lower() for word in stop_word_removal(stigma))
    cue_count = dict()
    for sentence in content:
        removed = [word.lower() for word in stop_word_removal(sentence)]
        cue_count[content.index(sentence)] = 0
        for cue_word in cue_words:
            if cue_word.lower() in removed:
                cue_count[content.index(sentence)] += 1
            elif cue_word.lower() in stigma_words:
                cue_count[content.index(sentence)] -= 10
    return cue_count


def cue_score(cue_frequencies: dict, sentences) -> dict:
    sentence_length = [len(word_tokenize(sentence)) for sentence in sentences]
    cue_score = dict()
    for sentence_position, count in cue_frequencies.items():
        if count != 0:
            cue_score[sentence_position] = count / sentence_length[sentence_position]
        else:
            cue_score[sentence_position] = 0
    return cue_score


def cue_word_combine(luhn_sentences, cue_score):
    sentences = list(luhn_sentences.keys())
    edmundson = dict()
    edmundson = {
        sentence: value + cue_score[sentences.index(sentence)]
        for (sentence, value) in luhn_sentences.items()
    }
    return edmundson
