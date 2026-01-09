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

    def summary(self, as_of: Optional[str] = None) -> List[HabitSummary]:
        day = as_of or today_iso()
        out: List[HabitSummary] = []
        for h in self.list_habits():
            out.append(
                HabitSummary(
                    name=h.name,
                    streak=self.streak(h.name, as_of=day),
                    done_today=h.is_done(day),
                )
            )
        return out

    def weekly_counts(self, end_day: Optional[str] = None) -> List[Tuple[str, int]]:
        """
        Returns list of (YYYY-MM-DD, total_done_across_all_habits) for last 7 days.
        """
        end = date.fromisoformat(end_day or today_iso())
        days = [(end - timedelta(days=i)) for i in range(6, -1, -1)]

        result: List[Tuple[str, int]] = []
        for d in days:
            di = d.isoformat()
            count = sum(1 for h in self._habits.values() if di in h.done_dates)
            result.append((di, count))
        return result

    # ---- persistence helpers ----
    def to_dict(self) -> Dict:
        return {
            "habits": [
                {
                    "name": h.name,
                    "created_on": h.created_on,
                    "done_dates": sorted(list(h.done_dates)),
                }
                for h in self.list_habits()
            ]
        }

    @classmethod
    def from_dict(cls, data: Dict) -> "HabitTracker":
        t = cls()
        for item in data.get("habits", []):
            h = Habit(
                name=item["name"],
                created_on=item["created_on"],
                done_dates=set(item.get("done_dates", [])),
            )
            t._habits[h.name] = h
        return t
