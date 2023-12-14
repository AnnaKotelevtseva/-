from db.models import Note
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy import Engine


def get_notes(user_id: int, engine: Engine) -> list:
    n = select(Note).where(Note.user_id == user_id)  # Получение данны
    session = Session(engine)
    list_note = []
    for note in session.scalars(n):
        list_note.append(note)
    return list_note
