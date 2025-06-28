from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

# faqat echo=False bo‘lishi kerak — loglar chiqmasin
engine = create_engine("sqlite:///users.db", echo=False)

Session = sessionmaker(bind=engine)
session = Session()
