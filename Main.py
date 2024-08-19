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
    "coffee": 100,
}
# Day 15 of 100 Days Of Code: The Complete Python Pro Bootcamp
# sorry, didn't know that I needed to save my projects to upload it, i did more, but it got deleted since
# "unnecessary". Sorry, I'm Non-english native speaker, sorry if my english is bad
# took me 5 days, this was the hardest one
penny = 0.01
nickel = 0.05
dime = 0.1
quarter = 0.25
global on
on = True
print('The coffees are espresso, latte and cappuccino')
print('espresso = $1.5, latte = $2.5, cappuccino = $3')
response = str(input('What coffee would you like?')).lower()
while on:



    def find_resources():
        # basically it is just to get the values of the ingredients on dict. "MENU"
        # The positional argument was removed because it was not important, removed for make the code to read easier
        if response == "espresso":
            coffee_ingredients = MENU[response]
            coffee_ingredients = coffee_ingredients["ingredients"]
            coffee_ingredients = coffee_ingredients["water"], coffee_ingredients["coffee"]
            return coffee_ingredients
        elif response == "cappuccino" or "latte":
            coffee_ingredients = MENU[response]
            coffee_ingredients = coffee_ingredients["ingredients"]
            coffee_ingredients = coffee_ingredients["water"], coffee_ingredients["milk"], coffee_ingredients["coffee"]
            return coffee_ingredients

    if response == 'report':
        # for maintenance
        for n in resources:
            resource = str((resources[n]))
            print(f'{n}: {resource}')
        response = str(input('What coffee would you like?')).lower()

    find_resources()
    def use_resources():
        global on
        # comparing ingredients
        if response == "espresso":
            if resources["water"] < find_resources()[0]:
                print('not enough water')
                on = False

            elif resources['coffee'] < find_resources()[1]:
                on = False
                print('Not enough coffee')
            else:
                resources["water"] = - find_resources()[0]
                resources['coffee'] = - find_resources()[1]
        elif response == "latte" or "cappuccino":
            if resources['water'] < find_resources()[0]:
                print('not enough water')
                on = False
            elif resources['milk'] < find_resources()[1]:
                on = False
                print('Not enough milk')
            elif resources['coffee'] < find_resources()[2]:
                on = False
                print('Not enough coffee')
            else:
                # asked for help for this, my original code was basically the same but was like in line 68, moved it
                resources["water"] = - find_resources()[0]
                resources["milk"] = - find_resources()[1]
                resources["coffee"] = - find_resources()[2]




    def pay():
        total_money = MENU[response]
        total_money = total_money["cost"]
        try:
            total_quarters = float(quarter * float((input("How many quarters?"))))
            total_dimes = float(dime * float((input("How many Dimes?"))))
            total_nickels = float(nickel * float(input("How many nickels?")))
            total_penny = float(penny * float(input("How many Penny's?")))
            all_given = total_penny +  total_quarters + total_dimes + total_nickels
            total = all_given - total_money
            print(total)
            # getting change
            if total == 0:
                print('Operation made successfully')
            if total < 0:
                print('You need more money.')
                pay()
                # Repeat
            elif total < total_money:
                print(f"here is your change: {total}")
        except ValueError:
            print('Not valid')
            pay()


    use_resources()
    if on == True:
        pay()
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
    elif next == "report":
        print(resources)
        on = False
    elif next == "off":
        print('MANUAL OFF TRIGGERED, TURNING OFF SYSTEM.')
        on = False
    # extra commands: off, report and refill