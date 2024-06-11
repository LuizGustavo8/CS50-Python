def main():
  while True:
      try:
          fraction = input("Fraction:")
          numerator, denominator = map(int, fraction.split('/'))
          percentage = round((numerator / denominator) * 100)
      except (ValueError, ZeroDivisionError):
          ...
      else:
          if percentage > 100:
              ...
          else:
              break

  if percentage <= 1:
       print("E")
  elif percentage >= 99:
       print("F")
  else:
       print(f"{percentage}%")



if __name__ == "__main__":
  main()
