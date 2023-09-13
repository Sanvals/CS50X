import csv
from cs50 import SQL

def create_houses(house, houses, head):
    count = 0
    for i in houses:
        if i["house"] == house:
            count += 1

    if count == 0:
        houses.append({"house": house, "head": head})

def create_student(name, students):
    students.append({"student_name": name})

def create_relations(name, house, relations):
    relations.append({"student_name": name, "house": house})

db = SQL("sqlite:///roster.db")

students = []
houses = []
relations = []

with open ("students.csv", "r") as f:
    reader = csv.DictReader(f)
    for i in reader:
        name = i["student_name"]
        house = i["house"]
        head = i["head"]

        create_houses(house, houses, head)
        create_student(name, students)
        create_relations(name, house, relations)

for students in students:
    db.execute("INSERT INTO new_students (students_name) VALUES (?)", i["student_name"])

for rel in relations:
    db.execute("INSERT INTO relations (students_name, house) VALUES (?,?)", rel["student_name"], rel["house"])

for house in houses:
    db.execute("INSERT INTO houses (house, head) VALUES (?,?)", house["house"], house["head"])