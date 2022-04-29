from rouge import Rouge


def rouge_1(summary, original):
    rouge = Rouge()
    scores =(rouge.get_scores(summary, original))
    return scores
