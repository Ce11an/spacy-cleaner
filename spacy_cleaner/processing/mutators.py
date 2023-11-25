"""Mutate `spaCy` tokens.

This module contains functions that assist with mutating `spaCy` tokens.

A typical usage example:
    ```python
    import spacy
    from spacy_cleaner import processing

    nlp = spacy.load("en_core_web_md")
    doc = nlp("swimming")
    tok = doc[0]

    processing.mutate_lemma_toke(tok)
    ```
    The lemma of `swimming` is `swim`.
"""

from spacy import tokens


def mutate_lemma_token(tok: tokens.Token) -> str:
    """Mutate a token to its lemma.

    Args:
        tok: tokens.Token

    Returns:
        The lemma of the token.
    """
    return tok.lemma_
