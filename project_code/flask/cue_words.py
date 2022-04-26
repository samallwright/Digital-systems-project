from nltk import word_tokenize

from text_functions import stop_word_removal


def find_cue_words(title: str, query: str, content: str) -> list:
    """uses cue and query words to influence weighting for summarisation"""
    cue_words = stop_word_removal(title + "" + query)
    cue_words = set(word for word in cue_words)
    # cue_words = FreqDist(word.lower() for word in cue_words)
    cue_count = dict()
    for sentence in content:
        removed = [word.lower() for word in stop_word_removal(sentence)]
        # print(sentence)
        # print(removed)
        for cue_word in cue_words:
            # print(cue_word)
            if cue_word.lower() in removed:
                print(content.index(sentence))
                if content.index(sentence) not in cue_count:
                    print("sentence not in")
                    cue_count[content.index(sentence)] = 1
                elif cue_word in sentence:
                    print("is in")
                    cue_count[content.index(sentence)] += 1
            else:
                cue_count[content.index(sentence)] = 0
            print(cue_count[content.index(sentence)])
    print(cue_count)
    return cue_count


def cue_score(cue_frequencies):
    sentence_length = [len(word_tokenize(sentence)) for sentence in cue_frequencies]
    cue_density = dict()
    for sentence, score in cue_frequencies.items():
        cue_density[sentence] = score / sentence_length[sentence]
    print(cue_density)
    return cue_density


def cue_word_combine(luhn_sentences, cue_words_freq):
    edmundson = {
        sentence: value * cue_words_freq for sentence, value in luhn_sentences.items()
    }
    print(edmundson)
    return edmundson
