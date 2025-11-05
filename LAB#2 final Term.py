# Moore Machine simulation (CS13A – Lab 2)

moore_machine = {
    'A': {'0': ('A', 'A'), '1': ('B', 'B')},
    'B': {'0': ('C', 'A'), '1': ('D', 'B')},
    'C': {'0': ('D', 'C'), '1': ('B', 'B')},
    'D': {'0': ('B', 'B'), '1': ('C', 'C')},
    'E': {'0': ('D', 'C'), '1': ('E', 'C')}
}

def process_input(machine, input_str, start='A'):
    """Simulate Moore machine and return the output string."""
    output = machine[start]['0'][1]  # Initial state's output
    state = start
    for symbol in input_str:
        next_state, out = machine[state][symbol]
        output += out
        state = next_state
    return output

# Input test cases
inputs = ["00110", "11001", "101010", "101111"]

print("=== Moore Machine Simulation ===")
for inp in inputs:
    result = process_input(moore_machine, inp)
    print(f"Input: {inp} -> Output: {result}")
