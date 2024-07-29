import re


def main():
    print(count(input("Text: ")))


def count(s):
    counter = len((re.findall(r"\b[uU][mM]\b", s)))

    return int(counter)

if __name__ == "__main__":
    main()
