import sqlite3
import time 
import datetime
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style
style.use('fivethirtyeight')

# The below code is used to connect to mysql
# mydb = mysql.connector.connect(
#     host = "localhost",
#     user = "usr",
#     passwd = "pwd",
#     db = "testdb",
#     port = 1234

# )

# Connection to database
conn = sqlite3.connect("test.db")

# Connection cursor
c = conn.cursor()

# Function to create table
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS table1(unix REAL, datestamp TEXT, keyword TEXT, value REAL)')

# Enter data into the table
def data_entry():
    c.execute('INSERT INTO table1 VALUES(12345678, "2016-01-01", "Python", 5)')
    conn.commit() # every change in the database needs to be commited 
    # c.close()
    # conn.close()

# Populate data in the database dynamically
def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Python'
    value = random.randrange(0,10)
    c.execute("INSERT INTO table1 (unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)",
    (unix, date, keyword, value))
    conn.commit()

# Read from database - queries
def read_from_db():
    c.execute('SELECT keyword, unix FROM table1 WHERE value=3 AND keyword="Python"')
    data = c.fetchall()
    for row in data:
        print(row) # Each row is a tuple 

# PLot from database 
def graph_data():
    c.execute('SELECT unix, value FROM table1')
    dates = []
    values = []
    data = c.fetchall()
    for row in data:
        print(row[0])
        print(datetime.datetime.fromtimestamp(row[0]))
        dates.append(datetime.datetime.fromtimestamp(row[0]))
        values.append(row[1])
    
    plt.plot(dates, values, '-')
    plt.show()    

# Update data in the database
def update_db():
    c.execute('SELECT * FROM table1')
    [print(row) for row in c.fetchall()]
    print(50 * '#')
    c.execute('UPDATE table1 SET value = 99 WHERE value= 4')
    conn.commit()
    c.execute('SELECT * FROM table1')
    [print(row) for row in c.fetchall()]

def del_db():
    c.execute('DELETE FROM table1 WHERE value = 99')
    conn.commit()


# create_table()
# data_entry()
# for i in range(10):
#     dynamic_data_entry()
#     time.sleep(1)

# read_from_db()
# graph_data()
# update_db()
# del_db()

c.close()
conn.close()