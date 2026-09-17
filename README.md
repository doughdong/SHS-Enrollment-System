# SHS Enrollment System

A professional desktop-based Senior High School Enrollment System developed as a **college academic project** using **Python, PyQt5, and SQLite**.

## Overview

The **SHS Enrollment System** is a desktop application designed to manage the enrollment information of Senior High School students. It provides a structured interface for registering students, validating enrollment information, selecting grade levels, tracks, and strands, and managing stored student records.

The project demonstrates practical programming concepts including graphical user interface development, input validation, CRUD operations, SQLite database management, and data persistence.

## Features

- Modern desktop GUI
- Student enrollment
- Student information management
- Input validation
- Grade 11 and Grade 12
- Academic and TVL tracks
- Track-dependent strand selection
- SQLite database storage
- Search student records
- Edit and delete records
- Enrollment status: OPEN / CLOSED
- School year settings
- Automatic database initialization
- Exit confirmation

## Tracks and Strands

### Academic

- STEM
- ABM
- HUMSS
- GAS

### TVL

- ICT - Programming
- ICT - CSS

## Technology Stack

- Python 3
- PyQt5
- SQLite
- PyCharm
- Git / GitHub

## Project Structure

```text
SHS-Enrollment-System/
├── main.py
├── database.py
├── enrollment.py
├── gui.py
├── requirements.txt
├── .gitignore
├── README.md
└── docs/
    ├── PROJECT_DOCUMENTATION.md
    └── USER_GUIDE.md
```

## Module Responsibilities

| Module | Responsibility |
|---|---|
| `main.py` | Starts the application and initializes the database |
| `database.py` | Handles SQLite database operations and CRUD functionality |
| `enrollment.py` | Handles enrollment rules and input validation |
| `gui.py` | Provides the PyQt5 interface and user interaction |

## Database

The application uses **SQLite** for local data storage. The database is initialized automatically when the application starts.

Student information is stored locally, allowing enrollment records to remain available between application sessions. The database file is excluded from GitHub through `.gitignore` so that local student data is not accidentally published.

## Installation

1. Clone or download the repository.
2. Open the project in **PyCharm** or another Python IDE.
3. Create or select a Python interpreter/virtual environment.
4. Install the required dependency:

```bash
pip install -r requirements.txt
```

SQLite is included with Python and does not require a separate installation.

## Run

In PyCharm:

1. Open `main.py`.
2. Right-click the file.
3. Select **Run 'main'**.

The application will initialize the local database and open the enrollment interface.

## Enrollment Workflow

```text
Dashboard
   ↓
Enroll Student
   ↓
Student Information
   ↓
Grade Level
   ↓
Track
   ↓
Strand
   ↓
Validation
   ↓
Enrollment Status Check
   ↓
SQLite Storage
   ↓
Enrollment Successful
```

## Settings

The system includes enrollment-related settings such as:

- School Name
- School Year
- Enrollment Status

When enrollment is set to **CLOSED**, new enrollment records are blocked while existing records remain available.

## Academic Purpose

This project was developed as part of a **college academic/software development project**. The application is intended to demonstrate the practical use of programming concepts by applying them to a Senior High School enrollment scenario.

The project focuses on:

- Python programming
- PyQt5 GUI development
- Form validation
- CRUD operations
- SQLite database management
- Data persistence
- Basic software organization

## Public GitHub Safety

This repository is public and intended for academic/project demonstration.

Do **not** publish real student:

- Names
- Addresses
- Contact numbers
- Passwords
- Credentials
- Identification numbers
- Other private or sensitive information

The local SQLite database is intentionally excluded from GitHub through `.gitignore`.

## Future Improvements

Possible future improvements include:

- Administrator authentication
- Password hashing
- Backup and restore
- Printable enrollment forms
- CSV/Excel export
- Role-based access
- Audit logs
- Improved reporting features

## License

For **educational and academic use**.

## Author

Developed as a college academic project.
