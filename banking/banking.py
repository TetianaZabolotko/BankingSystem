from Account import Account
from DataBase import DataBase
from Queries import Queries


class BankingSystem:
    def __init__(self):
        self.database = DataBase()
        self.database.create_connection(Queries.DATABASE)
        self.database.create_table(Queries.CREATE_TABLE)

    def login(self):
        card_num_input = input('\nEnter your card number:\n')
        pin_input = input('Enter your pin:\n')
        credentials = (pin_input, card_num_input)
        record = self.database.select_by_credentials(Queries.SELECT_BY_CREDENTIALS, credentials)
        if record is not None:
            print('\nYou have successfully logged in!\n')
            account = Account(self.database)
            account.set_info(record[0], record[1], record[2], record[3])
            account.account_menu()
        else:
            print('\nWrong card number or PIN!\n')

    def menu(self):
        while True:
            print('1.Create an account \n2.Log into account \n0.Exit')
            choice = input()
            if choice == '1':
                account = Account(self.database)
                account.create_account()
                card = (account.card_number, account.pin, account.balance)
                self.database.insert(Queries.INSERT_QUERY, card)
            elif choice == '2':
                self.login()
            elif choice == '0':
                self.database.cur.close()
                self.database.connection.close()
                print('\nBye!')
                exit()
            else:
                print('Unknown option.')


BankingSystem().menu()

