from cost_calculation import basic_cost_calculation

def main():
    try:
        while True:
            prompt = input("Enter your prompt/task: ")

            print(f"Cost for prompt is: {basic_cost_calculation(prompt)}")
            # send prompt to selected model
            # return response from model
            # repeat cycle till user exits
    except KeyboardInterrupt:
        print("Exiting program.")


if __name__ == "__main__":
    main()