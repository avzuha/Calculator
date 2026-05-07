# Scientific Calculator
Simple Scientific Calculator GUI
built using Python’s Tkinter library.
It supports both basic arithmetic operations and scientific functions like trigonometry, logarithms, square root, exponentials, and constants such as π.

 Features
- Basic Operations: Addition, subtraction, multiplication, division.
- Scientific Functions: sin, cos, tan, log, sqrt, exp.
- Constants: π (pi).
- Error Handling: Displays "Error" for invalid inputs.
- User-Friendly Interface:
- Pink-themed background (#ffc0cb).
- Buttons styled with hot pink (#ff69b4) and white text.
- Large, clear display for input/output.

 GUI Layout
- Top Row: Entry display for input/output.
- Buttons Grid:
- Numbers 0–9
- Operators: +, -, *, /
- Functions: sin, cos, tan, log, sqrt, exp
- Constants: pi
- Special: C (Clear), = (Evaluate)

 Notes
- The calculator uses Python’s built-in eval() for evaluation.
- eval() can execute arbitrary code if misused.
- Designed for educational purposes and basic scientific calculations.

 Example Usage
- Input: 2+3*4 → Output: 14
- Input: sin(pi/2) → Output: 1.0
- Input: log(10) → Output: 2.302585092994046

 Future Improvements
- Add support for parentheses buttons.
- Implement memory functions (M+, M-, MR).
- Replace eval() with a safer expression parser.
- Extend scientific functions (e.g., asin, acos, atan).

