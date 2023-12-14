from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
db = SQLAlchemy(app)

from datetime import datetime
from typing import Self
from app import db

class Note(db.Model):  # Создание модели для таблицы Zam в базе данных
    id = db.Column(db.Integer, primary_key=True) 
    nazvan= db.Column(db.String(50))  # Определение столбца заметка (строка, уникальное значение)
    sod = db.Column(db.String(300))  # Определение столбца заметка (строка, уникальное значение)
    date = db.Column(db.String(50))  # Определение столбца дата

    def __init__(self, nazvan, sod, date):  # Метод для инициализации экземпляра класса Note
        self.avtor = nazvan  # Присвоение значения заметка
        self.sod = sod # Присвоение значения дата
        self.date = date # Присвоение значения дата
        
with app.app_context():  # Вход в контекст приложения
    db.create_all()    
    note = Note.query.all()  # Получение всех пользователей
    db.session.close()  # Закрытие сессии

    for note in note: #вывод пользователей
        print(f"{note.nazvan}, {note.sod},{note.date}")  

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save', methods=['POST'])
def save():
    name=request.form['nazvan'] # Эту и последующие переменные берём из формы
    text=request.form['sod']
    date=request.form['date']
    notes=Note(name,text,date) 
    db.session.add(notes) #Добавляем  в базу данных
    db.session.commit()
    return render_template('index.html', message='Заметка успешно сохранена')

@app.route('/notes') # Определение маршрута для URL /zametkas/
def notes(): # Определение функции для обработки запроса к URL /zametkas/
    notes = Note.query.all() #Получение всех записей из таблицы (класса) Zametka
    return render_template('notes.html', notes=notes) #передача списка пользователе

if __name__ == "__main__":
    app.run(debug=True)






