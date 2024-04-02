awnser = input("Expression: ").split(" ")

match awnser[1]:
    case "+":
        print(float(awnser[0]) + float(awnser[2]))
    case "-":
        print(float(awnser[0]) - float(awnser[2]))
    case "*":
        print(float(awnser[0]) * float(awnser[2]))
    case "/":
        print(float(awnser[0]) / float(awnser[2]))