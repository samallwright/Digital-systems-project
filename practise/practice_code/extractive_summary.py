from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize


text = "Various organisations today, be it online shopping, private sector organisations, government, tourism and catering industry, or any other institute that offers customer services, they are all concerned to learn their customer’s feedback each time their services are utilised. Now, consider that these companies are receiving an enormous amount of feedback and data every single day. It becomes quite a tedious task for the management to analyse each of these datapoints and come up with insights.",
"However, we have reached a point in technological advancements where technology can help with the tasks and we ourselves do not need to perform them. One such field that makes this happen is Machine Learning. Machines have become capable of understanding human language with the help of NLP or Natural Language Processing. Today, research is being done with the help of text analytics.",
"One application of text analytics and NLP is Text Summarization. Text Summarization Python helps in summarizing and shortening the text in the user feedback. It can be done with the help of an algorithm that can help in reducing the text bodies while keeping their original meaning intact or by giving insights into their original text."


stopwords = set (stopwords.words("english"))
words = word_tokenize(text)
freqTable = dict()

sentences = sent_tokenize(text)
sentenceValue = dict()

sumValues = 0
for sentence in sentenceValue:
    sumValues += sentenceValue[sentence]

average = int(sumValues / len(sentenceValue))

print(summary)