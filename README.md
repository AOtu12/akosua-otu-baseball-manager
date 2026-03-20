 ⚾ Baseball Team Manager (Python OOP + SQLite + GUI Project)

 📌 Project Overview

This project is a **Baseball Team Manager application** developed in Python.
It started as a console-based system and was enhanced to include:

* Object-Oriented Programming (OOP)
* CSV file persistence (Sections 1–3)
* SQLite database integration (Section 4)
* Graphical User Interface (GUI) using Tkinter

The application allows users to manage a baseball team lineup, edit player data, and store information permanently.

This project was completed as part of the **Python Programming II (CPRO 2201) midterm/final project**.

---

🧱 Project Structure

```
project folder/
│
├── main.py            → Console application (Sections 1–3)
├── objects.py         → Player & Lineup classes (OOP)
├── db.py              → CSV file data layer
├── ui.py              → Console UI functions
│
├── db_sqlite.py       → SQLite database access layer
├── player_gui.py      → Tkinter GUI application
│
├── players.csv        → CSV data storage (Sections 1–3)
├── baseball.sqlite    → SQLite database (Section 4)
│
├── docs/              → Auto-generated documentation (pydoc)
└── README.md
```

---

⚙️ Features

👥 Player Management (Console Version)

* Add new players (first name, last name, position, stats)
* Remove players
* Move players within the lineup
* Edit player position
* Edit batting statistics (at-bats and hits)

---

 📊 Statistics

* Automatic batting average calculation
* Displayed to **3 decimal places**
* Validation rules:

  * Hits cannot exceed at-bats
  * No negative values allowed

---

 📅 Game Date Feature

* Optional game date entry
* Current date always displayed
* Days until game shown **only if the date is in the future**

---

 💾 Data Persistence (CSV – Sections 1–3)

* Data stored in `players.csv`
* Supports:

  * Old format (single name field)
  * New format (first + last name)

---

🗄️ Section 4 — Database Integration (SQLite)

* Replaced CSV storage with a **SQLite database**
* Database file: `baseball.sqlite`
* Table used:

```
Player(
    playerID INTEGER PRIMARY KEY,
    batOrder INTEGER NOT NULL,
    firstName TEXT NOT NULL,
    lastName TEXT NOT NULL,
    position TEXT NOT NULL,
    atBats INTEGER,
    hits INTEGER
)
```

---

 🧩 Enhancement — Position Table

An additional table was implemented:

```
Position(
    positionID INTEGER PRIMARY KEY,
    positionValue TEXT UNIQUE
)
```

* Stores valid positions (C, 1B, 2B, etc.)
* Used in GUI as a dropdown (Combobox)
* Improves data integrity and user input validation

---

🖥️ GUI Application (Tkinter)

The GUI allows users to manage player data easily.

 Features:

* 🔍 **Get Player**

  * Enter Player ID to retrieve player data
  * Displays data in editable fields
  * Shows error if player not found

* 💾 **Save Changes**

  * Updates:

    * First name
    * Last name
    * Position (dropdown)
    * At bats
    * Hits
  * Saves to database
  * Clears fields after saving

* ❌ **Cancel**

  * Restores original data (not just clearing)
  

* ⛔ **Batting order is NOT editable in GUI** (as required)

---

🧑‍💻 Technologies Used

* Python 3
* Object-Oriented Programming (OOP)
* SQLite (database)
* Tkinter (GUI)
* File I/O (CSV)
* Git & GitHub (version control)

---

 ▶️ How to Run

 Run Console Version (Sections 1–3)

```bash
python main.py
```

---

 Run GUI Version (Section 4)

```bash
python player_gui.py
```

---

 🧪 Testing Notes

 Game Date Testing

* Press **Enter** → skip date
* Future date → shows days remaining
* Past date → shows date only

 GUI Testing

* Enter valid Player ID → data loads
* Enter invalid ID → error + fields cleared
* Edit values → Save Changes updates DB
* Edit values → Cancel restores original data

---

🎯 Learning Outcomes

This project demonstrates:

* Object-Oriented Programming design
* Separation of concerns (UI, logic, data layers)
* File handling and database integration
* GUI development using Tkinter
* Data validation and persistence
* Incremental development using Git

---

 👤 Author

**Akosua Otu**
Python Programming II (CPRO 2201)
