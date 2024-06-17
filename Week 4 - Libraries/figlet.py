from pyfiglet import Figlet
import random
import sys

fonts = Figlet()
fonts = fonts.getFonts()

def main():
    if len(sys.argv) == 1:
        font = random.choice(fonts)
    elif len(sys.argv) == 3:
        if sys.argv[1] in ["-f", "--font"] and sys.argv[2] in fonts:
            font = sys.argv[2]
        else:
            sys.exit("Invalid arguments.")
    else:
        sys.exit("Invalid number of arguments.")

    user_input = input("Input: ")
    print("Output:\n", Figlet(font=font).renderText(user_input))


if __name__ == "__main__":
    main()
