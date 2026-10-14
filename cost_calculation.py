from memory import Memory

def basic_cost_calculation(prompt : str) -> tuple[float, float, float, float, float]:

    # Assuming model uses character tokenization
    chars : int = len(prompt)

    # 4 characters = 1 token
    input_tokens : float = chars / 4

    # Assuming output tokens are half of input
    output_tokens : float = input_tokens / 2

    # Assuming model has $0.005 per 1 million input tokens and twice the price for output
    input_cost : float = (input_tokens / 1000000) * 0.005
    output_cost : float = (output_tokens / 1000000) * 0.01

    cost : float = input_cost + output_cost

    # This cost is purely token based; does not yet include caching, extra components, and real-world usage factors like chat history, etc.
    return input_tokens, output_tokens, input_cost, output_cost, cost

def cost_calculation_with_chat_history(prompt : str, memory : Memory) -> float:

    input_tokens, output_tokens, input_cost, output_cost, cost = basic_cost_calculation(prompt)
    memory.add_exchange(input_tokens, output_tokens)
    return memory.total_cost_calculation()