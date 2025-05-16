# This program is a Finite Automaton (FA) Checker that checks whether an input string is accepted by a finite automation (FA).

class finiteAutomatonChecker:
    def __init__(self, fa_description):
        # initialize the finite automaton (FA) with states, alphabet, transitions, start state, and accept states.
        # fa_description: describing the FA in the 5-tuple format as mentioned in the question

        self.states = fa_description["states"]
        self.alphabet = fa_description["alphabet"]
        self.transitions = fa_description["transitions"]
        self.start_state = fa_description["start_state"]
        self.accept_states = fa_description["accept_states"]

    def processString(self, input_string: str) -> bool:
        # process an input string through the FA following the state transitions to determine whether it is accepted by the FA or not.
        # input_string is the input string to be tested for in our program.
        # we will return true if accepted, false otherwise.

        current_state = self.start_state  # we will first start at the initial state

        for symbol in input_string:
            # let's make sure that we are only dealing with valid symbols by checking if the symbol is valid
            if symbol not in self.alphabet:
                return False  # invalid character, then reject

            # transition to the next state if there is a defined transition
            transition_key = (current_state, symbol)
            if transition_key in self.transitions:
                current_state = self.transitions[transition_key]
            else:
                return False  # no transition/no valid transition then reject

        # check if the final state is an accept state. If yes and we finish in an accept state, then the FA will accept this tested input string.
        return current_state in self.accept_states


if __name__ == "__main__":
    # define finite automaton description
    fa_description = {
        "states": {"q0", "q1", "q2"},
        "alphabet": {"0", "1"},
        "transitions": {
            ("q0", "0"): "q1",
            ("q0", "1"): "q0",
            ("q1", "0"): "q2",
            ("q1", "1"): "q0",
            ("q2", "0"): "q2",
            ("q2", "1"): "q2",
        },
        "start_state": "q0",
        "accept_states": {"q2"}
    }

    # test input strings
    input_strings = ["0", "01", "001", "0001", "111", "10", "000"]

    # create a FA instance
    fa = finiteAutomatonChecker(fa_description)

    # run the acceptance check for each of the testing input string and see if the string is accepted
    for inputString in input_strings:
        result = fa.processString(inputString)
        print(f"Input: {inputString} -> Accepted: {result}")
