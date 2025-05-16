# Question 8's Code

## Description of the problem
This program simulates a finite automaton (FA) to determine whether a given input string is accepted or rejected by a finite automaton (FA). The finite automation (FA) is defined using the 5-tuple format, which includes:

- States: Set of states in the finite automaton.
- Alphabet: Set of input symbols that the finite automaton processes.
- Transitions: A dictionary that defines how the finite automaton moves/transitions between states based on input symbols. Basically, state changes based on input symbols.
- Start state: The state where the finite automaton begins processing/everything.
- Accept states: The set of states in which the finite automaton halts and accepts the input string.

- For this problem, remember that the finite automation (FA) is designed with the following configuration:

- States: q0, q1, q2
- Alphabet: 0, 1
- Transitions:
  - ("q0", "0") -> "q1"
  - ("q0", "1") -> "q0"
  - ("q1", "0") -> "q2"
  - ("q1", "1") -> "q0"
  - ("q2", "0") -> "q2"
  - ("q2", "1") -> "q2"
- Start state: q0
- Accept state: q2
  
Input String List:
- "0", "01", "001", "0001", "111", "10", "000"
  
Note that the FA can be NFA or DFA.

# How to Run the script/program
To run this program, make sure that you have Python installed onto your local computer and also make sure that your working directory is set to where the script is located and has been placed.

## Running via IDE:
If you are using an IDE like PyCharm:

1. Open the script file.
2. Click the green "Run" button to run the script file.

## Running via Command Line
If you prefer running the script from the terminal, ensure that your terminal is in the correct directory where the script file is located. If not, "cd" to the directory where the script file has been placed/is located. Then, run the following command:

```python
python main.py
```

This will execute the program and display an output similar to the output below.

# Expected Output
After running the script, it will process each input string in the provided list and print whether each string will be return as "False" or "True" in the "Accepted" status based on the fa_description. For example:

```text
Input: 0 -> Accepted: False
Input: 01 -> Accepted: False
Input: 001 -> Accepted: True
Input: 0001 -> Accepted: True
Input: 111 -> Accepted: False
Input: 10 -> Accepted: False
Input: 000 -> Accepted: True
```

# Customizing the input strings
To test additional input strings, you can modify the list of input strings within the script by adding or removing string(s) to/from the list. The list is defined as follows:

```python
input_strings = ["0", "01", "001", "0001", "111", "10", "000"]
```
You can add or remove strings from this list to test different cases. Be sure to only include valid input strings made up of the alphabet symbols defined in the fa_description (in this case, "0" & "1"). If any input string contains characters outside this alphabet, the program will return an error.

# FA Description Format
The finite automation (FA) is defined by the following dictionary, which you can also customize (but I would not recommend you to customize it because it will no longer meet all the requirements of the question as this is a program dedicated for this specific purpose):

```python
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
    "accept_states": {"q2"},
}
```


