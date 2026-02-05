#PROMPT: print the even numbers in the list


#Solution 1
def even_nums(nums):
    for x in nums:
        if x % 2 == 0:
           print(x)




nums = [1,2,3,4,5,6]

#Solution 2
newNum = [x for x in nums if x%2 == 0]

print(newNum)

even_nums(nums)

#Logging: Problem was easy to do. Quick and simple day due to time constraint.
#Glad I still got some practice in. I will spend more time tomorrow!
#Want to do some more pandas and numpy refreshing tomorrow. 
