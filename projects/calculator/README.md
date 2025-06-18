# Calculator Project

This project demonstrates a simple command-line calculator written in Python.
Below is a line-by-line explanation of `calculator.py`.

```python
1 def add(a, b):
2     return a + b
3 
4 def subtract(a, b):
5     return a - b
6 
7 def multiply(a, b):
8     return a * b
9 
10 def divide(a, b):
11     if b == 0:
12         raise ValueError("Cannot divide by zero")
13     return a / b
14 
15 def main():
16     print("Simple Calculator")
17     print("Enter 'q' to quit")
18 
19     while True:
20         first = input("First number: ")
21         if first == 'q':
22             break
23         second = input("Second number: ")
24         if second == 'q':
25             break
26         op = input("Operation (+, -, *, /): ")
27         if op == 'q':
28             break
29 
30         try:
31             a = float(first)  # convert input to numbers
32             b = float(second)
33             if op == '+':
34                 result = add(a, b)
35             elif op == '-':
36                 result = subtract(a, b)
37             elif op == '*':
38                 result = multiply(a, b)
39             elif op == '/':
40                 result = divide(a, b)
41             else:
42                 print("Unknown operation")
43                 continue
44             print("Result:", result)
45         except ValueError as e:
46             print("Error:", e)
47 
48 if __name__ == "__main__":
49     main()
```

### Explanation

1. **Functions** `add`, `subtract`, `multiply`, and `divide` each perform a basic mathematical
   operation and return the result.
2. **Error Handling** in `divide` prevents division by zero by raising `ValueError`.
3. The `main` function displays instructions and loops until the user types `'q'` to quit.
4. Inside the loop, user input for numbers and operations is converted to floats and used to
   call the relevant function.
5. A `try/except` block catches conversion errors or division by zero and prints an error message.
6. The script runs `main()` when executed directly (the `__name__ == '__main__'` check).
