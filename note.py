import datetime
import pickle
class Note:
    def __init__(self, title, text):
        self.title = title
        self.text = text
        self.created_at = datetime.datetime.now()

    def __repr__(self):
        date_str = self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        return f'[{date_str}] {self.title} - {self.text}'

class Notebook:
    def __init__(self):
        self.notes = []

    def add(self, title, text):
        note = Note(title, text)
        self.notes.append(note)

    def delete(self, index):
        if 0 <= index < len(self.notes):
            del self.notes[index]
        else:
            print("Invalid note index!")

    def list_notes(self):
        for index, note in enumerate(self.notes):
            print(f"{index}. {note}")

    def clear_all(self):
        self.notes = []

    def edit(self, index, new_title=None, new_text=None):
        try:
            note = self.notes[index]
            if new_title:
                note.title = new_title
            if new_text:
                note.text = new_text
            return True
        except IndexError:
            return False

    def save_to_file(self, filename="notes.pkl"):
        with open(filename, 'wb') as file:
            pickle.dump(self.notes, file)

    def load_from_file(self, filename="notes.pkl"):
        try:
            with open(filename, 'rb') as file:
                self.notes = pickle.load(file)
        except FileNotFoundError:
            pass

def input_with_retry(prompt, validation_func=None, error_message="Invalid input!"):
    while True:
        data = input(prompt)
        if validation_func is None or validation_func(data):
            return data
        print(error_message)

def notebook_interface():
    notebook = Notebook()
    notebook.load_from_file()
    while True:
        command = input_with_retry(
            "\nChoose an option in notes ('add', 'delete', 'edit', 'list', 'clear', 'exit'): ",
            lambda x: x in ['add', 'delete', 'edit', 'list', 'clear', 'exit']
        ).strip().lower()

        if command == 'add':
            title = input_with_retry("Enter note title: ", lambda x: x != "")
            text = input_with_retry("Enter note text: ", lambda x: x != "")
            notebook.add(title, text)
            notebook.save_to_file()

        elif command == 'edit':
            notebook.list_notes()
            index = input_with_retry(
                "Enter the index of the note you want to edit: ",
                lambda x: x.isdigit() and 0 <= int(x) < len(notebook.notes),
                "Please enter a valid index!"
            )
            index = int(index)

            new_title = input("Enter new title (leave blank to keep current): ")
            if not new_title:
                new_title = None

            new_text = input("Enter new text (leave blank to keep current): ")
            if not new_text:
                new_text = None

            if notebook.edit(index, new_title, new_text):
                print("Note updated successfully!")
            else:
                print("Invalid index!")
            notebook.save_to_file()

        elif command == 'delete':
            notebook.list_notes()
            index = input_with_retry(
                "Enter note index to delete: ",
                lambda x: x.isdigit() and 0 <= int(x) < len(notebook.notes),
                "Please enter a valid index!"
            )
            index = int(index)
            notebook.delete(index)
            notebook.save_to_file()

        elif command == 'list':
            notebook.list_notes()

        elif command == 'clear':
            notebook.clear_all()
            print("All notes have been cleared.")
            notebook.save_to_file()

        elif command == 'exit':
            break

if __name__ == '__main__':
    notebook_interface()
