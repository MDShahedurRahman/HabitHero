from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import List, Set


@dataclass
class Habit:
    name: str
    created_on: str  # YYYY-MM-DD
    done_dates: Set[str] = field(default_factory=set)

    def mark_done(self, day: str) -> None:
        self.done_dates.add(day)

    def is_done(self, day: str) -> bool:
        return day in self.done_dates


def today_iso() -> str:
    return date.today().isoformat()
