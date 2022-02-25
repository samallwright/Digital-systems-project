import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from open_test_text import get_text

stop_words = set(stopwords.words("english"))


def stop_word_vomit(input_text):
    word_tokens = word_tokenize(input_text)
    filtered_sentence = [
        word
        for word in word_tokens
        if not word.lower() in stop_words and word.isalnum()
    ]

    return " ".join(filtered_sentence)


# print(stop_word_vomit(get_text()))
# use marking criteria
