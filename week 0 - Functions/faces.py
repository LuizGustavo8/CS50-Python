input = input()

words = input.split(" ")

for word in words:
    if(word == ":)"):
        print("🙂", end=" ")
    elif(word == ":("):
        print("🙁", end=" ")
    else:
        print(word, end=" ")
print("")
