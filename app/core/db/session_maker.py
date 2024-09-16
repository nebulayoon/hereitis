from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine()

SESSION_FACTORY = sessionmaker(engine)
