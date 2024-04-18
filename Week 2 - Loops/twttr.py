def main():
  string = input("Input: ")
  vogal = ["a","e","i","o","u"]
  copy = []

  for char in string:
      if not char.lower() in vogal :
          copy.append(char)

  copy = "".join(copy)

  print(f"Output: {copy}")

if __name__ == "__main__":
  main()


