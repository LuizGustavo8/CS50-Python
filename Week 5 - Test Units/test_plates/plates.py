def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Check if length is between 2 and 6 characters
    if not (2 <= len(s) <= 6):
        return False

    # Check if the first two characters are letters
    if not s[:2].isalpha():
        return False

    # Check for invalid characters
    if not s.isalnum():
        return False

    # Check that any numbers are at the end
    num_started = False
    for char in s:
        if char.isdigit():
            if char == '0' and not num_started:
                return False
            num_started = True
        elif num_started:
            return False

    return True

if __name__ == "__main__":
    main()
