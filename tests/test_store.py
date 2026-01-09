from pathlib import Path
from habithero.storage.json_store import JsonStore
from habithero.core.tracker import HabitTracker


def test_store_save_and_load(tmp_path):
    db = tmp_path / "db.json"
    store = JsonStore(db_file=db)

    t = HabitTracker()
    t.add_habit("Meditate", created_on="2026-01-01")
    t.mark_done("Meditate", day="2026-01-02")

    store.save(t)
    loaded = store.load()

    assert [h.name for h in loaded.list_habits()] == ["Meditate"]
    assert loaded.streak("Meditate", as_of="2026-01-02") == 1
