import pickle
names=[]
grades=[]
numStudents=int(input("How many students do you have"))
for j in range(0,numStudents):
    name = input('Please enter Student name')
    names.append(name)
    prompt='Please Enter'+name+" 's grade"
    grade=float(input(prompt))
    grades.append(grade)
with open('studentData.pkl', 'wb') as f:
    pickle.dump(numStudents,f)
    pickle.dump(names,f)
    pickle.dump(grades,f)
with open('studentData.pkl', 'rb') as f:
    a = pickle.load(f)
    b = pickle.load(f)
    c = pickle.load(f)

print(a)
print(b)
print(c)

