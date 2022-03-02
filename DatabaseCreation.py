#Importing the sqlite module
import sqlite3

#Created a database if one doesn't exist, opens it if one does
conn = sqlite3.connect('LeaderBoard.db')

#Get a cursor object
cursor = conn.cursor()

#Creates the users table
cursor.execute('''
    CREATE TABLE Users(UserID INTEGER PRIMARY KEY, First_Name TEXT NOT NULL,
                       Last_Name TEXT NOT NULL)
                       ''')
#Runs the command
conn.commit()

#Creates the level_1 table
cursor.execute('''
    CREATE TABLE Level_1(UserID INTEGER PRIMARY KEY, High_Score_1 INTEGER,
                         FOREIGN KEY(UserID) REFERENCES Users(UserID))''')
conn.commit()

#Creates the level_2 table
cursor.execute('''
    CREATE TABLE Level_2(UserID INTEGER PRIMARY KEY, High_Score_2 INTEGER,
                         FOREIGN KEY(UserID) REFERENCES Users(UserID))''')
conn.commit()

#Creates the level_3 table
cursor.execute('''
    CREATE TABLE Level_3(UserID INTEGER PRIMARY KEY, High_Score_3 INTEGER,
                         FOREIGN KEY(UserID) REFERENCES Users(UserID))''')
conn.commit()

#Creates the level_4 table
cursor.execute('''
    CREATE TABLE Level_4(UserID INTEGER PRIMARY KEY, High_Score_4 INTEGER,
                         FOREIGN KEY(UserID) REFERENCES Users(UserID))''')
conn.commit()

#Creates the level_5 table
cursor.execute('''
    CREATE TABLE Level_5(UserID INTEGER PRIMARY KEY, High_Score_5 INTEGER,
                         FOREIGN KEY(UserID) REFERENCES Users(UserID))''')
conn.commit()


#Closes the database
conn.close()

