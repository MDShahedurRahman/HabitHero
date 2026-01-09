# HabitHero

HabitHero is a small Python command-line habit tracker built using multiple packages and classes.
It allows users to track daily habits, maintain streaks, view weekly activity, and persist data locally using JSON.

This project is intentionally lightweight and focuses on clean architecture, object-oriented design,
testable core logic, and professional GitHub workflow.

---

## Features

- Add and list habits
- Mark habits as done for today
- Automatic streak calculation
- Weekly activity summary across all habits
- Local JSON-based persistence
- Unit tests with pytest

---

## Requirements

- Python 3.9 or higher

---

## Setup

Clone the repository and navigate to the project directory:

```bash
git clone <your-repo-url>
cd HabitHero
```

Create and activate a virtual environment:

### macOS / Linux
```bash
python -m venv .venv
source .venv/bin/activate
```

### Windows (PowerShell)
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Upgrade pip and install dependencies:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

---

## Run the Application

```bash
python main.py
```

Use the interactive menu to manage habits and track progress.

---

## Run Tests

Always run tests using the active Python interpreter:

```bash
python -m pytest -q
```

---

## How Streaks Work

- A streak represents consecutive days a habit is completed
- Missing a day resets the streak to zero
- Streaks are calculated dynamically based on stored completion dates

---

## Weekly Activity

The weekly activity view shows how many habits were completed each day over the last seven days.
This provides a quick overview of overall consistency.

---

## Data Storage

Habit data is stored locally at:

```
~/.habithero/db.json
```

This file is created automatically and updated whenever habits are added or marked as done.

---

## Project Structure

```
HabitHero/
├── habithero/
│   ├── cli/
│   │   └── app.py
│   ├── core/
│   │   ├── models.py
│   │   └── tracker.py
│   ├── storage/
│   │   └── json_store.py
│   └── __init__.py
├── tests/
│   ├── conftest.py
│   ├── test_tracker.py
│   └── test_store.py
├── main.py
├── requirements.txt
└── README.md
```

---

## Changelog

### v1.0.0
- Initial release of HabitHero
- Added habit creation and completion tracking
- Implemented streak calculation logic
- Added weekly activity summary
- Persisted data using local JSON storage
- Added unit tests for core logic and storage
- Structured project using multiple packages and classes

---

## License

This project is licensed under the MIT License.
