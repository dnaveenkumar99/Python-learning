t=(10,"python",20.5)
print(t)
print(type(t))
t1=(10,20,30,60)
print(t1)
t2=(10)
print(type(t2))
t3=("py")
print(type(t3))
t4=(10,)
print(type(t4))

#Indexing and slicing
t=(10,20,30,40,50,60,70)
print(t[2])
print(t[1:5])
print(t[-6:5])

#list within Tuple
student_info=("naveen",[58,91,98])
print(student_info)
name,marks=student_info
print(name)
print(marks)