MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}
# Day 15 of 100 Days Of Code: The Complete Python Pro Bootcamp
# extra commands: off, report and refill
penny = 0.01
nickel = 0.05
dime = 0.1
quarter = 0.25
on = True
print('The coffees are espresso, latte and cappuccino')
print('espresso = $1.5, latte = $2.5, cappuccino = $3')
response = str(input('What coffee would you like?')).lower()


def find_resources():
    # basically it is just to get the values of the ingredients on dict. "MENU"
    # espresso requires an especial action due to it not using milk
    if response == "espresso":
        coffee_ingredients = MENU[response]
        coffee_ingredients = coffee_ingredients["ingredients"]
        coffee_ingredients = coffee_ingredients["water"], coffee_ingredients["coffee"]
        return coffee_ingredients
    elif response == "cappuccino" or response == "latte":
        coffee_ingredients = MENU[response]
        coffee_ingredients = coffee_ingredients["ingredients"]
        coffee_ingredients = coffee_ingredients["water"], coffee_ingredients["milk"], coffee_ingredients["coffee"]
        return coffee_ingredients


def pay():
    total_money = MENU[response]
    total_money = total_money["cost"]
    try:
        total_quarters = float(quarter * float((input("How many quarters?"))))
        total_dimes = float(dime * float((input("How many Dimes?"))))
        total_nickels = float(nickel * float(input("How many nickels?")))
        total_penny = float(penny * float(input("How many Penny's?")))
        all_given = total_penny + total_quarters + total_dimes + total_nickels
        total = all_given - total_money
        print(total)
        # getting change
        if total == 0:
            print('Operation made successfully')
        elif total < 0:
            print('You need more money.')
            pay()
            # Repeat
        elif total < total_money:
            print(f"here is your change: {total}")
    except ValueError:
        print('Not valid')
        pay()
        # If somone puts a string like "one" or "two"
        # print('Not valid')



def use_resources():
    ingredients_list = find_resources()
    print(resources)
    # comparing ingredients
    # if not enough the program return False, else it will return True
    if response == "espresso":
        if resources["water"] < ingredients_list[0]:
            print('not enough water')
            return False

        elif resources['coffee'] < ingredients_list[1]:
            print('Not enough coffee')
            return False
        else:
            resources["water"] -= ingredients_list[0]
            resources['coffee'] -= ingredients_list[1]
            return True

    elif response == "latte" or response == "cappuccino":
        if resources['water'] < ingredients_list[0]:
            print('not enough water')
            return False
        elif resources['milk'] < ingredients_list[1]:
            print('Not enough milk')
            return False
        elif resources['coffee'] < ingredients_list[2]:
            print('Not enough coffee')
            return False
        else:
            resources["water"] -= ingredients_list[0]
            resources["milk"] -= ingredients_list[1]
            resources["coffee"] -= ingredients_list[2]
            return True

while on:
    # Secret codes for mainteinance
    if response == 'report':
        print(resources)
    elif next == 'refill':
        resources["water"] = 300
        resources['milk'] = 200
        resources['coffee'] = 100
        print(f'Resources filled: {resources}')
        print('Turning off machine to reset')
        on = False
    elif response == "report":
        print(resources)
        on = False
    elif response == "off":
        print('MANUAL OFF TRIGGERED, TURNING OFF SYSTEM.')
        break

        for n in resources:
            resource = str((resources[n]))
            print(f'{n}: {resource}')
        response = str(input('What coffee would you like?')).lower()
    if use_resources():
        pay()
        # Even if use_resources() is in an if statement it still gets called
    else:
        # terminate program when not enough resources
        break

    next = input('Anything else?, need another coffee? type "y" or "n"').lower()
    if next == "y":
        response = str(input('What coffee would you like?')).lower()

    elif next == "n":
        on = False
    elif next == 'refill':
        resources["water"] = 300
        resources['milk'] = 200
        resources['coffee'] = 100
        print(f'Resources filled: {resources}')
        print('Turning off machine to reset')
        on = False
    elif next == "report":
        print(resources)
        on = False
    elif next == "off":
        print('MANUAL OFF TRIGGERED, TURNING OFF SYSTEM.')
        on = False
