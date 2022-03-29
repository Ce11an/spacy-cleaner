import logging

import spacy


def download_model(spacy_model: str) -> None:
    """
    Downloads a spaCy model.

    :param spacy_model: spaCy model name.
    """
    logging.info("Downloading spaCy model: {spacy_model}")
    spacy.cli.download(spacy_model)
    logging.info("Finished downloading model")


def load_model(spacy_model: str) -> spacy.language.Language:
    """
    Loads a spaCy model.

    :param spacy_model: spaCy model name.

    :return: spaCy Language model.

    :raises OSError: If the spaCy model is not installed.
    """
    try:
        return spacy.load(spacy_model, disable=["parser", "ner"])
    except OSError:
        raise OSError("Please download a spaCy model: SpacyCleaner.download_model()")
