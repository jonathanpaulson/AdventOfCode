import fileinput
import re
from collections import deque, defaultdict

# For part1, we need to keep track of which bags have other bags as containers
# For part2, we need to keep track of which bags (and how many!) each bag contains
# We can think of both of these as graphs where the vertices are the bags and the edges
#  are which bags might contain us (part1) and which bags and how many of each we contain (part2)

PARENTS = defaultdict(list) # PARENTS[x] are the bags that contain x
CONTENTS = defaultdict(list) # CONTENTS[x] are which bags x contains and how many of each

target = 'shinygoldbag'

lines = list(fileinput.input())
lines.append('')
for line in lines:
    line = line.strip()
    if line:
        words = line.split()
        container = words[0]+words[1]+words[2]
        container = container[:-1] # remove trailing 's' in 'bags'
        if words[-3] == 'no': # doesn't contain any other bags
            continue
        else:
            idx = 4
            while idx < len(words):
                bag = words[idx]+words[idx+1]+words[idx+2]+words[idx+3]
                if bag.endswith('.'):
                    bag = bag[:-1]
                if bag.endswith(','):
                    bag = bag[:-1]
                if bag.endswith('s'):
                    bag = bag[:-1]
                n = int(bag[0])
                assert bag[1] not in '0123456789'
                while any([bag.startswith(d) for d in '0123456789']):
                    bag = bag[1:]

                PARENTS[bag].append(container)
                CONTENTS[container].append((n, bag))
                idx += 4

SEEN = set()
Q = deque([target])
while Q:
    x = Q.popleft()
    if x in SEEN:
        continue
    SEEN.add(x)
    for y in PARENTS[x]:
        Q.append(y)
print(len(SEEN)-1)

def size(bag):
    ans = 1
    for (n,y) in CONTENTS[bag]:
        ans += n*size(y)
    return ans
print(size(target)-1)
