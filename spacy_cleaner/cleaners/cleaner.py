from typing import List, Optional

import warnings

import tqdm
from spacy import Language
from spacy.tokens import Doc, Token

from spacy_cleaner import exceptions
from spacy_cleaner.cleaners.base_cleaner import BaseCleaner


class Cleaner(BaseCleaner):
    """
    Cleans text using SpaCy!

    Args:
      model: The spaCy model to use.
      remove_numbers: Remove numbers from the text. Defaults to False.
      remove_punctuation: Remove punctuation from the text. Defaults to True.
      remove_pos: A list of POS tags to remove. For example, if you want to remove all nouns,
        you can pass in ['NOUN'].
      remove_stopwords: Remove stopwords from the text. Defaults to True.
      remove_email: Remove email addresses from the text. Defaults to True.
      remove_url: Remove URLs from the text. Defaults to True.
      lemmatize: If True, lemmatize the text. Defaults to False.
    """

    def __init__(
        self,
        model: Language,
        remove_numbers: bool = False,
        remove_punctuation: bool = True,
        remove_pos: Optional[List[str]] = None,
        remove_stopwords: bool = True,
        remove_email: bool = True,
        remove_url: bool = True,
        lemmatize: bool = False,
        **kwargs,
    ) -> None:
        super().__init__(model)

        if remove_pos is not None and "tagger" not in model.pipe_names:
            warnings.warn(
                "A `tagger` is not in your model pipeline. POS tags will not be removed."
            )

        if lemmatize and "lemmatizer" not in model.pipe_names:
            raise exceptions.SpacyCleanerMisconfigurationError(
                "A `lemmatizer` is not in your model pipeline."
            )

        self.remove_numbers = remove_numbers
        self.remove_punctuation = remove_punctuation
        self.remove_pos = remove_pos
        self.remove_stopwords = remove_stopwords
        self.remove_email = remove_email
        self.remove_url = remove_url
        self.lemmatize = lemmatize
        self.kwargs = kwargs

    def clean(self, texts: List[str], *args, **kwargs) -> List[str]:
        """
        For each document in the list of documents, clean the document using the model's pipe function

        Args:
          texts: List of texts to clean.
          args: Arguments for pipe method: https://spacy.io/api/language#pipe
          kwargs: Keyword Arguments for pipe method: https://spacy.io/api/language#pipe

        Returns:
          A list of cleaned documents.
        """
        return [
            self._clean_doc(doc)
            for doc in tqdm.tqdm(
                self.model.pipe(texts, *args, **kwargs),
                desc="Cleaning Progress",
                total=len(texts),
            )
        ]

    def _clean_doc(self, doc: Doc) -> str:
        """
        If the token is allowed, then append the lemma of the token to the list of tokens.

        Args:
          doc: The document to be cleaned.

        Returns:
          A string of the cleaned document.
        """
        tokens = []
        for tok in doc:
            if not self._allowed_token(tok):
                continue
            if self.lemmatize:
                tokens.append(str(tok.lemma_))
            else:
                tokens.append(str(tok))
        return " ".join(tokens).lower()

    def _allowed_token(self, tok: Token) -> bool:
        """
        If the token does not meet the conditions then it is allowed.

        Args:
          tok: A SpaCy token.

        Returns:
          True if the token is allowed and False if it is not allowed.
        """
        if isinstance(self.remove_pos, List) and tok.pos_:
            return False
        elif self.remove_stopwords and tok.is_stop:
            return False
        elif self.remove_punctuation and tok.is_punct:
            return False
        elif self.remove_numbers and tok.like_num:
            return False
        elif self.remove_email and tok.like_email:
            return False
        elif self.remove_url and tok.like_url:
            return False
        elif tok.text.strip() == "":
            return False
        else:
            return True
