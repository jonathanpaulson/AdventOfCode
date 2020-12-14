import fileinput
import re

p1 = 0
p2 = 0
passport = {} # current passport

def in_range(s, lo, hi):
    return lo<=int(s)<=hi

lines = list(fileinput.input())
lines.append('')
for line in lines:
    line = line.strip()
    if not line:
        valid1 = all([f in passport for f in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']])
        if valid1:
            p1 += 1
            valid2 = True

            if not in_range(passport['byr'], 1920, 2002):
                valid2 = False
            if not in_range(passport['iyr'], 2010, 2020):
                valid2 = False
            if not in_range(passport['eyr'], 2020, 2030):
                valid2 = False

            ht = passport['hgt']
            if ht.endswith('in'):
                if not in_range(ht[:-2], 59, 76):
                    valid2 = False
            elif ht.endswith('cm'):
                if not in_range(ht[:-2], 150, 193):
                    valid2 = False
            else:
                valid2 = False

            hcl = passport['hcl']
            if hcl[0]!='#' or any([c not in '0123456789abcdef' for c in hcl[1:]]):
                valid2 = False

            ecl = passport['ecl']
            if ecl not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                valid2 = False

            pid = passport['pid']
            if len(pid) != 9 or any([c not in '0123456789' for c in pid]):
                valid2 = False

            if valid2:
                p2 += 1
        passport = {}
    else:
        words = line.split()
        for word in words:
            k,v = word.split(':')
            passport[k] = v
print(p1)
print(p2)
