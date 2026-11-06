import pickle
fruits = ['apples','bananas','oranges']
x=7
y=3.14
nuts=['pecans','almond']
grades=[99,100,56,77,85]
with open('myData.pkl','wb') as f:
    pickle.dump(fruits,f)
    pickle.dump(x,f)
    pickle.dump(y,f)
    pickle.dump(nuts,f)
    pickle.dump(grades,f)
with open('myData.pkl','rb') as f:
    a=pickle.load(f)
    b=pickle.load(f)
    c=pickle.load(f)
    d=pickle.load(f)
    e=pickle.load(f)
print(a)