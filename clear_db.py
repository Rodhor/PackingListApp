from config import db, app
from models import Items

with app.app_context():
    # Drop all tables
    db.drop_all()

    # Recreate all tables
    db.create_all()

    print("Database has been cleared.")
