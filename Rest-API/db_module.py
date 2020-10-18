import sqlite3


def create():
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    create_query = "CREATE TABLE users (id TEXT, password TEXT)"
    cur.execute(create_query)
    conn.commit()
    conn.close()

def insert(id_,pass_):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    insert_query = "INSERT INTO users VALUES(?,?)"
    cur.execute(insert_query,(id_,pass_))
    conn.commit()
    conn.close()

def select():
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    select_query = 'SELECT * FROM users'
    cur.execute(select_query)
    result = cur.fetchall()
    conn.close()
    return result

def logincheck(id_,password_):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    select_query = 'SELECT * FROM users WHERE id =? and password =?'
    cur.execute(select_query,(id_,password_))
    result = cur.fetchall()
    conn.close()
    return result


def update(id_,pass_):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    update_query = "UPDATE users SET password =? WHERE id =?"
    cur.execute(update_query,(pass_,id_))
    conn.commit()
    conn.close()

# create()
# insert('Girish',1234)
# insert('Anshul',5678)

# print(select())
# print(logincheck('Girish',1234))
# print(logincheck('Anshul',1234))
