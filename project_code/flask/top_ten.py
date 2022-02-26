import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import FreqDist, ngrams
from open_test_text import get_text
from stop_word import stop_word_vomit

stop_words = set(stopwords.words("english"))


def token_dists(input_text: str) -> FreqDist:
    word_tokens = word_tokenize(stop_word_vomit(input_text))
    token_dist = FreqDist(word.lower() for word in word_tokens)
    return token_dist


def top_ten(tokens: FreqDist) -> list:
    return tokens.most_common(10)


def bottom_10(tokens: FreqDist) -> list:
    return tokens.most_common()[-10:]


def single_occurrence(tokens: FreqDist) -> list:
    list = tokens.most_common()[-1000:]
    new_list = []
    for tuple in list:
        if tuple[1] == 1:
            new_list.append(tuple)
    return new_list


def bigrams_trigrams(sentence_tokens: FreqDist) -> dict:
    all_counts = dict()
    for size in 2, 3:
        all_counts[size] = FreqDist(ngrams(sentence_tokens, size))
    return all_counts


input_text = get_text()
print(top_ten(token_dists(input_text)))
# print(bottom_10(token_dists(input_text)))
# print(single_occurrence(token_dists(input_text)))
# x = bigrams_trigrams(token_dists(input_text))
# for item in x.items():
#     print(item)


# stitching sentences with top ten word
# also important infrquent words
# how to select important infrequent
# any sentence with top 3 words in, + any sentence with 10 least common words in, ordered
# word pairs? (bigrams and trigrams)
