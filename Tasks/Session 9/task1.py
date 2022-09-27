def vectorize(tokens):
    vector=[]
    for w in filtered_vocab:
        vector.append(tokens.count(w))
    return vector

def unique(sequence):
    seen=set()
    return [x for x in sequence if not (x in seen or seen.add(x))]

stopwords=["to","is","a"]
special_char=[',',':',';','.','?','']
string1='Welcome to Great Learning, Now start learning to Great welcome'
string2='Learning is a good practice'

string1=string1.lower()
string2=string2.lower()

tokens1=string1.split()
tokens2=string2.split()

print(tokens1)
print(tokens2)

vocab=unique(tokens1+tokens2)
print(vocab)

filtered_vocab=[]
for w in vocab:
    if w not in stopwords and w not in special_char:
        filtered_vocab.append(w)

print(filtered_vocab)
vector1=vectorize(tokens1)
print(vector1)
vector2=vectorize(tokens2)
print(vector2)