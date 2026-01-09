from __future__ import annotations

import json
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict

from habithero.core.tracker import HabitTracker


@dataclass(frozen=True)
class StorePaths:
    base_dir: Path
    db_file: Path


def get_paths() -> StorePaths:
    home = Path(os.path.expanduser("~"))
    base = home / ".habithero"
    return StorePaths(base_dir=base, db_file=base / "db.json")


class JsonStore:
    def __init__(self, db_file: Path | None = None) -> None:
        paths = get_paths()
        self.db_file = db_file or paths.db_file

    def load(self) -> HabitTracker:
        if not self.db_file.exists():
            return HabitTracker()

        try:
            data = json.loads(self.db_file.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return HabitTracker()

        return HabitTracker.from_dict(data)

    def save(self, tracker: HabitTracker) -> None:
        self.db_file.parent.mkdir(parents=True, exist_ok=True)
        self.db_file.write_text(
            json.dumps(tracker.to_dict(), indent=2),
            encoding="utf-8",
        )
