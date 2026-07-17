# Program Name: Assignment5.py
# Course: IT3883/Advanced Application Development
# Student Name: Ivan Yann NGAKU FOSSO
# Assignment Number: Lab 5
# Due Date: 17/06/2026
# Purpose: Reads daily temperature readings from a text file, stores them in a
#          SQLite database, then queries and prints the average temperature
#          for Sunday and Thursday.
# Resources: Python sqlite3 documentation

import sqlite3

# connect to (or create) the database file
conn = sqlite3.connect("Assignment5.db")
cursor = conn.cursor()

# create the table to hold the temperature data
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Temperatures (
        ID INTEGER PRIMARY KEY,
        Day_Of_Week TEXT,
        Temperature_Value REAL
    )
""")

# clear any old data so re-running the script doesn't duplicate rows
cursor.execute("DELETE FROM Temperatures")

# read the input file and insert each line into the table
with open("Assignment5input.txt", "r") as file:
    for line in file:
        day, temp = line.split()
        cursor.execute(
            "INSERT INTO Temperatures (Day_Of_Week, Temperature_Value) VALUES (?, ?)",
            (day, float(temp))
        )

conn.commit()

# compute and print the average temperature for Sunday and Thursday
for day in ("Sunday", "Thursday"):
    cursor.execute(
        "SELECT AVG(Temperature_Value) FROM Temperatures WHERE Day_Of_Week = ?",
        (day,)
    )
    avg_temp = cursor.fetchone()[0]
    print(f"Average temperature on {day}: {avg_temp:.2f}")

conn.close()
