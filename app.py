from flask import Flask, render_template, request
from handlers.notes import get_notes
from handlers.save import save_notes
from sqlalchemy import create_engine
from datetime import datetime

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
engine = create_engine('sqlite:///notes.db', echo=True)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/save", methods=["POST"])
def save():
    name = request.form["nazvan"]
    text = request.form["sod"]
    date = request.form["date"]
    user_id = request.form["user_id"]
    save_notes(name, text, datetime.strptime(date, '%m/%d/%y %H:%M:%S'), int(user_id), engine)
    return render_template("index.html", message="Заметка успешно сохранена")


@app.route("/notes", methods=["GET"])  # Определение маршрута для URL /zametkas/
def notes():  # Определение функции для обработки запроса к URL /zametkas/
    user_id = request.form["user_id"]
    return render_template("notes.html", notes=get_notes(int(user_id), engine))  # передача списка пользователе


if __name__ == "__main__":
    app.run(debug=True)
