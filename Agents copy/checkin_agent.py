from crewai import Agent

class CheckInAgent(Agent):
    def __init__(self):
        super().__init__(name="CheckInAgent", role="Mood Tracker")
        self.history = []

    def record(self, mood: str, note: str = "") -> str:
        entry = {"mood": mood, "note": note}
        self.history.append(entry)
        return f"Mood recorded: {mood}. Thank you for sharing."

    def get_history(self) -> list:
        return self.history
