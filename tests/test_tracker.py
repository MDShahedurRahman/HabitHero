from habithero.core.tracker import HabitTracker


def test_add_and_list_habit():
    t = HabitTracker()
    t.add_habit("Drink Water", created_on="2026-01-01")
    t.add_habit("Read", created_on="2026-01-01")

    names = [h.name for h in t.list_habits()]
    assert names == ["Drink Water", "Read"]
