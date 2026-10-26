
import pytest
from app import app, get_db_connection


@pytest.fixture
def client(monkeypatch):
    # Използваме отделна тестова MariaDB база.
    monkeypatch.setenv("DB_HOST", "localhost")
    monkeypatch.setenv("DB_USER", "notetester")
    monkeypatch.setenv("DB_PASSWORD", "111")
    monkeypatch.setenv("DB_NAME", "testing")

    app.config["TESTING"] = True

    
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM notes")
        conn.commit()
    finally:
        conn.close()

    with app.test_client() as test_client:
        yield test_client


def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200


def test_get_notes(client):
    response = client.get("/api/notes")

    assert response.status_code == 200
    


def test_adding_notes(client):
    title = "1"
    content = "2"

    response = client.post(
        "/add",
        data={
            "title": title,
            "content": content
        }
    )

    assert response.status_code == 302

    # Проверяваме дали бележката е записана.
    notes_response = client.get("/api/notes")
    assert notes_response.status_code == 200

    notes = notes_response.get_json()

    assert any(
        note["title"] == title
        and note["description"] == content
        for note in notes
    )


def test_delete_note(client):
    title = "2"
    content = "3"

    # Първо добавяме бележката.
    client.post(
        "/add",
        data={
            "title": title,
            "content": content
        }
    )

  
    notes = client.get("/api/notes").get_json()

    note = next(
        (
            item for item in notes
            if item["title"] == title
            and item["description"] == content
        ),
        None
    )

    assert note is not None

    
    response = client.delete(
        f"/api/notes/{note['id']}"
    )

    assert response.status_code == 200
    assert response.get_json() == {"success": True}

    
    notes_after = client.get("/api/notes").get_json()

    assert all(
        item["id"] != note["id"]
        for item in notes_after
    )
