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
