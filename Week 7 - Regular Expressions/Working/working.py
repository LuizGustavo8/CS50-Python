import re

def convert(s):
    # Expressão regular para capturar o horário no formato 12 horas
    match = re.match(r"(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)", s)

    if not match:
        raise ValueError("Invalid time format")

    # Extraindo horas, minutos e AM/PM
    h1, m1, am_pm1, h2, m2, am_pm2 = match.groups()

    # Verificando se horas e minutos são válidos
    if not (1 <= int(h1) <= 12) or (m1 and not (0 <= int(m1) < 60)):
        raise ValueError("Invalid hour or minute for start time")
    if not (1 <= int(h2) <= 12) or (m2 and not (0 <= int(m2) < 60)):
        raise ValueError("Invalid hour or minute for end time")

    def to_24_hour(h, m, am_pm):
        h = int(h)
        m = int(m) if m else 0
        if am_pm == "PM" and h != 12:
            h += 12
        elif am_pm == "AM" and h == 12:
            h = 0
        return f"{h:02}:{m:02}"

    start_time = to_24_hour(h1, m1, am_pm1)
    end_time = to_24_hour(h2, m2, am_pm2)

    return f"{start_time} to {end_time}"

def main():
    print(convert(input("Hours: ")))

if __name__ == "__main__":
    main()
