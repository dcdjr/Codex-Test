def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def main():
    print("Simple Calculator")
    print("Enter 'q' to quit")

    while True:
        first = input("First number: ")
        if first == 'q':
            break
        second = input("Second number: ")
        if second == 'q':
            break
        op = input("Operation (+, -, *, /): ")
        if op == 'q':
            break

        try:
            a = float(first)
            b = float(second)
            if op == '+':
                result = add(a, b)
            elif op == '-':
                result = subtract(a, b)
            elif op == '*':
                result = multiply(a, b)
            elif op == '/':
                result = divide(a, b)
            else:
                print("Unknown operation")
                continue
            print("Result:", result)
        except ValueError as e:
            print("Error:", e)


if __name__ == "__main__":
    main()
