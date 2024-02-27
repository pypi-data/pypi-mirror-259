from abc import ABC, abstractmethod
from attrs import define
from typing import List
from datamaestro.record import Record, Item, recordtypes


class BaseRecord(Record):
    @classmethod
    def from_text(cls, text: str):
        return cls(SimpleTextItem(text))

    @classmethod
    def from_id(cls, id: str):
        return cls(IDItem(id))


class TopicRecord(BaseRecord):
    """Topic record"""


class DocumentRecord(BaseRecord):
    """Document record"""


@define()
class ScoredItem(Item):
    """A score associated with the document"""

    score: float
    """A retrieval score associated with this record (e.g. of the first-stage
    retriever)"""


class TextItem(Item, ABC):
    @abstractmethod
    def get_text(self) -> str:
        """Returns the text"""


@define
class SimpleTextItem(TextItem, ABC):
    """A topic/document with a text record"""

    text: str

    def get_text(self):
        return self.text


@define
class InternalIDItem(Item, ABC):
    """A topic/document with an internal ID"""

    id: int


@define
class IDItem(Item, ABC):
    """A topic/document with an external ID"""

    id: str


@define
class AdhocAssessment:
    doc_id: str


@define
class SimpleAdhocAssessment(AdhocAssessment):
    rel: float
    """Relevance (> 0 if relevant)"""


@define
class AdhocAssessedTopic:
    topic_id: str
    """The topic ID"""

    assessments: List[AdhocAssessment]
    """List of assessments for this topic"""


# --- Commonly used types


@recordtypes(IDItem)
class IDTopicRecord(TopicRecord):
    pass


@recordtypes(IDItem)
class IDDocumentRecord(DocumentRecord):
    pass


@recordtypes(SimpleTextItem)
class SimpleTextTopicRecord(TopicRecord):
    pass


@recordtypes(SimpleTextItem)
class SimpleTextDocumentRecord(DocumentRecord):
    pass


@recordtypes(IDItem, TextItem)
class GenericDocumentRecord(DocumentRecord):
    @classmethod
    def create(cls, id: str, text: str, *items: Item):
        return GenericDocumentRecord(IDItem(id), SimpleTextItem(text), *items)


@recordtypes(IDItem, TextItem)
class GenericTopicRecord(TopicRecord):
    @classmethod
    def create(cls, id: str, text: str, *items: Item):
        return GenericDocumentRecord(IDItem(id), SimpleTextItem(text), *items)
