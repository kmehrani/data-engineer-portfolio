#PROMPT: Categorize Numbers as "even" or "odd"

numbers = [3, 8, 15, 22, 27, 30]

result ={
    "even":[],
    "odd":[]
}


for num in numbers:
    if num%2 == 0:
        result["even"].append(num)
    else:
        result["odd"].append(num)
        
print(result)

#OUTPUT: {'even': [8, 22, 30], 'odd': [3, 15, 27]}
    
#LOG: Took a break to prep for ramadan but now I am back. Problem was not difficult.
#It gave me a small push.

