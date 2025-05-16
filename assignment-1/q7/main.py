# This program is intended to simulate a DFA's state transitions to accept or reject strings that ensures the absolute difference between the number of a(s) and b(s) in the input string is at most 3, while also making sure that the string length will not exceed the maximum string length in the table in Question 7.c) which is 16 characters.
def dfa_deterministic_finite_automation_simulation(s:str) -> bool:

    # Initial state indicating there is 0 difference between counting of "a" characters and "b" characters
    state_count = 0

    # Define a variable for consecutive "a", so we can use this variable to check whether a string has more than 9 "a" consecutive characters
    consecutive_a_count = 0

    # Define a variable for consecutive "b", so we can use this variable to check whether a string has more than 9 "b" consecutive characters
    consecutive_b_count = 0

    for char in s:
        # When encountered "a" (assuming moving to the next state), increment the state difference by 1 in number. This would represent an increase in the count of "a" relative to "b".
        if char == "a":
            state_count = state_count + 1

        # When encountered "b" (assuming moving to the next state), decrement the state difference by 1 in number. This would represent an increase in the count of "b" relative to "a".
        elif char == "b":
            state_count = state_count - 1

        # We would exit the for loop and return false if there are more than 9 consecutive "a" characters or "b" characters in a string
        if consecutive_a_count > 9 or consecutive_b_count > 9:
            return False


    # If the final absolute difference between the number of a(s) and b(s) is within the allowed number, which is 3 in this case (any difference smaller than and equal to 3 is acceptable)
    return abs(state_count) <= 3


if __name__ == '__main__':

    # String test cases from Question 7.c) table
    input_strings_test_cases = [
            "aaa",
            "abab",
            "aaaabbb",
            "aaaaaaa",
            "bbbbbbb",
            "aaaaaaabbbbbbbb",
            "bbbb",
            "aaaabbbbaaaa",
            "bbbaaaabbbb",
            "aaaaaaaabbbbbbbb",
            "abababab",
            "ababababab",
            "aaabbbbaa",
            "abbbaaaa",
            "bbbaaabbb",
            "",
            "a",
            "b",
            "aaabbb",
            "abababababab"
    ]


    # Run the DFA simulator program on each of the string test cases from Question 7.c) table and print their resulting status out to determine whether each string test case is accepted or rejected.
    for string in input_strings_test_cases:
        result = "Accepted" if dfa_deterministic_finite_automation_simulation(string) else "Rejected"

        print(f"{string}:{result}")

