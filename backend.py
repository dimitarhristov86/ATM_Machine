import time
from clients import CLIENTS
from helpers import pin_validation, get_withdraw, get_deposit, entry_log, welcome_note

welcome_note()
entry_log()


def main_menu():
    while True:
        name_input = input("Please enter your name\n-->").lower()
        if CLIENTS.get(name_input):
            client = CLIENTS.get(name_input)
            if pin_validation(client):
                balance = client["balance"]
                time.sleep(1)
                print(f"Your balance is {balance:.2f}")
                action = input("Please chose an action using code reference(1,2,3)"
                               "\n1.Withdraw\n2.Deposit\n3.View balance\n4.Logout\n-->")
                if action == "1":
                    withdraw_amount = get_withdraw(balance)
                    new_balance = balance - withdraw_amount
                    print(f"You just withdraw {withdraw_amount:.2f}lv.\nYour new balance is {new_balance:.2f}lv")
                    entry_log()
                elif action == "2":
                    deposit_amount = get_deposit(balance)
                    new_balance = balance + deposit_amount
                    print(f"You just deposit {deposit_amount:.2f}lv\nYour new balance is {new_balance:.2f}lv")
                    entry_log()
                elif action == "3":
                    print(f"Your balance is {balance:.2f}lv")
                    time.sleep(3)
                    entry_log()
                elif action == "4":
                    entry_log()
                else:
                    print("Wrong key reference, try again! ")
                    time.sleep(1)
                    entry_log()
        else:
            print(f"No such client {name_input}")
            print("Try again! ")
            time.sleep(1)
            entry_log()
