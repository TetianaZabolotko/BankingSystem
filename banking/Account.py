import random
from Queries import Queries


class Account:
    def __init__(self, database):
        self.database = database
        self.id = None
        self.card_number = None
        self.pin = None
        self.balance = 0

    def set_info(self, id_, card_number, pin, balance):
        self.id = id_
        self.card_number = card_number
        self.pin = pin
        self.balance = balance

    @staticmethod
    def generate_card_number():
        sequence = list('400000') + random.sample('0123456789', 9)
        return Account.luhn_algorithm(sequence)

    @staticmethod
    def luhn_algorithm(seq_origin):
        seq_modified = list(map(int, seq_origin))
        for n, let in enumerate(seq_modified):
            if n % 2 == 0:
                if int(let)*2 - 9 > 0:
                    seq_modified[n] = int(let) * 2 - 9
                else:
                    seq_modified[n] = int(let) * 2

        remainder = sum(seq_modified) % 10
        last_el = 0 if remainder == 0 else 10 - remainder

        return ''.join(seq_origin) + str(last_el)

    @staticmethod
    def generate_pin_number():
        return ''.join(random.sample('123456789', 4))

    def account_menu(self):
        while True:
            print('1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n5. Log out\n0. Exit')
            choice = input()
            if choice == '1':
                print(f"\nBalance: {self.balance}\n")
            elif choice == '2':
                self.add_income()
            elif choice == '3':
                self.transfer_money()
            elif choice == '4':
                self.delete_account()
            elif choice == '5':
                print('\nYou have successfully logged out!\n')
                return
            elif choice == '0':
                self.database.cur.close()
                self.database.connection.close()
                print('\nBye!')
                exit()
            else:
                print('Unknown option.\n')

    def add_income(self):
        income = int(input('\nEnter income:\n'))
        self.balance += income
        balance_card_num = (self.balance, self.card_number)
        self.database.update_table(Queries.UPDATE_BALANCE, balance_card_num)
        print('Income was Added\n')

    def transfer_money(self):
        print('\nTransfer')
        receiver_card_num = input('Enter card number:\n')
        if receiver_card_num != self.card_number:
            if Account.luhn_algorithm(receiver_card_num[:-1]) == receiver_card_num:
                record = self.database.get_by_card_num(Queries.SELECT_BY_CARD_NUM, receiver_card_num)
                if record is not None:
                    transfer_money_amount = int(input('Enter how much money you want to transfer:\n'))
                    if transfer_money_amount < self.balance:
                        balance_card_receiver = record[3] + transfer_money_amount
                        balance_card_num_receiver = (balance_card_receiver, record[1])
                        self.database.update_table(Queries.UPDATE_BALANCE, balance_card_num_receiver)
                        self.balance = self.balance - transfer_money_amount
                        balance_card_num = (self.balance, self.card_number)
                        self.database.update_table(Queries.UPDATE_BALANCE, balance_card_num)
                        print('\nSuccess\n')
                    else:
                        print('\nNot enough money!\n')
                else:
                    print('\nSuch a card does not exist\n')
            else:
                print('Probably you made a mistake in the card number. Please try again!\n')
        else:
            print("\nYou can't transfer money to the same account!\n")

    def create_account(self):
        self.card_number = self.generate_card_number()
        self.pin = self.generate_pin_number()
        print(f'\nYour card has been created \nYour card number: \n{self.card_number}')
        print(f'Your card PIN: \n{self.pin}\n')

    def delete_account(self):
        self.database.delete_by_card_num(Queries.DELETE_FROM_BY_CARD_NUM, self.card_number)
        print('The account has been closed!')
        return