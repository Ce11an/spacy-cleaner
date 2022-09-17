"""Mutate `spaCy` tokens.

This module contains functions that assist with mutating `spaCy` tokens.

A typical usage example:
    ```python
    import spacy

    nlp = spacy.load("en_core_web_md")
    doc = nlp("swimming")
    tok = doc[0]

    mutate_lemma_toke(tok)
    ```
    The lemma of `swimming` is `swim`.
"""

from spacy.tokens import Token


def mutate_lemma_token(tok: Token) -> str:
    """Mutate a token to its lemma.

    Args:
        tok: Token

    Returns:
        The lemma of the token.
    """
    return tok.lemma_
