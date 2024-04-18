def main():

    valid_coins = [5,10,25]

    amount = 50
    print(f"Amount Due: {amount}")

    while (amount > 0):
        value = int(input("Insert Coin: "))
        if value in valid_coins:
            amount = amount - value
            if amount > 0:
                 print(f"Amount Due: {amount}")
            else:
                 print(f"Change Owed: {abs(amount)}")
        else:
            print(f"Amount Due: {amount}")





if __name__ == "__main__":
    main()
