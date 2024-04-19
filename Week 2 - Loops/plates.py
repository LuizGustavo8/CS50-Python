import string


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    counter = 0
    string_conditions = False
    char_conditions = True
    if len(s) <= 6 and len(s) >= 2 and s[0].isalpha() and s[1].isalpha():
        string_conditions = True

    for char in s:
        if char.isdigit():
            counter += 1
        if char in string.punctuation or (char == "0" and counter == 1) or (counter > 0 and not s[-1].isdigit()) or (counter > 0and char.isalpha()):
            char_conditions = False

    if string_conditions and char_conditions:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
