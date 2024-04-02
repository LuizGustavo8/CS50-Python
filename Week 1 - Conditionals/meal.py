def main():
    time = input("What time is it? ")

    float_time = convert(time)

    if 7 <= float_time < 8:
        print("breakfast time")
    elif float_time > 18:
        print("dinner time")
    elif float_time > 12:
        print("lunch time")

def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes) /60
    return hours + minutes


if __name__ == "__main__":
    main()
