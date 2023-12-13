from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
db = SQLAlchemy(app)

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

@app.route('/view')
def view():
    return render_template('view.html')
if __name__ == "__main__":
    app.run(debug=True)
