#PROMPT: Word frequency counter, create dictionary, count how many times a word appears, print dictionary
sentence = "code fast and code smart and stay consistent"


splitSen = sentence.split()

result = {}


for word in splitSen:
    if word in result:
        result[word]+=1
    else:
        result[word]=1
        
#print(result)
#OUTPUT: {'code': 2, 'fast': 1, 'and': 2, 'smart': 1, 'stay': 1, 'consistent': 1}

#cleaner output
for key, value in result.items():
    print(key, value)
    
#OUTPUT:
#code 2
#fast 1
#and 2
#smart 1
#stay 1
#consistent 1
