numGrades = int(input("Please enter number of grades "))
grades = []
for j in range(0, numGrades):
    grade = float(input("Enter a grade "))
    grades.append(grade)

for i in range(0,numGrades-1):
    for i in range(0,numGrades-1):
        if grades[i]<grades[i+1]:
            swp=grades[i]
            grades[i]=grades[i+1]
            grades[i+1]=swp

print('sorted grade list is ', grades)
