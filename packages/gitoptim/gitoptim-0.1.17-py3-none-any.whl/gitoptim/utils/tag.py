import uuid
from abc import ABC, abstractmethod
from typing import ClassVar


class Tag(ABC):

    @abstractmethod
    def generate_tag_content(self):
        pass

    def __str__(self):
        return f"<GITOPTIM {self.generate_tag_content()}>"

    def __repr__(self):
        return str(self)


class StartTag(Tag):
    id: ClassVar[str] = str(uuid.uuid4())

    def generate_tag_content(self):
        return f"START {self.id}"


class EndTag(Tag):
    id: ClassVar[str] = str(uuid.uuid4())

    def generate_tag_content(self):
        return f"END {self.id}"


class SectionTag(Tag):
    def generate_tag_content(self):
        return "SECTION"
