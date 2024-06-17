import random

def get_positive_integer(prompt):

    #Prompt the user for a positive integer and return it.
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
        except ValueError:
            pass

def main():
    # Prompt the user for a level
    level = get_positive_integer("Level: ")

    # Randomly generate an integer between 1 and the level, inclusive
    target = random.randint(1, level)

    while True:
        # Prompt the user to guess the integer
        guess = get_positive_integer("Guess: ")

        if guess < target:
            print("Too small!")
        elif guess > target:
            print("Too large!")
        else:
            print("Just right!")
            break

if __name__ == "__main__":
    main()
