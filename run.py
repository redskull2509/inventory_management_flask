from app import app
from db import  db

#Create all tables before first request
@app.before_first_request
def create_tables():
    db.create_all()

db.init_app(app)