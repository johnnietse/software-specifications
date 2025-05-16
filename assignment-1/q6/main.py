import string
from typing import List, Tuple


def emailValidatorFSM_Finite_State_Machine(email: str) -> bool:

    # A finite state machine (FSM) function program for validating email addresses.

    # The validation rules:
    # - The local part (before '@') may contain letters, digits, dots (.), hyphens (-), and underscores (_).
    # - The domain part (after '@') must contain only letters and at least one dot (.) separating the domain and top-level domain.
    # - The top-level domain must only contain letters.


    # initial state before processing anything
    state = "Start"
    # flag to check if there is a dot in domain
    dot_in_domain = False

    def transition(char: str, current_state: str) -> str:
        # handle state transitions based on the current character
        nonlocal dot_in_domain

        # beginning of email (start local part)
        if current_state == "Start":
            # here are all the valid characters the question mentioned for the local part
            if char.isalnum() or char in {".", "-", "_"}:
                return "local"
            return "invalid"

        # inside local part of email
        if current_state == "local":
            # again, here are all the valid characters the question mentioned
            if char.isalnum() or char in {".", "-", "_"}:
                return "local"
            # transition to domain part
            if char == "@":
                return "domain_start"
            return "invalid"

        # the start of the domain name must be a letter
        if current_state == "domain_start":
            # again, checking if the domain starts with a letter (the domain must start with a letter)
            if char.isalpha():
                return "domain"
            return "invalid"

        # inside domain name before the dot
        if current_state == "domain":
            # continue with the domain name part
            if char.isalpha():
                return "domain"
            # the dot indicates the start of the top-level domain
            if char == ".":
                dot_in_domain = True
                return "domain_dot"
            return "invalid"

        # inside the top-level domain, again must be letters only
        if current_state == "domain_dot":
            # continue with a valid top-level domain
            if char.isalpha():
                return "domain"
            return "invalid"

        # this is to catch all the invalid cases
        return "invalid"

    # process each character in the email
    for char in email:
        state = transition(char, state)
        # if hit an invalid state, we will then reject the email
        if state == "invalid":
            return False

    # otherwise, the email is valid if we end in a proper domain state and there is a dot in the domain
    return state == "domain" and dot_in_domain


def emailValidator():
    # Testbenches to validate multiple email inputs using the FSM function."""
    the_test_cases: List[Tuple[str, bool]] = [
        ("johnnie.tse@gmail.com", True),  # Valid email
        ("j_t@gmail.co", True),  # Valid email with underscore
        ("@gmail.com", False),  # Invalid email (missing local part)
        ("johnnie.tse@.com", False),  # Invalid email (missing domain part)
        ("johnnie-tse@g.mail.com", True),  # Valid email with subdomain
        ("johntse@gmail", False),  # Invalid email (missing top-level domain)
        ("john.tse@994.com", False),  # Invalid email (digits in domain)
        ("johnnietse994@gmail.com", True),  # Valid email (personal test case with my full email)
        ("t.johnnie_tse-name@gmail.com", True)  # Valid email (with multiple types of characters (letters, dots, hyphens, and underscores), local part with all possible valid letters and domain & top-level domain with only letters)
    ]




    #  Run the test cases to test the emailValidatorFSM_Finite_State_Machine() function out and print the results out
    for email, expected in the_test_cases:
        result = "Valid" if emailValidatorFSM_Finite_State_Machine(email) else "Invalid"
        print(f"{email}: {result} (Expected: {'Valid' if expected else 'Invalid'})")


if __name__ == '__main__':
    emailValidator()
