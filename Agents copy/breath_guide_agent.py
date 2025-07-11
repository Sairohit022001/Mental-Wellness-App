from crewai import Agent
import time

class BreathGuideAgent(Agent):
    def __init__(self):
        super().__init__(name="BreathGuideAgent", role="Breathing Guide")

    def start_breathing(self, cycles: int = 3) -> list:
        guide = []
        for _ in range(cycles):
            guide.append("Inhale slowly...")
            time.sleep(1)
            guide.append("Hold...")
            time.sleep(1)
            guide.append("Exhale slowly...")
            time.sleep(1)
        return guide
