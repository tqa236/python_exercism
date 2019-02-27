"""Choose a response based on the phrase."""


def hey(phrase):
    """Choose a response based on the phrase."""
    phrase = phrase.rstrip()
    if phrase == "":
        return "Fine. Be that way!"
    is_question = phrase[-1] == "?"
    is_yelling = phrase == phrase.upper() and any(c.isalpha() for c in phrase)
    if is_question and is_yelling:
        return "Calm down, I know what I'm doing!"
    if is_question:
        return "Sure."
    if is_yelling:
        return "Whoa, chill out!"
    return "Whatever."
