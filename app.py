from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///zam.db'
db = SQLAlchemy(app)

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




