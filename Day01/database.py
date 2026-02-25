from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# This URL tells SQLAlchemy to connect to the 'db' service we defined in docker-compose
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/ai_journey")

from sqlalchemy import create_engine
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# This is our Table definition
class CalculationHistory(Base):
    __tablename__ = "history"
    id = Column(Integer, primary_key=True, index=True)
    type = Column(String) # e.g., "Prime" or "TwoSum"
    input_data = Column(String)
    result = Column(String)

# Create the table
Base.metadata.create_all(bind=engine)