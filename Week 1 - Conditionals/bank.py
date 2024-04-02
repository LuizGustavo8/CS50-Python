awnser = input("Greeting: ").lower().strip()

first_letter = awnser[0]


if(awnser[0:5] == "hello"):
    print("$0")

elif(first_letter == "h"):
    print("$20")

else:
    print("$100")