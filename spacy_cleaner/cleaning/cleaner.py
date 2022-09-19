"""class `Cleaner` allows for configurable cleaning of text using `spaCy`.

Functionality:
    - Remove numbers.
    - Remove punctuation.
    - Remove part-of-speech tags.
    - Remove stopwords
    - Remove emails.
    - Remove URLs.
    - Lemmatization.

Typical usage example:
    ```python
    texts = ["I won £1000"]
    nlp = spacy.load("en_core_web_sm")
    cleaner = Cleaner(nlp, remove_numbers=True)
    clean_texts = cleaner.clean(texts, disable=["ner"])
    ```
"""
import typing
from typing import Any, Dict, Iterable, List, Optional, Tuple, Union

import warnings

import tqdm
from spacy import Language
from spacy.tokens import Doc, Token
from spacy.util import SimpleFrozenList

from spacy_cleaner.base.base_cleaner import BaseCleaner, _AnyContext
from spacy_cleaner.utils import exceptions


class Cleaner(BaseCleaner):
    """Cleans text using SpaCy!

    Args:
      model: The `spaCy` model to use.
      remove_numbers: Remove numbers from the text.
      remove_punctuation: Remove punctuation from the text.
      remove_pos: A list of POS tags to remove. For example, if you want to
          remove all nouns, you can pass in `['NOUN']`.
      remove_stopwords: Remove stopwords from the text.
      remove_email: Remove email addresses from the text.
      remove_url: Remove URLs from the text.
      lemmatize: If True, lemmatize the text.

    Raises:
        SpacyCleanerMisconfigurationError: When attempting to lemmatize when a
            `lemmatizer` is not in the model pipeline.

    Example:
        ```python
        nlp = spacy.load("en_core_web_sm")

        cleaner = Cleaner(
            spacy_model=nlp,
            lemmatize=True,
            remove_numbers=True,
        )

        raw_texts = [
            "Travelling to London with Cellan took 3 hours",
            "I love to go to the beach and see seagulls",
        ]

        cleaner.clean(raw_texts)
        ```
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
    ) -> None:
        super().__init__(model)

        if remove_pos is not None and "tagger" not in model.pipe_names:
            warnings.warn(
                "A `tagger` is not in your model pipeline. POS tags will not "
                "be removed."
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

    # noinspection PyTypeChecker,PyDefaultArgument,PydanticTypeChecker
    @typing.no_type_check
    def clean(  # noqa: F811
        self,
        texts: Union[
            Iterable[Union[str, Doc]],
            Iterable[Tuple[Union[str, Doc], _AnyContext]],
        ],
        *,
        as_tuples: bool = False,
        batch_size: Optional[int] = None,
        disable: Iterable[str] = SimpleFrozenList(),
        component_cfg: Optional[Dict[str, Dict[str, Any]]] = None,
        n_process: int = 1,
    ) -> List[str]:
        """Clean a stream of texts.

        Args:
            texts: A sequence of texts or docs to process.
            as_tuples: If set to True, inputs should be a sequence of
                (text, context) tuples. Output will then be a sequence of
                (doc, context) tuples. Defaults to False.
            batch_size: The number of texts to buffer.
            disable: The pipeline components to disable.
            component_cfg: An optional dictionary with extra keyword arguments
                for specific components.
            n_process: Number of processors to process texts. If `-1`, set
                `multiprocessing.cpu_count()`.

        Returns:
              A list of cleaned strings in the order of the original text.

        DOCS: https://spacy.io/api/language#pipe
        """
        return [
            self._clean_doc(doc)
            for doc in tqdm.tqdm(
                self.model.pipe(
                    texts,
                    as_tuples=as_tuples,
                    batch_size=batch_size,
                    disable=disable,
                    component_cfg=component_cfg,
                    n_process=n_process,
                ),
                desc="Cleaning Progress",
                total=len(texts),
            )
        ]

    def _clean_doc(self, doc: Doc) -> str:
        """Cleans a `spaCy` document.

        If the token is allowed, then append the token to the list of tokens.

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
        """Checks if a token is allowed.

        If the token does not meet the conditions then it is allowed.

        Args:
          tok: A `spaCy` token.

        Returns:
          True if the token is allowed and False if it is not allowed.
        """
        if isinstance(self.remove_pos, List) and tok.pos_ in self.remove_pos:
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
