"""Base cleaner classes."""

from typing import Any, Dict, Iterable, List, Optional, Tuple, TypeVar, Union

import abc

from spacy import Language
from spacy.tokens import Doc
from spacy.util import SimpleFrozenList

# Type variable for contexts piped with documents
_AnyContext = TypeVar("_AnyContext")


class BaseCleaner(abc.ABC):
    """Abstract base class that defines the interface for text cleaning.

    Attributes:
        model: SpaCy Language model for text cleaning.
    """

    def __init__(self, model: Language) -> None:
        """Initialises a SpaCy Language model for text cleaning."""
        self.model = model

    # noinspection PyDefaultArgument
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
            as_tuples: If set to True, inputs should be a sequence of (text, context) tuples. Output will then be a
                sequence of (doc, context) tuples. Defaults to False.
            batch_size (Optional[int]): The number of texts to buffer.
            disable: The pipeline components to disable.
            component_cfg: An optional dictionary with extra keyword arguments for specific components.
            n_process: Number of processors to process texts. If -1, set `multiprocessing.cpu_count()`.

        Returns:
              A list of cleaned strings in the order of the original text.

        DOCS: https://spacy.io/api/language#pipe
        """
