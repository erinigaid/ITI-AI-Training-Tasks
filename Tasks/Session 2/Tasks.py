########################Task1#########################
s = "demo loops"
for index in range(len(s)):
    if s[index] == 'i'or s[index] == 'u':
        print("There is an i or u")

for char in s:
    if char == 'i' or char =='u':
        print("There is an i or u")
#########Task 2#############################################
l=[1,2,3]
doublelist=[2*item for item in l]
evenlist=[item for item in l if item%2==0]
print(doublelist)
print(evenlist)
updateEvenList=[item/2 for item in l if item%2==0]
print(updateEvenList)
###################Task3#########################################

import nltk
lines="I Love Cat"
is_noun= lambda pos: pos[:2]=='NN'
tokenized=nltk.word_tokenize(lines)
nouns=[word for (word,pos)in nltk.pos_tag(tokenized)if is_noun(pos)]
print(nouns)

#####################Task4#######################################
from nltk.tokenize import word_tokenize
mytxt="Hello Mr. Adam, how are you? i hope everything is going well. Today is a good day, see you dude."
print(word_tokenize(mytxt))
