# SHS Enrollment System

A professional desktop-based Senior High School Enrollment System developed with **Python, PyQt5, and SQLite**.

## Overview

The system manages SHS enrollment through a modern desktop interface. It provides student registration, validation, track-and-strand selection, SQLite storage, student record search, editing and deletion, and practical enrollment settings.

## Features

- Modern desktop GUI
- Student enrollment
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
SHS_Enrollment_System/
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
| `database.py` | SQLite tables and CRUD/settings operations |
| `enrollment.py` | Enrollment rules and validation |
| `gui.py` | PyQt5 interface and user interaction |

## Database

The application creates `shs_enrollment.db` automatically. It contains `students` and `settings` tables. The database file is excluded from GitHub through `.gitignore` so local student data is not published.

## Installation

1. Open the project in PyCharm.
2. Create or select a Python interpreter/virtual environment.
3. Install the dependency:

```text
pip install -r requirements.txt
```

SQLite is included with Python and does not require a separate installation.

## Run

In PyCharm, open `main.py`, right-click, and select **Run 'main'**.

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

The Settings page provides real system configuration:

- School Name
- School Year
- Enrollment Status

When enrollment is set to **CLOSED**, new enrollment records are blocked while existing records remain available.

## Public GitHub Safety

Do not publish real student names, addresses, contact numbers, passwords, credentials, or other private information. The local SQLite database is intentionally ignored by Git.

## Future Improvements

- Administrator authentication
- Password hashing
- Backup and restore
- Printable enrollment forms
- CSV/Excel export
- Role-based access
- Audit logs

## License

For educational and academic use.
