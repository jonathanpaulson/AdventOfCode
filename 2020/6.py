import fileinput
import re
import string

# p1 = sum_group len(union(answers))
# p2 = sum_group len(intersection(answers))
p1 = 0
p2 = 0

lines = list(fileinput.input())
lines.append('')

# We could also start any_yes and all_yes with the identity for their operations.
# For any_yes the operation is union (|), whose identity is set()
# For all_yes the operation is intersection (&), whose identity is set(string.ascii_lowercase)
any_yes = None
all_yes = None

for line in lines:
    line = line.strip()
    if not line:
        p1 += len(any_yes)
        p2 += len(all_yes)
        any_yes = None
        all_yes = None
    else:
        if any_yes is None:
            any_yes = set(line)
        else:
            any_yes = any_yes | set(line)

        if all_yes is None:
            all_yes = set(line)
        else:
            all_yes = all_yes & set(line)

print(p1)
print(p2)
