from crewai import Agent
import subprocess

class ResponseAgent(Agent):
    def __init__(self, llama_cli_path: str, model_path: str):
        super().__init__(name="ResponseAgent", role="LLM Responder")
        self.cli_path = llama_cli_path
        self.model_path = model_path

    def respond(self, prompt: str) -> str:
        try:
            result = subprocess.run(
                [self.cli_path, "-m", self.model_path, "-p", prompt],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            return result.stdout.split("<start_of_turn>model")[-1].strip()
        except Exception as e:
            return f"Error generating response: {e}"
