def main():
  fraction = input("Fraction: ")
  try:
      percentage = convert(fraction)
      print(gauge(percentage))
  except (ValueError, ZeroDivisionError) as e:
      print(f"Error: {e}")

def convert(fraction):
  try:
      x, y = fraction.split("/")
      x = int(x)
      y = int(y)
  except ValueError:
      raise ValueError("X and Y must be integers")

  if y == 0:
      raise ZeroDivisionError("Y cannot be zero")

  if x > y:
      raise ValueError("X cannot be greater than Y")

  percentage = round((x / y) * 100)
  return percentage

def gauge(percentage):
  if percentage <= 1:
      return "E"
  elif percentage >= 99:
      return "F"
  else:
      return f"{percentage}%"

if __name__ == "__main__":
  main()
