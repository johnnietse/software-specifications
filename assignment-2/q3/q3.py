"""we are simulating a stack data structure with the stack operations such as pop, push, peek, empty, etc."""
class simulatorForStack:
    """initialize the initial stack symbol "$" to handle the empty inputs"""
    def __init__(self):
        # initial stack symbol
        self.__elements = ['$']

    """push an element onto the top of stack"""
    def push(self, ele):
        self.__elements.append(ele)

    """pop which means to remove and return the top element of stack. However, it will return "None" if the stack is empty"""
    def pop(self):
        return self.__elements.pop() if self.__elements else None

    """return the top element of stack without removing it. Again, return "None" if the stack is empty"""
    def peek(self):
        return self.__elements[-1] if self.__elements else None

    """check if stack is empty but ignore the initial stack symbol "$" """
    def empty(self):
        return len(self.__elements) == 0


"""for simulating a PDA to check if input string matches the Language L = {w c w^R} """
# we have to validate this input string: input_seq: str
def simulate_pda(input_seq: str) -> bool:
    stack = simulatorForStack()
    """push symbols onto stack until we encounter "c" """
    state = "push"

    for sym in input_seq:
        """build stack with symbols before we encounter "c" """
        if state == "push":
            if sym in ('0', '1'):
                stack.push(sym)
            # if we encounter "c" then transition to the phase that does reverse-checking
            elif sym == 'c':
                state = "pop"
            # reject if we encounter invalid symbols
            else:
                return False

        elif state == "pop":
            #we need to verify whether the symbols after "c" match the reverse of the stack
            if sym in ('0', '1'):
                # if we find the match, pop the symbol
                if stack.peek() == sym:
                    stack.pop()
                # if we didn't find the match or is a mismatch, then we reject the input string
                else:
                    return False
            # again, reject any invalid symbols
            else:
                return False
        # reject any invalid state
        else:
            return False

    # make transition to the accept state if the stack only has the initial stack symbol "$" left
    if state == "pop" and stack.peek() == '$':
        # remove the initial stack symbol "$"
        stack.pop()
        # make transition to the accept state
        state = "Accept"

    # stack is empty and state is accept
    return state == "Accept" and stack.empty()


# here are all the test cases for testing the PDA
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


def testPDAImplementation():
    # run the test cases
    for inputString, expected in testCases:
        result = simulate_pda(inputString)
        current_status = "Passed" if result == expected else "Failed"
        print(f"[{current_status}] -> Test Case: {inputString}")


if __name__ == "__main__":
    testPDAImplementation()