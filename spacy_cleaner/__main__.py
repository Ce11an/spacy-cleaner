# type: ignore[attr-defined]
from typing import List, Optional

import typer
from rich.console import Console

from spacy_cleaner import version
from spacy_cleaner.example import run_clean

app = typer.Typer(
    name="spacy-cleaner",
    help="Easily clean text with spaCy!",
    add_completion=False,
)
console = Console()


def version_callback(print_version: bool) -> None:
    """Print the version of the package."""
    if print_version:
        console.print(f"[yellow]spacy-cleaner[/] version: [bold blue]{version}[/]")
        raise typer.Exit()


@app.command()
def main(
    texts: List[str] = typer.Option(
        ..., help="A string of text you would like to clean."
    ),
    remove_numbers: bool = typer.Option(
        False,
        "-rn",
        "--remove_numbers",
        case_sensitive=False,
        help="Set to True to remove numbers from texts.",
    ),
    remove_punctuation: bool = typer.Option(
        True,
        "-rp",
        "--remove_punctuation",
        case_sensitive=False,
        help="Set to True to remove punctuation from texts.",
    ),
    remove_pos: Optional[List[str]] = typer.Option(
        None,
        "-rpos",
        "--remove_pos",
        case_sensitive=False,
        help="List of POS tags to remove from texts.",
    ),
    remove_stopwords: bool = typer.Option(
        True,
        "-rs",
        "--remove_stopwords",
        case_sensitive=False,
        help="Set to True to remove stopwords from texts.",
    ),
    extra_stopwords: Optional[List[str]] = typer.Option(
        None,
        "-res",
        "--extra_stopwords",
        case_sensitive=False,
        help="List of extra stopwords to remove from texts.",
    ),
    remove_email: bool = typer.Option(
        True,
        "-re",
        "--remove_email",
        case_sensitive=False,
        help="Set to True to remove emails from texts.",
    ),
    remove_url: bool = typer.Option(
        True,
        "-rurl",
        "--remove_url",
        case_sensitive=False,
        help="Set to True to remove urls from texts.",
    ),
    lemmatize: bool = typer.Option(
        True,
        "-l",
        "--lemmatize",
        case_sensitive=False,
        help="Set to True to lemmatize texts.",
    ),
    print_version: bool = typer.Option(
        None,
        "-v",
        "--version",
        callback=version_callback,
        is_eager=True,
        help="Prints the version of the spacy-cleaner package.",
    ),
) -> None:

    clean_texts: List[str] = run_clean(
        texts=texts,
        remove_numbers=remove_numbers,
        remove_punctuation=remove_punctuation,
        remove_pos=remove_pos,
        remove_stopwords=remove_stopwords,
        extra_stopwords=extra_stopwords,
        remove_email=remove_email,
        remove_url=remove_url,
        lemmatize=lemmatize,
    )
    console.print(f"{clean_texts}")


if __name__ == "__main__":
    app()
