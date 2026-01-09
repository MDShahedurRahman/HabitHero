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

    def mark_done(self, name: str, day: Optional[str] = None) -> Habit:
        h = self.get_habit(name)
        if h is None:
            raise KeyError("Habit not found.")
        day = day or today_iso()
        h.mark_done(day)
        return h

    def streak(self, name: str, as_of: Optional[str] = None) -> int:
        h = self.get_habit(name)
        if h is None:
            raise KeyError("Habit not found.")

        as_of_date = date.fromisoformat(as_of or today_iso())
        count = 0
        cur = as_of_date

        while True:
            if cur.isoformat() in h.done_dates:
                count += 1
                cur = cur - timedelta(days=1)
            else:
                break
        return count
