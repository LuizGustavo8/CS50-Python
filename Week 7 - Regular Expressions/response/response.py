from validator_collection import validators, errors

def main():
    print(validate_email(input("What's your email address? ")))

def validate_email(s):

    try:
        if validators.email(s):
            return "Valid"

    except errors.InvalidEmailError:
        return "Invalid"



if __name__ == "__main__":
    main()

