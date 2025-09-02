students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
    "Luna": "Ravenclaw",
}

print(students)
print(students["Hermione"])
print(students.get("Draco"))

for student in students:
    print(student, students[student], sep=" is in ")