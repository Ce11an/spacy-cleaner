"""Module containing functions that mutate spaCy tokens with strings."""

from spacy.tokens import Token


def mutate_lemma_token(tok: Token) -> str:
    """Mutate token to its lemma.

    Args:
        tok: Token

    Returns:
        The lemma of the token.
    """
    return tok.lemma_
