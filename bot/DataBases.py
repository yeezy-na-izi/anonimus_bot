import sqlite3


def data_add_users(user, id):
    conn = sqlite3.connect('bot.db')
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS user(
       name TEXT,
       surname TEXT,
       about_user TEXT,
       gender BLOB,
       chat_id INTEGER,
       looking_for BLOB);
    """)
    conn.commit()
    if prof_show(id):
        cur.execute(f"DELETE FROM user WHERE chat_id='{id}';")
        conn.commit()
    cur.execute(f"INSERT INTO user(name, surname, about_user, gender, chat_id, looking_for) "
                f"VALUES('{user[0]}','{user[1]}', '{user[2]}', '{user[3]}', '{id}', 'False');")
    conn.commit()


def prof_show(id):
    try:
        conn = sqlite3.connect('bot.db')
        cur = conn.cursor()
        cur.execute(f"select * from user where chat_id='{id}'")
        gag = cur.fetchall()[0]
        return gag
    except:
        return []
