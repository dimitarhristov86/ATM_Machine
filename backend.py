from clients import CLIENTS
from helpers import pin_validation, get_withdraw, get_deposit

print(30 * "-")
print()
print("Welcome to BULGARIAN ATM MACHINES")
print()
print(30 * "-")


def main_menu():
    name_input = input("Please enter your name\n-->").lower()

    if CLIENTS.get(name_input):
        client = CLIENTS.get(name_input)
        if pin_validation(client):
            balance = client["balance"]
            print(f"Your balance is {balance}")
            action = input("Please chose an action using code reference(1,2,3)"
                           "\n1.Withdraw\n2.Deposit\n3.View balance\n-->")
            if action == "1":
                withdraw_amount = get_withdraw(balance)
                new_balance = balance - withdraw_amount
                CLIENTS[f"{client}"][f"{balance}"] = [f"{new_balance}"]
                print(f"You just withdraw {withdraw_amount}lv.\nYour new balance is {new_balance}lv")
            elif action == "2":
                deposit_amount = get_deposit(balance)
                new_balance = balance + deposit_amount
                print(f"You just deposit {deposit_amount}lv\nYour new balance is {new_balance}lv")
            elif action == "3":
                print(f"Your balance is {balance}lv")
    else:
        print(f"No such client {name_input}")
