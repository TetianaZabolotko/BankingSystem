import sqlite3
from sqlite3 import Error


class DataBase:
    def __init__(self):
        self.connection = None
        self.cur = None

    def create_connection(self, db_file):
        try:
            self.connection = sqlite3.connect(db_file)
            if self.connection is not None:
                self.cur = self.connection.cursor()
            else:
                print("Error! cannot create the database connection.")
        except Error as e:
            print(e)

    def create_table(self, create_query):
        try:
            self.cur.execute(create_query)
            self.connection.commit()
        except Error as e:
            print(e)

    def insert(self, insert_query, account_info):
        try:
            self.cur.execute(insert_query, account_info)
            self.connection.commit()
        except Error as e:
            print(e)

    def select_all(self, select_query):
        try:
            self.cur.execute(select_query)
            return self.cur.fetchall()
        except Error as e:
            print(e)
        return None

    def select_by_credentials(self, select_query, credentials):
        try:
            self.cur.execute(select_query, credentials)
            return self.cur.fetchone()
        except Error as e:
            print(e)
        return None

    def get_by_card_num(self, select_by_card_num, num):
        try:
            self.cur.execute(select_by_card_num, (num,))
            return self.cur.fetchone()
        except Error as e:
            print(e)
        return None

    def delete_by_card_num(self, del_query, num):
        try:
            self.cur.execute(del_query, (num,))
            self.connection.commit()
        except Error as e:
            print(e)

    def delete_table(self, del_query):
        try:
            self.cur.execute(del_query)
            self.connection.commit()
        except Error as e:
            print(e)

    def delete_database(self, del_query):
        try:
            self.cur.execute(del_query)
            self.connection.commit()
        except Error as e:
            print(e)

    def update_table(self, update_query, balance_num):
        try:
            self.cur.execute(update_query, balance_num)
            self.connection.commit()
        except Error as e:
            print(e)