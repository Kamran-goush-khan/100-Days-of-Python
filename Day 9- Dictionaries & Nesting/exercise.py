student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for name in student_scores:
    if 90 < student_scores[name] <= 100:
        student_grades[name] = "Outstanding"
    elif 80 < student_scores[name] <= 90:
        student_grades[name] = "Exceeds Expectations"
    elif 70 < student_scores[name] <= 80:
        student_grades[name] = "Acceptable"
    else :
        student_grades[name] = "Fail"

print(student_grades)
