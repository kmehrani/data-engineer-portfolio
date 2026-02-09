#PROMPT: Predict outputs without running the code

print(2%3)

nums = [2, 5, 8, 11]

result = {n: n % 3 for n in nums}

print(result)

#{2: 2, 5: 2, 8: 2, 11: 2}


nums = [1, 2, 3, 4]

result = [n*n for n in nums if n % 2 == 0]

print(result)

#[4, 16]

words = ["data", "engineer", "python", "sql"]

lengths = {w: len(w) for w in words if len(w) > 4}

print(lengths)

#"{engineer": 8, "python":6}


#logging day 7: I got them all correct. Less coding today because I hurt my hand. Feeling comfortable with coding again.
#It's clicking

