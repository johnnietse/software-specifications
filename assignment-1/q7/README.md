# DFA Simulation Code for Question 7 b)

## Description of the problem:
The purpose of the code is to design a DFA that processes strings over the alphabet {a,b}. The DFA accepts all the strings where the absolute difference between the number of a's (n<sub>a</sub>) and b's (n<sub>b</sub>) is at most 3 (meaning no greater than 3, but it can accept 3). The example given by the question is this: i.e., |n<sub>a</sub> - n<sub>b</sub>| ≤ 3. The DFA will then reject any strings that have the absolute difference (|n<sub>a</sub> - n<sub>b</sub>|) that exceed this threshold. Also, given that the question also states that "given in the Table for question 7.c i.e., string length wll not exceed the maximum string length in the table" where we can see in the Table for question 7.c that the string with the greatest string length is 16, this suggests that the maximum string length will not exceed the number of 16 characters in this case.

## Running the program/the simulator function:
To execute the program/simulator function, we first have to ensure that a Python IDE has been properly installed into your local computer. You can then run the code by clicking the "Run" button in an IDE like the PyCharm to run the code script without typing in any commands into the IDE terminal. Of course, you can copy the code and run it on an online python compiler. This can avoid having to download the code script file into your local computer and also checking whether the downloaded code script file has a current working directory that is correct before you run it with a command (which is the directory where the dowloaded code script file should be located). Otherwise, you will have to "cd" the directory to where the downloaded code script file is located before you run the command to run the script. After you have everything checked out, you can run the script by typing the following command to run the script if you choose to run the script with a command and not by running the script in an IDE with a "Run" button OR by running the script with an online python compiler.

```shell
python main.py
```

By running this command to run the script, you should expect the output to be all the strings defined in the table in the question as well as these input strings' corresponding/respective status after each input string has been processed based on the DFA's conditions. There are two status for the input string: "Accepted" or "Rejected".



## Customizing the input strings
The list, input_strings_test_cases, in the script contains all the input strings from the table of the question that the questions asks us to test for. You can certainly modify the list to add more or remove strings to/from the list for testing other strings that you want to test for. The script also assumes that the provided strings only contain 'a' and 'b' characters. Any other characters/symbols will not be handled by the script and thus will cause/return an error as they are not supported by this program/simulator function. I will refer to the list from the script for you below to ensure you modify the correct one if you choose to add or remove strings to/from the list:

```python
input_strings_test_cases = [
            "aaa",
            "abab",
            "aaaabbb",
            "aaaaaaa",
            "bbbbbbb",
            "aaaaaaabbbbbbbb", 
            ...
]
```