import pandas as pd
########################Task1##################
s=pd.Series([1,2,3,4])
print(s.describe())

s=pd.Series(['a','b','c','d'])
print(s.describe())

############################Task2##################################
df = pd.DataFrame({"categorical": pd.Categorical(['s','t','u']),
                   "numeric":[2,3,4],
                   "object":["p","q","r"]})
print(df)
print(df.describe())
print(df.describe(include="all"))
print(df.describe(include='category'))
print(df.describe(exclude=[object]))

#####################Task3############################
salaries = pd.read_csv('salaries.csv')
print(salaries.tail())
print(salaries.describe())


##############Task4########################33
f=open("file.txt","r")
lines=f.readlines()
for line in lines:
    print(line)

with open("file.txt","r")as file:
    fileContent=file.read()
    print(fileContent)
print(file.closed)
print(fileContent)
with open ('file.txt','a')as file:
    file.write("hi there")