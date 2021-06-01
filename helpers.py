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
            deposit_amount = float(input("Please enter deposit amount to deposit\n-->"))
            return deposit_amount
        except ValueError:
            print("Amount has to be a number-example(125.45, 100.....")
