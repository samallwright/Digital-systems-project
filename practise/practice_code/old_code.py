def top_ten_comp(input_text):
    word_tokens = word_tokenize(input_text)

    token_dist = nltk.FreqDist(
        word.lower()
        for word in word_tokens
        if word.lower() not in stop_words and word.isalnum()
    )

    mostCommon = token_dist.most_common(10)
    return mostCommon
