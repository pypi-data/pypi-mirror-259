"""Context class."""
from requests import Session


class Context:
    def __init__(self) -> None:
        self.session = Session()
