A Python-based file management system that allows users to manage files (create, read, write, edit, and delete) through a simple command-line interface. This project demonstrates basic file handling operations and error handling in Python.

Features
Create Files: Allows users to create new files with error handling if the file already exists.
View Files: Lists all the files present in the current working directory.
Delete Files: Deletes a file if it exists, with proper error handling for missing files.
Write to Files: Enables users to write content into a file.
Read Files: Displays the content of a selected file.
Edit Files: Appends new content to an existing file.
Project Structure
main.py: Contains the main logic for file management, including file creation, deletion, viewing, reading, writing, and editing functions.
demo.py: A sample file reading functionality.
How to Run
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/file-management-system.git
cd file-management-system
Run the main script:

bash
Copy code
python main.py
Follow the command-line prompts to perform different file management operations.

Example Usage
text
Copy code
File management app
1: Create file
2: View all files
3: Delete file
4: Write file
5: Read file
6: Edit file
7: Exit
Create a file: Choose option 1 and enter the filename.
View files: Choose option 2 to see all files in the directory.
Delete a file: Choose option 3, then enter the filename to delete.
Write to a file: Choose option 4, then enter the filename and content.
Read a file: Choose option 5 to display the file content.
Edit a file: Choose option 6 to append new content to an existing file.
Technologies Used
Python: The core programming language for file handling and exception handling.
OS Module: To interact with the operating system for file and directory operations.
Contributions
Feel free to fork this project and submit pull requests if you want to contribute or improve the functionality.
