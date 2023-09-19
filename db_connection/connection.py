# Database connection script
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Adjust the database URI as needed
engine = create_engine('sqlite:///event_app.db')
Session = sessionmaker(bind=engine)
