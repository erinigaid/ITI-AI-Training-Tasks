# vacuum Agent
import random

def display(room):
    print(room)
room=[
    [1,1,1,1],
    [1,1,1,1],
    [1,1,1,1],
    [1,1,1,1],
]
print("All the rooms are dirty")
display(room)

x=0
y=0
while x<4:
    while y<4:
        room[x][y]=random.choice([0,1])
        y+=1
    x+=1
    y=0
print("before cleaning the room i detect all of these random dirts")
display(room)
x=0
y=0
z=0
while x<4:
    while y<4:
        if room[x][y]==1:
            print("Vaccum in this location now",x,y)
            room[x][y]=0
            print("cleaned",x,y)
            z+=1
        y+=1
    x+=1
    y=0
pro=(100-((z/16)*100))
print("room is clean now")
display(room)
print("performance",pro,'%')
