import uuid
from abc import ABC, abstractmethod


class Tag(ABC):

    @abstractmethod
    def generate_tag_content(self):
        pass

    def __str__(self):
        return f"<GITOPTIM {self.generate_tag_content()}>"

    def __repr__(self):
        return str(self)


class StartTag(Tag):

    def generate_tag_content(self):
        return "START"


class EndTag(Tag):

    def generate_tag_content(self):
        return "END"


class UniqueTag(Tag):
    id: str

    def __init__(self):
        self.id = str(uuid.uuid4())

    def generate_tag_content(self):
        return f"UNIQUE {self.id}"
