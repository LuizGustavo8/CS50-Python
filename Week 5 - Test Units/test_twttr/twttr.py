def main():


    string = input("Input: ")

    str = shorten(string)

    print(f"Output: {str}")

def shorten(string):
    vogal = ["a","e","i","o","u"]
    copy = []

    for char in string:
        if not char.lower() in vogal :
            copy.append(char)

    return "".join(copy)

if __name__ == "__main__":
    main()


