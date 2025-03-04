from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text

Base = declarative_base()


class ScrapedContent(Base):
    """
    Data model for storing scraped content.
    """
    __tablename__ = 'scraped_content'
    id = Column(Integer, primary_key=True)
    source = Column(String(50))
    title = Column(String(255), nullable=True)
    content = Column(Text, nullable=False)

    def __init__(self, content, source="unknown", title=None):
        self.content = content
        self.source = source
        self.title = title
