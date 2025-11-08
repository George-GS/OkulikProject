students = {
    "Alice": {"math": 85, "physics": 92, "chemistry": 78},
    "Bob": {"math": 76, "physics": 88, "chemistry": 94},
    "Charlie": {"math": 92, "physics": 79, "chemistry": 86},
    "Diana": {"math": 88, "physics": 95, "chemistry": 91}
}

# Найди:
# 1. Студента с самым высоким средним баллом
# 2. Предмет с самой высокой средней оценкой
# 3. Выведи всех студентов с оценкой по математике > 85

a = 0
best_student = None
stud_math_85 = []


subject_totals = {"math": 0, "physics": 0, "chemistry": 0}
subject_counts = {"math": 0, "physics": 0, "chemistry": 0}

for student, objects in students.items():

    if a < sum(objects.values()) / 3:
        a = sum(objects.values()) / 3
        best_student = student


    for object, ocenka in objects.items():
        if object == 'math' and ocenka > 85:
            stud_math_85.append(student)

        subject_totals[object] += ocenka
        subject_counts[object] += 1

avg_object = 0
best_object = None

for object, ocenka in subject_totals.items():
    if avg_object < subject_totals[object] / subject_counts[object]:
        avg_object = subject_totals[object] / subject_counts[object]
        best_object = object


print(best_student)
print(stud_math_85)
print(best_object)


