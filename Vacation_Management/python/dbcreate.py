from model import db

db.create_all()

# db.session.add(admin)
db.session.commit()
