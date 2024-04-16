def main():
  string = input("camelCase: ")
  snake = []  # Lista para acumular os caracteres
  counter = 0
  for char in string:
      if char.isupper():
          # Adiciona um sublinhado seguido do caractere em minúsculo à lista
          snake.append("_" + char.lower())
          counter += 1
      else:
          # Adiciona o caractere à lista
          snake.append(char)

  # Junta todos os caracteres da lista em uma única string
  snake = "".join(snake)

  if counter > 0:
      # Se houve substituições, remove o primeiro sublinhado
      snake = snake.lstrip("_")
      print("snakeCase: " + snake)
  else:
      print("snakeCase: " + string)

if __name__ == "__main__":
  main()

