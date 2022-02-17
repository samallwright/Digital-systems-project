import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words('english'))

def stop_word_vomit(input_text):
	word_tokens = word_tokenize(input_text)

	filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]

	filtered_sentence = []

	for w in word_tokens:
		if w not in stop_words:
			filtered_sentence.append(w)

	return ' '.join(filtered_sentence)
