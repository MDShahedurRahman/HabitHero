from __future__ import annotations

from habithero.core.tracker import HabitTracker
from habithero.storage.json_store import JsonStore


MENU = """
HabitHero ✅
------------
1) Add habit
2) List habits
3) Mark done (today)
4) Summary (streaks)
5) Weekly activity (last 7 days)
6) Quit
"""


def run() -> None:
    store = JsonStore()
    tracker: HabitTracker = store.load()

    while True:
        print(MENU)
        choice = input("Choose (1-6): ").strip()

        if choice == "6":
            store.save(tracker)
            print("Saved. Bye!")
            break

        if choice == "1":
            name = input("Habit name: ").strip()
            try:
                tracker.add_habit(name)
                store.save(tracker)
                print("Added.\n")
            except ValueError as e:
                print(f"Error: {e}\n")

        elif choice == "2":
            habits = tracker.list_habits()
            if not habits:
                print("No habits yet.\n")
            else:
                for h in habits:
                    print(f"- {h.name} (created {h.created_on})")
                print()

        elif choice == "3":
            name = input("Habit name to mark done: ").strip()
            try:
                tracker.mark_done(name)
                store.save(tracker)
                print("Done for today.\n")
            except KeyError:
                print("Habit not found.\n")

        elif choice == "4":
            for s in tracker.summary():
                status = "✅" if s.done_today else "⬜"
                print(f"{status} {s.name} | streak: {s.streak}")
            print()

        elif choice == "5":
            for day, count in tracker.weekly_counts():
                print(f"{day}: {count} completion(s)")
            print()

        else:
            print("Invalid option.\n")
