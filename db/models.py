import datetime

from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))


class Note(Base):  # Создание модели для таблицы Zam в базе данных
    __tablename__ = "notes"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    # Определение столбца заметка (строка, уникальное значение)
    # TODO: А тут точно должно быть уникальное значение? Потому что имена авторов могут повторятся
    autor: Mapped[str] = mapped_column(String(50), unique=False, nullable=True)
    # Тот кто написал эту заметку
    user_id: Mapped[int] = mapped_column(Integer, unique=True, nullable=False)
    # Определение столбца заметка (строка, уникальное значение)
    note: Mapped[str] = mapped_column(String(300), unique=True, nullable=False)
    date: Mapped[datetime.datetime] = mapped_column(String(300), unique=False, nullable=True)  # Определение столбца дата

    # def __init__(
    #     self, nazvan, sod, date
    # ):  # Метод для инициализации экземпляра класса Note
    #     self.avtor = nazvan  # Присвоение значения заметка
    #     self.sod = sod  # Присвоение значения дата
    #     self.date = date  # Присвоение значения дата
