MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "money": 0,
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
    "money": 0,
}

report = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
        "money": 0,
}

should_continue = True

while should_continue:
    def resources_checker(option):
        for key in MENU:
            if key == option:
                availability = ""
                for items in resources and MENU[option]["ingredients"]:
                    if resources[items] < MENU[option]["ingredients"][items]:
                        availability = items
                        print(f"Sorry there isn't enough {availability}")
                        return 0

        return 1
    def money_processor():
        if resources_checker(option=options) == 1:
            print("Please insert coin.")
            quarters = 0.25
            dimes = 0.10
            nickles = 0.05
            pennies = 0.01

            quarter = float(input("How many quarters?: "))
            dime = float(input("How many dimes?: "))
            nickle = float(input("How many nickles?: "))
            pennie = float(input("How many pennies?: "))

            total_amount = round(float(quarter + dime + nickle + pennie))
            return total_amount
    def transaction_verification():
        actual_money = MENU[options]["cost"]
        inserted_money = money_processor()

        if inserted_money < actual_money:
            print(f"Sorry that's not enough money. Money refunded {inserted_money}$💸")
            return 0
        elif inserted_money == actual_money:
            report['money'] += actual_money
            print(f"Here is your {options} enjoy☕️")
            return 1
        elif inserted_money > actual_money:
            report['money'] += actual_money
            refund = inserted_money - actual_money
            print(f"Here is {refund}$ in change 💸")
            print(f"Here is your {options} enjoy☕️")
            return 1

    def make_coffee():
        if transaction_verification() == 1:
            ingredients = MENU[options]["ingredients"]

            for item in ingredients:
                report[item] -= ingredients[item]

    options = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if options == "off":
        print("Machine is shutting down...⏳")
        should_continue = False
    elif options == "report":
        for item in report:
            print("Here is the report ⚠")
            print(f"{item}: {report[item]}")
        should_continue = False
    elif options in MENU:
        make_coffee()
    else:
        print("Wrong choice")
        should_continue = False
