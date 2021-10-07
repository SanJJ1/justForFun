final=[]
import re
from itertools import permutations
while True:
    final.append(x := input())   #Each input given by the user gets appended to the list "final"
    if x == "0":
        break                   #When no input is given by the user, control moves to

final = final[:-1]
def count_substrings(string, substring):
    string_size = len(string)
    substring_size = len(substring)
    count = 0
    for i in range(0,string_size-substring_size+1):
        if string[i:i+substring_size] == substring:
            count+=1
    return count

for i in final:
    s, l = i.split()
    print(count_substrings(l, s))
    