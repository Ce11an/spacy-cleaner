"""Class `Pipeline` allows for configurable cleaning of text using `spaCy`."""

import typing
from typing import Any, Callable, Dict, Iterable, List, Optional, Tuple, Union

import tqdm
from spacy import Language
from spacy.tokens import Doc, Token
from spacy.util import SimpleFrozenList

from spacy_cleaner import processing
from spacy_cleaner.base.base_cleaner import BaseCleaner, _AnyContext


class Pipeline(BaseCleaner):
    """Cleans a sequence of texts.

    Args:
        model: A `spaCy` model.
        *processors: Callable token processors.

    Example:
        ```python
        import spacy

        model = spacy.blank("en")
        model.add_pipe("lemmatizer", config={"mode": "lookup"})
        model.initialize()

        texts = ["Hello, my name is Cellan! I love to swim!"]

        pipline = Pipeline(
            model,
            remove_stopword_token,
            replace_punctuation_token,
            mutate_lemma_token,
        )
        pipline.clean(texts)
        ['Hello _IS_PUNCT_ Cellan _IS_PUNCT_ love swim _IS_PUNCT_']
        ```
    """

    def __init__(
        self, model: Language, *processors: Callable[[Token], Union[str, Token]]
    ) -> None:
        super().__init__(model)
        self.processors = processors

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
                (doc, context) tuples.
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
            processing.clean_doc(doc, *self.processors)
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
