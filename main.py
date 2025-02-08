def main() -> None:
    while True:
        try:
            user_input = input('Enter the cost: ')
            if user_input == 'exit':
                break
            cost = float(user_input)
            user_input = input('Enter the amount of money given: ')
            money_given = float(user_input)
        except ValueError:
            print('Enter a floating-point value!')
            continue

        change = round(money_given - cost, 2)
        if change < 0:
            print('Cost should be at most equal to amount of money given!')
            continue

        diff = change
        num_of_quarters = 0
        num_of_dimes = 0
        num_of_nickels = 0
        num_of_pennies = 0
        while diff > 0:
            if (diff-0.25) >= 0:
                diff = round(diff - 0.25, 2)
                num_of_quarters += 1
            elif (diff-0.10) >= 0:
                diff = round(diff - 0.10, 2)
                num_of_dimes += 1
            elif (diff-0.05) >= 0:
                diff = round(diff - 0.05, 2)
                num_of_nickels += 1
            elif (diff-0.01) >= 0:
                diff = round(diff - 0.01, 2)
                num_of_pennies += 1
        print(f'The change is ${change:.2f}.')
        print(f'{num_of_quarters} quarters, {num_of_dimes} dimes, {num_of_nickels} nickels, and {num_of_pennies} pennies are required for this change.')


if __name__ == '__main__':
    main()
