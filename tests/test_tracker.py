from habithero.core.tracker import HabitTracker


def test_add_and_list_habit():
    t = HabitTracker()
    t.add_habit("Drink Water", created_on="2026-01-01")
    t.add_habit("Read", created_on="2026-01-01")

    names = [h.name for h in t.list_habits()]
    assert names == ["Drink Water", "Read"]


def test_mark_done_and_streak():
    t = HabitTracker()
    t.add_habit("Workout", created_on="2026-01-01")

    t.mark_done("Workout", day="2026-01-03")
    t.mark_done("Workout", day="2026-01-02")
    t.mark_done("Workout", day="2026-01-01")

    assert t.streak("Workout", as_of="2026-01-03") == 3
    assert t.streak("Workout", as_of="2026-01-04") == 0
