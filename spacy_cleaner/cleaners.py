"""Class `Cleaner` allows for configurable cleaning of text using `spaCy`."""

from typing import (
    Any,
    Callable,
    Dict,
    Iterable,
    List,
    Optional,
    Tuple,
    TypeVar,
    Union,
)

import spacy
import tqdm
from spacy import tokens, util

from spacy_cleaner.processing import helpers

_AnyContext = TypeVar("_AnyContext")


class Cleaner:
    """Cleans a sequence of texts.

    Args:
        model: A `spaCy` model.
        *processors: Callable token processors.

    Example:
        ```python
        import spacy
        from spacy_cleaner import Cleaner, processing

        model = spacy.blank("en")
        model.add_pipe("lemmatizer", config={"mode": "lookup"})
        model.initialize()

        texts = ["Hello, my name is Cellan! I love to swim!"]

        cleaner = Cleaner(
            model,
            processing.remove_stopword_token,
            processing.replace_punctuation_token,
            processing.mutate_lemma_token,
        )
        cleaner.clean(texts)
        ['hello _IS_PUNCT_ Cellan _IS_PUNCT_ love swim _IS_PUNCT_']
        ```
    """

    def __init__(
        self,
        model: spacy.Language,
        *processors: Callable[[tokens.Token], Union[str, tokens.Token]],
    ) -> None:
        self.model = model
        self.processors = processors

    # noinspection PyTypeChecker,PyDefaultArgumentdd,PyDefaultArgument
    def clean(  # noqa: PLR0913
        self,
        texts: Union[
            Iterable[Union[str, tokens.Doc]],
            Iterable[Tuple[Union[str, tokens.Doc], _AnyContext]],
        ],
        *,
        as_tuples: bool = False,
        batch_size: Optional[int] = None,
        disable: Iterable[str] = util.SimpleFrozenList(),
        component_cfg: Optional[Dict[str, Dict[str, Any]]] = None,
        n_process: int = 1,
    ) -> List[str]:
        """Clean a stream of texts.

        Args:
            texts: A sequence of texts or docs to process.
            as_tuples: If set to True, inputs should be a sequence of
                (text, context) tuples. Output will then be a sequence of
                (doc, context) tuples.
            batch_size: The number of texts to buffer.
            disable: The pipeline components to disable.
            component_cfg: An optional dictionary with extra keyword arguments
                for specific components.
            n_process: Number of processors to process texts. If `-1`, set
                `multiprocessing.cpu_count()`.

        Returns:
              A list of cleaned strings in the order of the original text.

        References:
            https://spacy.io/api/language#pipe
        """
        return [
            helpers.clean_doc(doc, *self.processors)
            for doc in tqdm.tqdm(
                self.model.pipe(  # type: ignore[call-overload]
                    texts,
                    as_tuples=as_tuples,
                    batch_size=batch_size,
                    disable=disable,
                    component_cfg=component_cfg,
                    n_process=n_process,
                ),
                desc="Cleaning Progress",
                total=len(texts),  # type: ignore[arg-type]
            )
        ]
