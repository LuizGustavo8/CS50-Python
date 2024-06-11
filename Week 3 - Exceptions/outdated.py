months = [
  "January", "February", "March", "April", "May", "June",
  "July", "August", "September", "October", "November", "December"
]

def parse_date(date_str):
  # Try to handle the numeric format first
  if '/' in date_str:
      parts = date_str.split('/')
      if len(parts) == 3:
          month, day, year = parts
          try:
              month = int(month)
              day = int(day)
              year = int(year)
              if 1 <= month <= 12 and 1 <= day <= 31:
                  return f"{year:04}-{month:02}-{day:02}"
          except ValueError:
              pass
  # Try to handle the textual format next
  else:
      for month in months:
          if date_str.startswith(month):
              parts = date_str[len(month):].strip().split(',')
              if len(parts) == 2:
                  day, year = parts
                  try:
                      day = int(day.strip())
                      year = int(year.strip())
                      month_index = months.index(month) + 1
                      if 1 <= day <= 31:
                          return f"{year:04}-{month_index:02}-{day:02}"
                  except ValueError:
                      pass
  return None

def main():
  while True:
      date_str = input("Date: ").strip()
      iso_date = parse_date(date_str)
      if iso_date:
          print(iso_date)
          break
      else:
          print("Invalid date format. Please try again.")

if __name__ == "__main__":
  main()
