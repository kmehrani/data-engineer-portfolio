#Prompt: group employee names by department

employees = [
    {"name": "Alice", "department": "Tech"},
    {"name": "Bob", "department": "HR"},
    {"name": "Charlie", "department": "Tech"},
    {"name": "Dana", "department": "Finance"},
]


groupDept = {}

for item in employees:
    key = item["department"]
    if key not in groupDept:
        groupDept[key] = []


    groupDept[key].append(item["name"])
    

print(groupDept)

#little dictionary practice. not bad! proud of myself for being able to solve this
#one easily. definately had fun with it. I missed yesterday, but it's ok.
#I came back to practice today and that's what counts
