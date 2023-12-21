import pathlib
from typing import Optional, Self
from .article import Article

class Orchestrator:
    mds: list[Article] = []
    
    def add(self: Self, article: Article):
        print(article)
        
    def add_with_autotitle(self: Self, markdown_path: pathlib.Path, description: Optional[str] = None):
        ...