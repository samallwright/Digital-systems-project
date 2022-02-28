import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from text_functions import get_text

stop_words = set(stopwords.words("english"))


def stop_word_removal(input_text):
    word_tokens = word_tokenize(input_text)
    filtered_sentence = [
        word
        for word in word_tokens
        if not word.lower() in stop_words and word.isalnum()
    ]

    return " ".join(filtered_sentence)


# print(stop_word_removal(get_text()))
# use marking criteria
