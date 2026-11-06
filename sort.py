numGrades = int(input("Please enter number of grades "))
grades = []
for j in range(0, numGrades):
    grade = float(input("Enter a grade "))
    grades.append(grade)

list_ordered = []
for j in range(0, numGrades):       # fix: j, not i
    highest_grade = 0
    for i in range(0, len(grades)):  # fix: use len(grades) since it shrinks
        if highest_grade <= grades[i]:
            highest_grade = grades[i]
    list_ordered.append(highest_grade)
    grades.remove(highest_grade)

print(list_ordered)
