import matplotlib.pyplot as plt
students_names=['Sanjay','Rahul','Karan','Wasim','Ramesh','Ajay','Sartaj','Priya']
Students_marks=[35,50,20,45,25,40,25,40]
marks_perc=[]
for x in Students_marks:
    res = (x/50)*100
    marks_perc.append(res)
print(marks_perc)
def marks_line_chart():
    plt.plot(students_names,Students_marks)
    plt.title('Students Marks Graph')
    plt.xlabel('Students Names')
    plt.ylabel('Students Marks')
    plt.show()
def marks_bar_chart():
    plt.bar(students_names , marks_perc)
    plt.title('Students Percentage Graph')
    plt.xlabel('Students Names')
    plt.ylabel('Student Percentage')
    plt.show()
marks_line_chart()
marks_bar_chart()