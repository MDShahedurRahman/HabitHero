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
