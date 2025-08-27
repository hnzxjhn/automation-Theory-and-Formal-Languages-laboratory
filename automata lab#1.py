# Automata Theory and Formal Languages - Laboratory 1
# DFA/NFA simulation for given automata diagrams
# (Enhanced: tracing, input validation, tidy printouts)

# -------------------------
# Question 1  (formerly Automaton 1)
# -------------------------
# States: a, b, c
# Start state: a
# Accepting state: c
# Transitions:
# a --0--> a
# a --1--> b
# b --0--> c
# b --1--> a
# c --0--> b
# c --1--> c (loop)

question1 = {
    'a': {'0': 'a', '1': 'b'},
    'b': {'0': 'c', '1': 'a'},
    'c': {'0': 'b', '1': 'c'}
}
start_q1 = 'a'
accept_q1 = {'c'}

# -------------------------
# Question 2  (formerly Automaton 2)
# -------------------------
# States: q0, q1, q2, q3
# Start state: q0
# Accepting state: q0 (highlighted)
# Transitions: square movement
# q0 --a--> q1, q0 --b--> q2
# q1 --a--> q3, q1 --b--> q0
# q2 --a--> q0, q2 --b--> q3
# q3 --a--> q2, q3 --b--> q1

question2 = {
    'q0': {'a': 'q1', 'b': 'q2'},
    'q1': {'a': 'q3', 'b': 'q0'},
    'q2': {'a': 'q0', 'b': 'q3'},
    'q3': {'a': 'q2', 'b': 'q1'}
}
start_q2 = 'q0'
accept_q2 = {'q0'}

# -------------------------
# DFA Simulator (with trace + validation)
# -------------------------
def alphabet(automaton):
    """Infer the alphabet from the transition table."""
    symbols = set()
    for trans in automaton.values():
        symbols |= set(trans.keys())
    return symbols

def simulate(automaton, start, accept, string):
    """Return True/False if string is accepted by the DFA."""
    state = start
    for ch in string:
        if ch not in automaton[state]:
            return False
        state = automaton[state][ch]
    return state in accept

def simulate_trace(automaton, start, accept, string):
    """Return (accepted: bool, path: list of (state, symbol, next_state))."""
    path = []
    state = start
    for ch in string:
        if ch not in automaton[state]:
            path.append((state, ch, None))  # invalid symbol/transition
            return False, path
        nxt = automaton[state][ch]
        path.append((state, ch, nxt))
        state = nxt
    return (state in accept), path

def print_result(title, automaton, start, accept, examples):
    print(title)
    print("-"*len(title))
    sig = alphabet(automaton)
    print(f"Alphabet: {sorted(sig)}")
    print(f"Start: {start} | Accepting: {sorted(accept)}\n")

    # quick validation of symbol set per string
    for s in examples:
        bad = [ch for ch in s if ch not in sig]
        if bad:
            print(f"⚠️  Skipping '{s}' (invalid symbols: {set(bad)})")
            continue
        ok, path = simulate_trace(automaton, start, accept, s)
        verdict = "ACCEPTED ✅" if ok else "REJECTED ❌"
        print(f"Input: '{s}' → {verdict}")
        # show step-by-step trace
        if path:
            steps = " → ".join([f"{st} -{sym}-> {nx}" for (st, sym, nx) in path])
        else:
            steps = f"(ε) start at {start}"
        print(f"Trace: {steps}\n")

# -------------------------
# Test Examples
# -------------------------

# Question 1 (Σ = {0,1})
examples_q1 = [
    '10111',  # ACCEPTED
    '101',    # ACCEPTED
    '010',    # ACCEPTED
    '0',      # REJECTED
    '111',    # REJECTED
    '100'     # REJECTED
]

# Question 2 (Σ = {a,b})
# Accepted iff the number of a's is even AND the number of b's is even.
examples_q2 = [
    'abba',   # ACCEPTED  (2 a's, 2 b's)
    'bbaa',   # ACCEPTED  (2 a's, 2 b's)
    'aabb',   # ACCEPTED  (2 a's, 2 b's)
    'ab',     # REJECTED  (1 a, 1 b) -> odd+odd => not q0
    'aba',    # REJECTED  (2 a's, 1 b) -> b odd
    'bbb'     # REJECTED  (0 a's, 3 b's) -> b odd
]

# -------------------------
# Run
# -------------------------
print_result("Question 1 Results", question1, start_q1, accept_q1, examples_q1)
print()
print_result("Question 2 Results", question2, start_q2, accept_q2, examples_q2)