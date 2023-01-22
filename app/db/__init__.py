from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

# connect to database using env variable
# engine manages overall connection to database
engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0)
# generates temp connections for CRUD operations
Session = sessionmaker(bind=engine)
# map models to real MYSQL tables
Base = declarative_base()