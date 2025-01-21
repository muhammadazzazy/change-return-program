cost_str = input('Enter the cost: ')

while cost_str[0] != '$':
    cost_str = input('Enter the cost: ')

cost = float(cost_str[1:])

money_str = input('Enter the amount of money given: ')
while money_str[0] != '$':
    money_str = input('Enter the amount of money given: ')

money_given = float(money_str[1:])

while cost > money_given:
    cost_str = input('Enter the cost: ')
    money_str = input('Enter the amount of money given: ')
    while cost_str[0] != '$':
        cost_str = input('Enter the cost: ')
    cost = float(cost_str[1:])
    while money_str[0] != '$':
        money_str = input('Enter the amount of money given: ')
    money_given = float(money_str[1:])

cost = float(cost_str[1:])
money_given = float(money_str[1:])

change = round(money_given - cost, 2)
diff = change
num_of_quarters = 0
num_of_dimes = 0
num_of_nickels = 0
num_of_pennies = 0

while diff > 0:
    if (diff-0.25) >= 0:
        diff = round(diff - 0.25, 2)
        num_of_quarters+=1
    elif (diff-0.10) >= 0:
        diff = round(diff - 0.10, 2)
        num_of_dimes+=1
    elif (diff-0.05) >= 0:
        diff = round(diff - 0.05, 2)
        num_of_nickels+=1
    elif (diff-0.01) >= 0:
        diff = round(diff - 0.01, 2)
        num_of_pennies+=1

print(f'The change is ${change:.2f}.')
print(f'{num_of_quarters} quarters, {num_of_dimes} dimes, {num_of_nickels} nickels, and {num_of_pennies} pennies are required for this change.')
