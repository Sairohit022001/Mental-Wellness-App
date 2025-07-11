from crewai import Agent

class FallbackAgent(Agent):
    def __init__(self):
        super().__init__(name="FallbackAgent", role="Safety Responder")

    def fallback(self, user_input: str) -> str:
        return (
            "I'm sorry, I didn't understand that. "
            "Try journaling, checking in, or doing a breathing exercise."
        )
