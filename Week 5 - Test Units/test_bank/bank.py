def main():
    awnser = (input("Greeting: ")).lower().strip()

    print(f"${value(awnser)}")

def value(greeting):

        first_letter = greeting[0]

        if(greeting[0:5] == "hello"):
            return 0

        elif(first_letter == "h"):
            return 20

        else:
            return 100


if __name__ == "__main__":
    main()
