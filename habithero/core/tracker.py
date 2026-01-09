from __future__ import annotations

from dataclasses import dataclass
from datetime import date, timedelta
from typing import Dict, List, Optional, Tuple

from .models import Habit, today_iso


@dataclass
class HabitSummary:
    name: str
    streak: int
    done_today: bool


class HabitTracker:
    def __init__(self) -> None:
        self._habits: Dict[str, Habit] = {}

    def add_habit(self, name: str, created_on: Optional[str] = None) -> Habit:
        name = name.strip()
        if not name:
            raise ValueError("Habit name cannot be empty.")
        if name in self._habits:
            raise ValueError("Habit already exists.")

        created_on = created_on or today_iso()
        h = Habit(name=name, created_on=created_on)
        self._habits[name] = h
        return h

    def list_habits(self) -> List[Habit]:
        return sorted(self._habits.values(), key=lambda h: h.name.lower())

    def get_habit(self, name: str) -> Optional[Habit]:
        return self._habits.get(name)
