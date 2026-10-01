# Project Development Process

This file documents the development process of my initial DevOps project.

### Initial Setup

* Created a Linux CentOS virtual machine and enabled SSH.
* Connected to the VM remotely from my local environment using PuTTY.
* Created the project directory.
* Installed Python, Git, and UFW.
* Installed Pip and Flask.
* Created a Python virtual environment (`venv`).

### Application

* Created a basic `app.py` Flask application to test the initial setup.
* Configured the application so it can be started using Python.
* Created a database to store notes.
* Connected the database to `app.py`.
* Added `POST` functionality to `/api/notes` for creating new notes.
* Added `GET` functionality to `/api/notes` for retrieving stored notes.
* Created `app.js` to manipulate the DOM and fetch notes from the API.
* Added functionality to display notes retrieved from the database.
* Added functionality to delete notes through the API.

### Next Steps

* Add note editing functionality.
* Containerize the application using Docker.
* Create a Docker Compose setup.
* Implement CI/CD with GitHub Actions.
* Deploy the application to a cloud VM.
* Add monitoring and logging.
