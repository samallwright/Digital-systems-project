from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import (
    PorterStemmer,
    LancasterStemmer,
    WordNetLemmatizer,
    SnowballStemmer,
)


def get_text() -> str:
    with open(
        # "Project\\project_code\\flask\\test_text.txt",
        # "r",
        # encoding="utf-8"
        "project_code\\flask\\test_text.txt",
        encoding="utf-8",
        # "test_text.txt", encoding="utf-8"
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


def word_stemming(text):
    ls = LancasterStemmer()
    lstems = {word: ls.stem(word) for word in text}
    return lstems
