from crewai import Agent

class JournalingAgent(Agent):
    def __init__(self):
        super().__init__(name="JournalingAgent", role="Wellness Companion")
        self.entries = []

    def write(self, input_text: str) -> str:
        self.entries.append(input_text)
        return "Your thoughts have been noted. Reflecting regularly helps with clarity."

    def get_journal(self) -> list:
        return self.entries
