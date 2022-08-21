"""Base cleaner classes."""

from typing import List

import abc

from spacy import Language


class BaseCleaner(abc.ABC):
    """Abstract base class that defines the interface for text cleaning.

    Attributes:
        model: SpaCy Language model for text cleaning.
    """

    def __init__(self, model: Language) -> None:
        """Initialises a SpaCy Language model for text cleaning."""
        self.model = model

    @abc.abstractmethod
    def clean(self, texts: List[str]) -> List[str]:
        """Cleans texts.

        Args:
          texts: List of texts to clean.

        Returns:
            Clean texts.
        """
