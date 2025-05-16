# software-specifications

This repository contains my solutions for **Assignment 1** and **Assignment 2** of the **Software Specifications** course at Queen's University. The assignments cover formal languages, automata theory, and algorithm verification.

---

## 📂 Repository Structure


---

## 📝 Assignment Details

### **Assignment 1**
- **Topics**: Regular languages, finite automata, NFA/DFA conversions.
- **Key Problems**:
  - Problem 1: Design a finite automaton for a specific string set.
  - Problem 6: Email validator using state machines.
  - Problem 8: FA simulator for string acceptance.

### **Assignment 2**
- **Topics**: Context-free grammars, PDAs, Turing machines.
- **Key Problems**:
  - Problem 2: PDA for `L = {wcw^R}`.
  - Problem 3: PDA simulator implementation.
  - Problem 4: Turing machine design for `L = {wxw^R}`.

---

## 🛠 Tools & Languages
- **Theory**: LaTeX (for proofs/diagrams) or handwritten solutions scanned to PDF.
- **Programming**: Python (preferred), C/C++, or Java.
- **Validation**: Test suites for automata simulators (e.g., `test_cases.txt`).

---

## 🚀 How to Run Code
### For Problem 6 (Email Validator):
1. Navigate to `Assignment1/q6/`.
2. Run the script:
   ```bash
   python email_validator.py < input.txt
