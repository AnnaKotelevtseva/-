from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///zam.db'
db = SQLAlchemy(app)

from datetime import datetime
from typing import Self
from app import db
   
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/save', methods=['POST'])
def save():
    text = request.form['text']
    with open('notes.txt', 'a') as file:
        file.write(f'{text}')
        return render_template('index.html', message='Заметка успешно сохранена')
if __name__ == '__main__':
    app.run(debug=True)
    from flask import render_template

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        return redirect('/')
    return render_template('add.html')

if __name__ == "__main__":
    app.run(debug=True)


