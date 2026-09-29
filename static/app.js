
fetch("/api/notes")
    .then(response => response.json())
    .then(notes => {

        const container = document.getElementById("notescontainer");

        notes.forEach(note => {

            const noteElement = document.createElement("div");
            noteElement.className = "note";

            noteElement.innerHTML = `
                <h3>${note.title}</h3>
                <p>${note.content}</p>
                <button class="delete-button">Delete</button>
            `;

            const delbutton = noteElement.querySelector(".delete-button");

            delbutton.addEventListener("click", () => {

                fetch(`/api/notes/${note.id}`, {
                    method: "DELETE"
                })
                .then(response => {

                    if (!response.ok) {
                        throw new Error("Failed to delete note");
                    }

                    return response.json();
                })
                .then(data => {

                    console.log(data);
                    noteElement.remove();

                })
                .catch(error => {
                    console.error(error);
                });

            });

            container.appendChild(noteElement);
        });
    });
