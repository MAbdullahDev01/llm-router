from cost_calculation import cost_calculation_with_chat_history
from memory import Memory

def main():
    memory = Memory()
    try:
        while True:
            prompt = input("Enter your prompt/task: ")

            print(f"Cost for prompt is: {cost_calculation_with_chat_history(prompt, memory)}")
            # send prompt to selected model
            # return response from model
            # repeat cycle till user exits
    except KeyboardInterrupt:
        print("Exiting program.")


if __name__ == "__main__":
    main()