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


def test_weekly_counts_across_habits():
    t = HabitTracker()
    t.add_habit("A", created_on="2026-01-01")
    t.add_habit("B", created_on="2026-01-01")

    t.mark_done("A", day="2026-01-07")
    t.mark_done("B", day="2026-01-07")
    t.mark_done("A", day="2026-01-06")

    last7 = dict(t.weekly_counts(end_day="2026-01-07"))
    assert last7["2026-01-07"] == 2
    assert last7["2026-01-06"] == 1
