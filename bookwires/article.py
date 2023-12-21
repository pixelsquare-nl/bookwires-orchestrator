
from datetime import datetime
from pathlib import Path

from dataclasses import dataclass

@dataclass
class Article:
    title: str
    description: str
    markdown_path: Path
    publishing_date: datetime = datetime.now()