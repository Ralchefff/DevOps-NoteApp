console.log("JavaScript is working!");

fetch("/api/notes")
    .then(response => response.json())
    .then(notes => {

        const container = document.getElementById("notescontainer");

        notes.forEach(note => {

            const noteElement = document.createElement("div");

            noteElement.innerHTML = `
                <h3>${note.title}</h3>
                <p>${note.content}</p>
            `;

            container.appendChild(noteElement);
        });
    });
