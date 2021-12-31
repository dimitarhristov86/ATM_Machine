def pin_validation(client):
    tries = 3
    for x in range(3):
        user_pin = input("Please enter pin\n-->")
        if user_pin == client["pin"]:
            return True
        elif user_pin != client["pin"]:
            tries -= 1
            print(f"Wrong pin, you have {tries} tries left")
    else:
        print("Your card is blocked, please contact your bank")
        return False


def get_withdraw(balance):
    while True:
        try:
            withdraw_amount = float(input("Please enter withdraw amount\n-->"))
            if withdraw_amount <= balance:
                return withdraw_amount
            else:
                print(f"You don't have enough money!Your balance is {balance}.Try again")
        except ValueError:
            print("Amount has to be a numbers:(example-125.25, 100....")


def get_deposit(balance):
    while True:
        try:
            deposit_amount = float(input("Please enter amount to deposit in your bank account\n-->"))
            return deposit_amount
        except ValueError:
            print("Amount has to be a number-example(125.45, 100.....")


def welcome_note():
    print(30 * "-")
    print()
    print("WELCOME TO BULGARIAN ATM MACHINES")
    print()
    print(30 * "-")


def entry_log():
    while True:
        try:
            entry_action = int(input("Do you want to continue?\n1.YES\n2.NO\n-->"))
            if entry_action == 1:
                return True
                pass
            elif entry_action == 2:
                print("Thank you for visiting us! Have a nice day! ")
                exit()
            elif entry_action >= 3:
                print("Action has to be a number(1 or 2), try again!")
        except ValueError:
            print("Action has to be a number(1 or 2), try again!")
