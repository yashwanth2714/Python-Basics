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
    


print("---------------")

studentsList = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}, # None is like null in other languages. It represents the absence of a value.
    {"name": "Luna", "house": "Ravenclaw", "patronus": "Hare"},
]

for student in studentsList:
    print(student["name"], student["house"], student["patronus"], sep=", ")
    
print("---------------")

for student in studentsList:
    print(student)
    for each in student:
        print(each, student[each], sep=": ")
        
        

size = 3
for i in range(size):
    for j in range(size):
        print("*", end="") 
    print("")
    

for i in range(size):
    print("#" * size)