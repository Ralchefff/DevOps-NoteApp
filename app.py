from flask import Flask, render_template, request, redirect
import pymysql
import os 


app = Flask(__name__)

def get_db_connection():
	
		return pymysql.connect(
			host=os.environ["DB_HOST"],
			user=os.environ["DB_USER"],
			password=os.environ["DB_PASSWORD"],
			database=os.environ["DB_NAME"],
			cursorclass=pymysql.cursors.DictCursor,
			autocommit=False
		)
	
	
@app.route("/api/notes")
def get_notes():
    conn = get_db_connection()

    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM notes")
            notes = cursor.fetchall()
    finally:
        conn.close()

    return notes
@app.route("/add", methods=["POST"])
def add_note():
    title = request.form["title"]
    content = request.form["content"]

    conn = get_db_connection()

    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO notes (title, description) VALUES (%s, %s)",
                (title, content)
            )
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

    return redirect("/")

	
@app.route("/api/notes/<int:note_id>", methods=["DELETE"])
def delete_note(note_id):
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "DELETE FROM notes WHERE id = %s",
                (note_id,)
            )
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

    return {"success": True}


@app.route("/")
def home():

	return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
