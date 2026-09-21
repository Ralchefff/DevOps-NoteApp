from flask import Flask, render_template, request, redirect
import sqlite3


app = Flask(__name__)

def get_db_connection():
	conn = sqlite3.connect("notes.db")
	conn.row_factory = sqlite3.Row
	return conn

@app.route("/api/notes")
def get_notes():
	conn = get_db_connection()
	notes = conn.execute("SELECT * FROM notes").fetchall()
	conn.close()
	return [dict(note) for note in notes]
@app.route("/add", methods=["POST"])
def add_note():
	title =  request.form["title"]
	content = request.form["content"]
	conn = get_db_connection()
	conn.execute("INSERT INTO notes (title, content) VALUES (?, ?)",
	(title, content))
	conn.commit()
	conn.close()
	return redirect("/")

@app.route("/")
def home():

	return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
