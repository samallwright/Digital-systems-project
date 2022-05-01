from rouge import Rouge


def rouge_1(summary, original):
    rouge = Rouge()
    # original = """
    # James Webb, astronomy's new super space telescope, has taken another major step to full operational capability.
    # The $10bn successor to the Hubble Space Telescope is now fully focused and aligned.
    # It just remains to check that the instruments are properly calibrated - that they are delivering their data in a way that's expected and understood.
    # Scientists intend to use Webb and its remarkable 6.5m-wide mirror to capture events that occurred just a couple of hundred million years after the Big Bang.
    # A joint endeavour of Nasa, Esa and the Canadian Space Agency, Webb is the biggest telescope ever sent into space."""
    # original = """
    # Amazon has reported its first quarterly loss since 2015 due to lower online sales and a fall in the value of
    # its shares in electric vehicle firm Rivian.

    # Growth in other parts of Amazon's business, including cloud computing and advertising, remained strong.

    # The company reported a loss of $3.8bn, mainly due to a loss of $7.6bn on the value of its stake in Rivian.

    # Overall, Amazon forecast sales growth of as little as 3% in the coming months - a marked slowdown from the double
    # digit growth it has enjoyed in recent years, even before the pandemic.

    # Amazon has already said it is raising the price of its Prime service, which gives subscribers access to
    # benefits like faster shipping, for US customers, citing increased wage and shipping costs.


    # """
#     original = """Sir David Attenborough has been named a Champion of the Earth by the UN's Environment Programme.

# The prestigious award recognises the 95-year-old's commitment to telling stories about the natural world and climate change.

# Accepting the award, Sir David said the world must take action now to protect nature and the planet.


# Sir David said that environmental success stories should give us hope that change is possible.


# "We know what the problems are and we know how to solve them. All we lack is unified action." """


    scores = rouge.get_scores(summary, original)
    return scores
