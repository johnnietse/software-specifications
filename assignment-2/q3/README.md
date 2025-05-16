# Problem 3 Program Description: PDA Simulator for the language L = { w c w^R }

This project implements a **Pushdown Automaton (PDA)** to determine whether an input string belongs to the language "L = { w c w^R }".
- "w" is a string of "0"s & "1"s.
- "c" is used to separate the string into two parts: "w" & "w^R".
- "w^R" is the reverse of "w".


The solution fulfills all the requirements mentioned in Problem 3 by explicitly implementing stack operations and state transitions without using any external libraries.

---

## Requirements that I met
1. **PDA simulation**: Processes input string(s) and check whether they belong to the language "L"
2. **Handling explicit stack operations**: Handle custom stack implementation with "pop", "push", "peek", and "empty" functions
3. **Implement transition function**: Manages state changes based on input symbols & stack contents


## How to run the code to test the PDA:
1. **Execute the code by running the following line in the terminal**:
   ```bash
   python3 q3.py
   ```
   
---

## Expected Output:
```text
[Passed] -> Test Case: c
[Passed] -> Test Case: 0c0
[Passed] -> Test Case: 1c1
[Passed] -> Test Case: 0c1
[Passed] -> Test Case: 10c0
[Passed] -> Test Case: 01c10
[Passed] -> Test Case: 10c01
[Passed] -> Test Case: 01c01
[Passed] -> Test Case: 10c10
[Passed] -> Test Case: 001c100
[Passed] -> Test Case: 010c010
[Passed] -> Test Case: 01cc10
[Passed] -> Test Case: 10c01c10
```

You should expect to see the following output once you run the program by running "python3 q3.py" to execute the program.

In order to provide input for the program, you can add and remove any instances from the "testCases" list as seen below. But remember to add any new tuples in the format of "inputString, expected". For "expected", you have two options: "True" or "False". "True" means accepted, "False" means rejected.:
```text
testCases = [
    ("c", True),
    ("0c0", True),
    ("1c1", True),
    ("0c1", False),
    ("10c0", False),
    ("01c10", True),
    ("10c01", True),
    ("01c01", False),
    ("10c10", False),
    ("001c100", True),
    ("010c010", True),
    ("01cc10", False),
    ("10c01c10", False)
]
```