import inflect

p = inflect.engine()
names =[]

def main():

    while True:
        try:
            names.append(input("Name: ").strip())
        except EOFError:
            break

    print(f"Adieu, adieu, to {p.join(names)}")

if __name__ == "__main__":
    main()
