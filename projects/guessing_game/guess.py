import random


def main():
    number = random.randint(1, 10)
    attempts = 0
    print("Guess the number between 1 and 10")

    while True:
        guess = input("Your guess: ")
        attempts += 1
        try:
            guess_num = int(guess)
        except ValueError:
            print("Please enter a valid integer")
            continue

        if guess_num == number:
            print(f"Correct! You needed {attempts} attempts.")
            break
        elif guess_num < number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")


if __name__ == "__main__":
    main()
