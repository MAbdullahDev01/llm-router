class Memory:
    def __init__(self):
        self.total_input_tokens : float = 0.0
        self.total_output_tokens : float = 0.0
        self.total_input_cost : float = 0.0
        self.total_output_cost : float = 0.0
        self.total_cost : float = 0.0
        self.token_history : dict[int, list[float]] = {}
        self.exchange_number : int = 1

    def add_exchange(self, input_tokens : float, output_tokens : float) -> None:
        self.token_history[self.exchange_number] = [input_tokens, output_tokens]
        self.exchange_number += 1
        self.total_input_tokens += input_tokens
        self.total_output_tokens += output_tokens

    def total_cost_calculation(self) -> float:
        self.total_input_cost : float = (self.total_input_tokens / 1000000) * 0.005
        self.total_output_cost : float = (self.total_output_tokens / 1000000) * 0.01
        self.total_cost = self.total_input_cost + self.total_output_cost
        return self.total_output_cost