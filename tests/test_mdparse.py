import pathlib
from bookwires.md_parser import MarkdownParser
import pytest
def test_parse_md_nofound():
    parser = MarkdownParser()
    with pytest.raises(FileNotFoundError):
        parser.parse(pathlib.Path('notfound.txt'))


def test_parse_found(samples_path: pathlib.Path):
    filepath = samples_path / 'NICE_DOCS.md'
    result = MarkdownParser().parse(filepath)

    assert result
    assert result == '# Nice documentation\nA nice view on documentation.'