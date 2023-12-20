import pathlib


class MarkdownParser:
    def parse(self, path: pathlib.Path) -> str:
        file = open(path)
        return file.read()