def basic_cost_calculation(prompt : str) -> float:

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
    return cost