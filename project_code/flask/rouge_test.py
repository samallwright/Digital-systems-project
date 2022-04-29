from rouge import Rouge


def rouge_1(summary, original):
    rouge = Rouge()
    print(rouge.get_scores(summary, original))
