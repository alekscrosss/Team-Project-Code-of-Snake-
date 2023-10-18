Below is an instructional guide for using the commands in your code:

1.Add a Contact:
   - Command: `add [name] [phone] [birthday] [email]`
   - Example: `add John Doe +123456789 01.01.90 john.doe@example.com`
   - Description: Adds a new contact with an optional phone number, birthday, and email.

2.Show All Contacts:
   - Command: `show all`
   - Example: `show all`
   - Description: Displays all contacts with their phones, email, and birthday information.

3.Find Contacts:
   - Command: `find [query]`
   - Example: `find John`
   - Description: Displays contacts that match the provided query.

4.Delete a Contact:
   - Command: `delete [name]`
   - Example: `delete John Doe`
   - Description: Deletes a contact by name.

5.Change Contact Information:
   - Command: `change [name] [phone/birthday/email] [new_value]`
   - Example: `change John Doe phone +987654321`
   - Description: Changes the phone, birthday, or email of a contact.

6.Phone Information:
   - Command: `phone [name]`
   - Example: `phone John Doe`
   - Description: Displays the phone number for a specific contact.

7.Email Information:
   - Command: `email [name]`
   - Example: `email John Doe`
   - Description: Displays the email address for a specific contact.

8.Upcoming Birthdays:
   - Command: `celebration in [days]`
   - Example: `celebration in 7`
   - Description: Shows upcoming birthdays in the next [days] days.

9.Notebook Interface:
   - Command: `notebook`
   - Example: `notebook`
   - Description: Opens the notebook interface for additional functionality.
	9.1 You will see the notebook interface prompting you to choose one of the options.

		* Adding a new note (command `add`):

		- Type 	add and press Enter.
		- Enter the title of the note.
		- Enter the text of the note.
		- Enter tags for the note, separated by commas. If you don't want to add tags, simply press Enter.

		* Editing an existing note (command `edit`):

		- Type edit and press Enter.
		- You will see a list of all notes. Select the index of the note you want to edit and enter it.
		- Enter a new title or simply press Enter to keep the current one.
		- Enter new text or simply press Enter to keep the current one.
		- Enter new tags, separated by commas, or simply press Enter to keep the current tags.
		
		* Deleting a note (command `delete`):

		- Type `delete` and press Enter.
		- You will see a list of all notes. Select the index of the note you want to delete and enter it.

		* Searching notes (command `search`):

		- Type `search` and press Enter.
		- Enter a keyword to search for. The program will show all notes containing this word in the title, text, or tags.

		* Listing all notes (command `list`):

		- Type list and press Enter. You will see a list of all notes.

		* Clearing all notes (command `clear`):

		- Type clear and press Enter. All notes will be deleted.

		* Viewing all tags (command `tags`):

		- Type `tags` and press Enter. You will see a list of all unique tags from the notes.

  		* Exiting the program (command `exit`):

		- Type `exit` and press Enter to return main menu.
		
		**Note: After each command (except list, search, and tags), your notebook is automatically saved to the file notes.pkl, so all your changes are preserved between sessions.

10.Clean Folder Interface:
    - Command: `clean`
    - Example: `clean`
    - Description: Opens the sorter for cleaning folders. Enter the path to the folder you want to sort. If you need to unpack archives, enter 'yes'. If not, enter 'no

11.Display Available Commands:
    - Command: `helper`
    - Example: `helper`
    - Description: Displays available commands and their descriptions.

12.Exit the Program:
    - Command: `goodbye`, `close`, or `exit`
    - Example: `exit`
    - Description: Saves the address book to a file and exits the program.
