class Queries:
    DATABASE = 'card.s3db'

    TABLE_NAME = 'card'

    CREATE_TABLE = 'CREATE TABLE IF NOT EXISTS ' + TABLE_NAME + """(
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    number TEXT NOT NULL UNIQUE,
                    pin TEXT NOT NULL,
                    balance INTEGER DEFAULT 0 NOT NULL
                    );"""
    INSERT_QUERY = 'INSERT INTO ' + TABLE_NAME + ' (number, pin, balance) VALUES(?,?,?)'
    SELECT_QUERY = 'SELECT * FROM ' + TABLE_NAME
    SELECT_BY_ID_QUERY = 'SELECT * FROM ' + TABLE_NAME + ' WHERE id ='
    SELECT_BY_CREDENTIALS = 'SELECT * FROM ' + TABLE_NAME + ' WHERE pin = ? AND number= ?'
    SELECT_BY_CARD_NUM = 'SELECT * FROM ' + TABLE_NAME + ' WHERE number = ?'
    DELETE_FROM_DT = 'DELETE FROM ' + TABLE_NAME
    DELETE_FROM_BY_CARD_NUM = 'DELETE FROM ' + TABLE_NAME + ' WHERE number = ?'
    DELETE_TABLE = 'DROP TABLE ' + TABLE_NAME
    DELETE_DATABASE = 'DROP DATABASE card'
    UPDATE_BALANCE = 'UPDATE ' + TABLE_NAME + ' SET balance = ? WHERE number = ?'
