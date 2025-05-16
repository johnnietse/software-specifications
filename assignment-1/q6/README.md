# Question 6's Code

## Description of the problem:
This program validates email addresses using a finite state machine (FSM) approach. The FSM approach ensures that email addresses follow the required structure:

The local part (before "@") can contain letters, digits, dots ("."), hyphens ("-"), and underscores ("_")
The domain (after "@") must start with a letter, contain only letters, and have at least one dot (".")
The top-level domain (after the dot) must contain only letters

I have included in this program's script file a test suite to verify different email formats and determine whether they are valid or invalid.

## Running the program/the function (sum-up/overview):
To execute the program/function, we first have to ensure that a Python IDE has been properly installed into your local computer. You can then run the code by clicking the "Run" button in an IDE like the PyCharm to run the code script without typing in any commands into the IDE terminal. Of course, you can copy the code and run it on an online python compiler. This can avoid having to download the code script file into your local computer and also checking whether the downloaded code script file has a current working directory that is correct before you run it with a command (which is the directory where the dowloaded code script file should be located). Otherwise, you will have to "cd" the directory to where the downloaded code script file is located before you run the command to run the script. After you have everything checked out, you can run the script by typing the following command to run the script if you choose to run the script with a command and not by running the script in an IDE with a "Run" button OR by running the script with an online python compiler.

```shell
python main.py
```

### Running via Command Line 
1. Open a terminal or the command prompt.
2. Navigate to the directory where the script file has been placed/is located. Type this "cd" command into the terminal to change your directory to the script file directory if the terminal says that it cannot find the script file in the current working directory.
3. Run the following command to run the program

```shell
python main.py
```

By running this command to run the script, it will execute the program and display in the terminal whether each test case email is valid or invalid.

### Running via IDE:
If you are using an IDE like PyCharm:

1. Open the script file.
2. Click the green "Run" button to run the script file.

## Expected Output 
When you run the script file, you should see a list of output similar to this (this only applies to how the original script is written before any modification):

```text
johnnie.tse@gmail.com: Valid (Expected: Valid)
j_t@gmail.co: Valid (Expected: Valid)
@gmail.com: Invalid (Expected: Invalid)
johnnie.tse@.com: Invalid (Expected: Invalid)
johnnie-tse@g.mail.com: Valid (Expected: Valid)
johntse@gmail: Invalid (Expected: Invalid)
john.tse@994.com: Invalid (Expected: Invalid)
johnnietse994@gmail.com: Valid (Expected: Valid)
t.johnnie_tse-name@gmail.com: Valid (Expected: Valid)
```

## Customizing the test cases
This program contains a list of pre-defined email test cases which the question requires us to test for. The question says to "Create a test suite with at least
5 different email inputs to demonstrate the validation logic." But you can definitely make modifications to the test cases and add or remove any test cases to/from this list of tuples (the_test_cases) as shown below:

```python
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

```

In order to add more email test cases, you can simply just add a new pair "(email, expected)" to this list of tuples.