import csv
import pandas as pd
with open('persons.csv','w',newline='')as file:
    writer=csv.writer(file)
    writer.writerow(['Name','Age','Salary'])
    for i in range (10):
        name = input("Enter name: ")
        age = input("Enter age: ")
        salary = input("Enter Salary: ")
        writer.writerow([name, age, salary])
        i+=1
    with open('persons.csv','r')as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
persons = pd.read_csv('persons.csv')

print(persons.head(3))
print(persons.describe())
print(persons.tail(3))

