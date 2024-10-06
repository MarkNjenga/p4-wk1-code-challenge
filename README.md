# Superheroes Management System
## Overview
The Superheroes Management System is a Flask-based web application that provides an API for managing superheroes, their powers, and relationships between them. The system allows users to create, retrieve, update, and delete heroes and powers while maintaining relationships through a hero powers table.

## Features
- Hero Management: Create, read, update, and delete superheroes.
- Power Management: Create, read, update, and delete superhero powers.
- Hero-Power Relationships: Establish relationships between heroes and their powers.
- Input Validation: Ensure data integrity with validation checks on inputs.

## Tech Stack
- Flask 
- SQLite
- Python

## Installation
## Requirements
- *Python 3.8 or higher*
- *Flask*
- *SQLAlchemy*
- *Faker*

## Steps to Install
1. Clone the repository:
- *Use git clone to copy the repository to your local machine*.
2. Navigate to the project directory:
- *Change into the project directory using cd*.
3. Create a virtual environment:
- *Use pipenv*.
4. Activate the virtual environment:
- *pipenv shell*

## Install the required packages:
*Use pipenv install -r requirements.txt to install all dependencies*.
## Configuration
## Environment Variables
Set the following environment variables as needed:
- FLASK_APP: Name of your main Flask application file (e.g., app.py).
- FLASK_ENV: Set to development for development mode.
## Database Configuration
The application uses SQLite for simplicity. The database will be created automatically upon the first run of the application.
## Usage
- Start the Flask application:
- Run the command flask run in your terminal.

Access the API:
The API is accessible at http://localhost:5000.
API Endpoints
1. Heroes:
GET /heroes: Retrieve a list of all superheroes.
GET /heroes/<int:id>: Retrieve a superhero by their ID.
POST /heroes: Create a new superhero.
PATCH /heroes/<int:id>: Update an existing superhero by their ID.
DELETE /heroes/<int:id>: Delete a superhero by their ID.

2. Powers:
GET /powers: Retrieve a list of all powers.
GET /powers/<int:id>: Retrieve a power by its ID.
POST /powers: Create a new power.
PATCH /powers/<int:id>: Update an existing power by its ID.
DELETE /powers/<int:id>: Delete a power by its ID.

3. Hero Powers:
POST /hero_powers: Create a relationship between a hero and a power.
Testing
To run the test suite, execute the following command:

Use pytest to run all tests. This will execute the tests defined in the app_test.py file and check the functionality of the API endpoints.
## Author
This program was written by [MarkWanjiku]
## Contributing
Contributions are welcome! If you have suggestions for improvements or find a bug, feel free to open an issue or submit a pull request.