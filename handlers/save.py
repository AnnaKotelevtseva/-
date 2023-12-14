import datetime

from db.models import Note
from sqlalchemy import Engine
from sqlalchemy.orm import Session


def save_notes(name: str, text: str, date: datetime.datetime, user_id: int, engine: Engine):
    with Session(engine) as session:
        n = Note(author=name, user_id=user_id, note=text, date=date)
        session.add(n)
        session.commit()

