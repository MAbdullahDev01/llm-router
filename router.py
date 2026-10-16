from memory import Memory
from utils import load_model_data

rules = [
            {
                "name": "complex_coding",
                "signals": ["debug", "refactor", "implement"],
                "route": "strong",
            },
            {
                "name": "simple_definition",
                "signals": ["define", "what does"],
                "route": "cheap",
            },
        ]

# function to route the prompt to the appropriate model based on the rules
def route(prompt : str, memory : Memory):
    ...