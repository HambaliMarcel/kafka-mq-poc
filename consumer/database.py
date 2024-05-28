import sqlite3

def create_connection(db_file):
    conn = sqlite3.connect(db_file)
    return conn

def create_table(conn):
    sql_create_messages_table = """
    CREATE TABLE IF NOT EXISTS messages (
        id integer PRIMARY KEY,
        type text NOT NULL,
        user_id text,
        action text,
        timestamp real
    );"""
    try:
        c = conn.cursor()
        c.execute(sql_create_messages_table)
    except Exception as e:
        print(e)

def insert_message(conn, message):
    sql = ''' INSERT INTO messages(type, user_id, action, timestamp)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, (message['type'], message['user_id'], message['action'], message['timestamp']))
    conn.commit()
    return cur.lastrowid
