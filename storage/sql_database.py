from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from storage.models import Base, ScrapedContent

from config import settings

# Create an engine using the connection string from settings
engine = create_engine(settings.SETTINGS["database"]["connection_string"], echo=False)
Session = sessionmaker(bind=engine)
session = Session()

def init_db():
    """Creates database tables based on the defined models."""
    Base.metadata.create_all(engine)

def save_data(data):
    """Saves a single data record to the database."""
    # Assuming data is a dictionary with keys matching our model
    record = ScrapedContent(**data)
    session.add(record)
    session.commit()