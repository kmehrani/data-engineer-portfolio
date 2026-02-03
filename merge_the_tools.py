from collections import OrderedDict

def merge_the_tools(string, k):
    # your code goes here
    n = 0
    
    for grouping in range(0, len(string), k):
        split = string[n:n+k]
        keys = OrderedDict.fromkeys(split).keys()
        print(''.join(keys))
        n+=k
        

if __name__ == '__main__':


#Day 2 logging: I had a hard time with this Hackerrank question and had to google
#A LOT before finding a solution BUT I am still proud of myself for pushing through
#It was discouraging and I hope that tomorrow will be better. Right now my goal
#is to stay consistant 
