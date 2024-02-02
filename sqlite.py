import sqlite3


def create_table():
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    try:
        c.execute("""CREATE TABLE IF NOT EXISTS users (
            first text,
            last text,
            taxable real,
            total_income real,
            tax real
            )""")
        conn.commit()
        conn.close()
    except sqlite3.OperationalError as e:
        print(f"Table creation failed: {e}")


def add_user(user):
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES (:first, :last, :taxable_amount :total_income, :tax)",
              (user.first, user.last, user.taxable_amount, user.total_income, user.tax))
    conn.commit()
    conn.close()

def update_user_income(first_name, last_name, new_income):
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    c.execute("UPDATE users SET total_income = ?, tax = ? WHERE first = ? AND last = ?",
              (new_income, round((new_income - 12750) * 0.0475, 2), first_name, last_name))

    conn.commit()
    conn.close()

def display_table():
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    rows = c.fetchall()

    for row in rows:
        print(row)
    conn.close()
