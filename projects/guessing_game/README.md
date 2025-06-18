# Guessing Game Project

This project is a simple number guessing game. Run `guess.py` and try to
identify the secret number between 1 and 10. Below is a line-by-line explanation.

```python
1 import random
2
3 def main():
4     number = random.randint(1, 10)
5     attempts = 0
6     print("Guess the number between 1 and 10")
7
8     while True:
9         guess = input("Your guess: ")
10        attempts += 1
11        try:
12            guess_num = int(guess)
13        except ValueError:
14            print("Please enter a valid integer")
15            continue
16
17        if guess_num == number:
18            print(f"Correct! You needed {attempts} attempts.")
19            break
20        elif guess_num < number:
21            print("Too low! Try again.")
22        else:
23            print("Too high! Try again.")
24
25 if __name__ == "__main__":
26     main()
```

### Explanation

1. The `random` module provides the `randint` function to pick a random integer.
2. `number` stores the random target value; `attempts` counts guesses.
3. The program loops indefinitely, asking for a guess each time.
4. Inputs are converted to integers inside a `try/except` block, handling invalid input gracefully.
5. The `if`/`elif`/`else` chain provides feedback if the guess is too low or too high, or ends the game if correct.
6. The final `if __name__ == '__main__':` block allows the script to run when executed directly.
