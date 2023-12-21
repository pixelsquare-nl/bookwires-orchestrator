import pathlib
from bookwires.article import Article
from bookwires.orchestrator import Orchestrator


def test_orchestrate_add_md(samples_path: pathlib.Path):
    o = Orchestrator()
    o.add(Article(
        "A sample artifle", "A description of", samples_path / "NICE_DOCS.md" 
    ))