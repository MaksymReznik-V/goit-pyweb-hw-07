from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


engine = create_engine('postgresql+psycopg2://postgres:12345678@localhost:5432/postgres')

Base = declarative_base()

Session = sessionmaker(bind=engine)

