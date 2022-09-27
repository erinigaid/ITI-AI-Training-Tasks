import csv
with open('people.csv','w',newline='')as file:
    writer=csv.writer(file)
    writer.writerow(['SN','Movie','Protagonist'])
    writer.writerow([1,'Lord of the Rings','Frodo Baggins'])
    writer.writerow([2,'Harry Potter','Harry Potter'])


    with open('people.csv','r')as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
for i in range (10):
    name=input("Enter name: ")
    age=input("Enter age: ")
    salary=input("Enter Salary: ")
    i+=1
i=0
