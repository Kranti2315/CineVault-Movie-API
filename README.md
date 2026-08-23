CineVault – Movie Management REST API
A beginner-friendly Movie Management REST API built with Python, Flask, and MySQL.

This project allows a client/frontend application to communicate with a backend API and retrieve movie data from a MySQL database. It also includes a simple logging system to record application events.

Features:
*Get all movies from the database
*MySQL database connectivity
*Flask REST API
*Application logging
*Organized backend project structure
*JSON API responses
*Easy to test using a browser, Postman, or a frontend application

Technologies Used: 
*Python
*Flask
*MySQL
*MySQL Connector
*REST API
*JSON
*Python Logging
*VS Code
*Git & GitHub

Project Structure:
Backend/
│
├── Logs/
│   └── app.log
│
├── app.py
├── database.py
├── logger.py
├── Movie_Manager.py
├── requirements.txt
├── .gitignore
└── README.md
app.log is a generated log file. For a public GitHub repository, it is recommended not to commit continuously generated log files.

Setup
1. Clone the repository
git clone YOUR_GITHUB_REPOSITORY_URL
cd Backend
2. Create a virtual environment
python -m venv venv
Activate it on Windows:

venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
4. Configure MySQL
Create your MySQL database and movies table.

Update the database configuration in your project using environment variables or your local configuration file.

Never upload real database passwords or credentials to GitHub.

5. Run the application
python app.py
The Flask server should start locally, for example:

http://127.0.0.1:5000
API Endpoint
Get All Movies
GET

/movies
Example:

http://127.0.0.1:5000/movies
The endpoint retrieves movie records from MySQL and returns them as JSON.

Logging
The project uses Python's logging module.

Example:

logger.info("Movies fetched")
The application automatically writes log messages when the relevant code executes.

The application should be started with:

python app.py
You do not need to run logger.py separately.

Example Response
[
    {
        "id": 1,
        "title": "Example Movie"
    }
]
The exact response depends on the columns in your MySQL movies table.

Security Notes:
*Before pushing this project to GitHub:
*Do not upload database passwords.
*Do not upload API keys.
*Do not upload .env files containing secrets.
*Do not upload your venv folder.
*Do not upload __pycache__.
*Avoid committing generated log files containing sensitive information.
*Use .gitignore to keep private/generated files out of the repository.

Running from VS Code: 
Open the project folder in VS Code, open the integrated terminal, activate your virtual environment, and run:

python app.py
Then test the API using your browser or Postman.

Future Improvements:
*Add movie POST, PUT, and DELETE endpoints
*Add user authentication
*Add input validation
*Add search and filtering
*Add pagination
*Add a frontend
*Add automated tests
*Add production deployment

Author:
**Kranti Lohar**

Built as a Python/Flask backend project for learning REST APIs, MySQL integration, and application logging.

