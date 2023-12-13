from datetime import datetime
from typing import Self
from app import db
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    content = db.Column(db.Text)
    created_at = db.Column(db.Date, default=datetime.utcnow)
    
    def _init_(self,title,content, created_at):
        self.title=title
        self.content=content
        self.created_at=created_at    
with app.app_context():
    db.create_all()
    db.session.add()
    db.session.commit()
    db.session.close()

