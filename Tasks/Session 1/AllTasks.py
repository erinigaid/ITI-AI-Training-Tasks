y="java is a language"
print(y.replace('java','python'))

#########session 1#############################################
3+4
print("hi")
x=1.5
print(type(x))
print(type("hi"))
z=10
print(z%2)
print(z**2)
pi=3.14
r=2
area=2*pi*r
print(area)
greet="hi"
name="erini"
print(greet + name)
print(greet,name)
print(greet+" "+name *3)

####################################
for n in range(5):
    print(n)
###################################
n=0
while n<5:
    print(n)
    n=n+1

##################################

ans=0
neg_flag = False
x=int(input("Enter an integer: "))
if x < 0:
    neg_flag= True
while ans**2 < x:
    ans+= 1
if ans**2 == x:
    print("sqare root of", x,"is",ans)
else:
    print(x, "is not a perfect sqaure")
if neg_flag:
    print("just checking... did you mean", -x,"?")

#######################Task1###############################
a= float(input("Enter a number for a:"))
b= float(input("Enter a number for b:"))
if a==b:
    print("a & b are equal")
    if b!=0:
        print("a/b is",a/b)
elif a>b:
    print("b is smaller")
elif b > a:
    print("a is smaller")
print("thanks")

############Task 2############################################
k="this is a code"
character=input("Enter the character you wanna search: ")
for index in range(len(k)):
    if k[index]==character:
        print("true")
        break
    else:
        print("False")
        break

###############Task 3############################################
idlist=[1,2,3,4]
id=int(input("enter your id: "))
if id in idlist:
    print(id,"exists in the list")
else:
    print(id,"doesn't exist in the list")

# ###############Task 4############################################
idlist=[1,2,3,4]
id=int(input("enter your id: "))
i=0
while i < len(idlist):
    if id == idlist[i]:
        print(id,"exists in the list")
    else:
        print(id,"doesn't exist in the list")
    i=i+1
################Task 5###########################################
name=input("What is your name? ")
age=int(input("What is your age? "))
hundred=int((100-age)+2021)
print("Hi",name+"!","your age is",age,".","You will turn 100 in",hundred)

###############Task 6############################################
list1=[2,3,5,6,7]
list2=[1,2,4,5,6]
list3=[]
for i in list1:
    for j in list2:
        if i==j:
            list3.append([i])
print(list3)

##############Task 7############################################
text=input("Enter text: ")
reversedtxt=text[::-1]
if(reversedtxt==text):
    print("true")
else:
    print("false")
