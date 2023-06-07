import sqlite3

conn = sqlite3.connect('Main.db')
print("Opened database successfully")

conn.execute('CREATE TABLE Teams (Team_ID INTEGER PRIMARY KEY, Team_Name VARCHAR(50))')
conn.execute('CREATE TABLE Player (Player_ID INTEGER PRIMARY KEY, Team_ID INTEGER, Position VARCHAR(20), Height INTEGER, FIRST_NAME VARCHAR(50), LAST_NAME VARCHAR(50), FOREIGN KEY (Team_ID) REFERENCES Teams(Team_ID))')

print("Table created successfully")

conn.close()