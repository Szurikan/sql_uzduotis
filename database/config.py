from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,DeclarativeBase

class Base(DeclarativeBase):
    pass

engine = create_engine("mysql://Szurikan:ranek@localhost/darbuotoju_projektas", pool_pre_ping=True, pool_recycle=3600)

# def initialize_database():
#     Base.metadata.create_all(engine)

session_maker = sessionmaker(engine)

# initialize_database()