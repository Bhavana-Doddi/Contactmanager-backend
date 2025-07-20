from main import app

with app.app_context():
    from main import db
    db.create_all()
