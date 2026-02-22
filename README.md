
⚾ Baseball Team Manager (Python OOP Project)

📌 Project Overview

This project is a **Baseball Team Manager console application** developed in Python.
It allows users to manage a baseball team lineup by adding, editing, moving, and removing players while saving data permanently in a CSV file.

The project was completed as part of a **Python Programming II (CPRO 2201) midterm project** and demonstrates:

* Object-Oriented Programming (OOP)
* File handling using CSV
* Modular program design (UI, objects, database layers)
* Input validation and data persistence

---

🧱 Project Structure

```
project folder/
│
├── main.py        → Main program (control flow)
├── objects.py     → Player & Lineup classes
├── db.py          → File/data access layer
├── ui.py          → User interface display functions
├── players.csv    → Persistent player data
└── README.md
```

---

⚙️ Features

👥 Player Management

* Add new players (first name, last name, position, stats)
* Remove players
* Move players within the lineup
* Edit player position
* Edit batting statistics (at-bats and hits)

📊 Statistics

* Automatic batting average calculation
* Always displayed to 3 decimal places
* Validation:

  * Hits cannot exceed at-bats
  * No negative values allowed

📅 Game Date Feature

* Optional game date entry
* Current date always displayed
* Days until game shown only if the date is in the future

💾 Data Persistence

* Player data saved in `players.csv`
* Supports:

  * Old format (single name field)
  * New format (first + last name)

---

🧑‍💻 Technologies Used

* Python 3
* Object-Oriented Programming
* File I/O (CSV text format)
* Git & GitHub for version control

---

▶️ How to Run

1. Open terminal or PowerShell in the project folder.
2. Run:

```bash
python main.py
```

3. Follow the menu prompts.

---

🧪 Testing Notes

You can test the game date feature:

* Press **Enter** → Skip game date
* Enter future date → Shows days until game
* Enter past date → Shows date only (no days)

---

🎯 Learning Outcomes

This project demonstrates:

* OOP design with classes and methods
* Separation of concerns (UI, logic, data layers)
* Data validation techniques
* Git commit tracking during development

---

👤 Author

**Akosua Otu**
Python Programming II 

