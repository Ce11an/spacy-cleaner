from typing import List

import abc

from spacy import Language


class BaseCleaner(abc.ABC):
    """
    Abstract base class that defines the interface for cleaning data.

    Args:
        model: A spaCy text-processing pipeline.
    """

    def __init__(self, model: Language) -> None:
        self.model = model

    @abc.abstractmethod
    def clean(self, texts: List[str]) -> List[str]:
        """
        Cleans text.

        Args:
          texts: List of texts to clean.

        Returns:
            Clean texts.
        """
