# src/rules.py
def study_suggestion(time_available: str, energy: str) -> str:
    """Return a study suggestion based on time and energy.

    Valid time_available: short, medium, long
    Valid energy: low, high
    """
    if not time_available or not energy:
        return "Pick a small, achievable task"

    t = str(time_available).strip().lower()
    e = str(energy).strip().lower()

    if t == "short" and e == "low":
        return "Do 1 review question"
    if t == "short" and e == "high":
        return "Watch a 5-min concept video"
    if t == "medium" and e == "low":
        return "Summarize notes (10 min)"
    if t == "medium" and e == "high":
        return "Practice 2 coding problems"
    if t == "long" and e == "low":
        return "Deep read + 1 note page"
    if t == "long" and e == "high":
        return "Build a tiny CLI feature"

    return "Pick a small, achievable task"
