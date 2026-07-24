from sqlmodel import create_engine, SQLModel, Session
from dotenv import load_dotenv
import os

load_dotenv()
 
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(
    DATABASE_URL,
    echo = True # Prints SQL query in terminal, before deployment we change it to False
)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session  
        # Everything before yield is startup code and everything after is shutdown code. Yield pauses a function when it reaches there and then APIs are called, after application shutsdown , the function returns after yield