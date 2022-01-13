from student import student

student1 = student(1,"Vasu Pastagia",8.0,False)

# we can also create list of students
student2 = [
    student(1,"Vasu Pastagia",8.0,False),
    student(2,"Jay modi",7.0,True),
    student(3,"Rahul",6.5,True),
]

for i in student2:
    print(i.gpa)
    if i.on_honour_roll():
        print("This student is horrable")
    else:
        print("dont worry, work hard")

