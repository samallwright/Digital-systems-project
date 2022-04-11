from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def get_text() -> str:
    with open(
        # "Project\\project_code\\flask\\test_text.txt", "r", encoding="utf-8"
        "project_code\\flask\\test_text.txt",
        encoding="utf-8",
    ) as test_text:
        text = test_text.read()
    return text


stop_words = set(stopwords.words("english"))


def stop_word_removal(input_text):
    word_tokens = word_tokenize(input_text)
    filtered_sentence = [
        word
        for word in word_tokens
        if not word.lower() in stop_words and word.isalnum()
    ]

    # return " ".join(filtered_sentence)
    return filtered_sentence

def word_query(input) -> list:
    # return important key word sentences + words from title?
    return


def cue_words():
    return


def stigma_words():
    return
