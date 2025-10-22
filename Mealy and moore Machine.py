# Automata Laboratory Activity 1
# Implementation of Mealy and Moore Machines (OOP Version)
# Task: Print 'a' whenever the sequence "01" is encountered

class MealyMachine:
    def __init__(self):
        self.state = 'A'
        self.output = ""

    def transition(self, symbol):
        if self.state == 'A':
            if symbol == '0':
                next_state = 'B'
                out = 'b'
            else:
                next_state = 'A'
                out = 'b'

        elif self.state == 'B':
            if symbol == '0':
                next_state = 'B'
                out = 'b'
            else:
                next_state = 'A'
                out = 'a'  # sequence 01 detected

        # Print formatted transition info
        print(f" |   {symbol}   |     {next_state}      |   {out}")
        self.state = next_state
        self.output += out

    def process(self, input_string):
        print("\n=== MEALY MACHINE ===")
        print("Step | Input | Next State | Output")
        print("----------------------------------")

        for i, symbol in enumerate(input_string):
            print(f"{i+1:>4}", end="")
            self.transition(symbol)

        print("\nFinal Output String (Mealy):", self.output)
        return self.output


class MooreMachine:
    def __init__(self):
        self.state = 'A'
        self.output = ""
        self.outputs = {'A': 'b', 'B': 'b', 'C': 'a'}

    def transition(self, symbol):
        if self.state == 'A':
            if symbol == '0':
                next_state = 'B'
            else:
                next_state = 'A'

        elif self.state == 'B':
            if symbol == '0':
                next_state = 'B'
            else:
                next_state = 'C'  # sequence 01 found

        elif self.state == 'C':
            if symbol == '0':
                next_state = 'B'
            else:
                next_state = 'A'

        out = self.outputs[next_state]

        # Print formatted transition info
        print(f" |   {symbol}   |     {next_state}      |   {out}")
        self.state = next_state
        self.output += out

    def process(self, input_string):
        print("\n=== MOORE MACHINE ===")
        print("Step | Input | Next State | Output")
        print("----------------------------------")

        for i, symbol in enumerate(input_string):
            print(f"{i+1:>4}", end="")
            self.transition(symbol)

        print("\nFinal Output String (Moore):", self.output)
        return self.output


# -----------------------
# MAIN PROGRAM
# -----------------------
if __name__ == "__main__":
    print("Automata Lab Activity 1: Mealy and Moore Machine Example")
    print("Task: Print 'a' whenever the sequence '01' is encountered.\n")

    user_input = input("Enter input string (e.g., 0101 or 11001): ").strip()

    # Create objects
    mealy = MealyMachine()
    moore = MooreMachine()

    # Run processes
    mealy_output = mealy.process(user_input)
    moore_output = moore.process(user_input)
