# Loading rucksacks with rules
# Rucksacks (lines) have two equal-size compartments.
# Items (letters) can only be in one of them

import string
letters = list(string.ascii_lowercase) + list(string.ascii_uppercase)
letter_priority = dict(zip(letters, list(range(1, 53))))

# Find priority mapping of redundant letters and get sum of all
raw_data = [line.strip() for line in open('03_input.txt', 'r').readlines()]


def compartments(rucksack):
    r_size = len(rucksack)
    return rucksack[:int(r_size/2)], rucksack[int(r_size/2):len(rucksack)]


def find_duplicate(rucksack):
    c1, c2 = compartments(rucksack)
    repeat = [item for item in c1 if item in c2][0]
    return repeat


priority_pts = [letter_priority[find_duplicate(sack)] for sack in raw_data]
print(f'Total priority pts: {sum(priority_pts)}')

# Part 2 - find the letter that appears in each set of three lines instead (same priority and sum)
# Not sure how to do this efficiently...


def get_badge(elf_rucks):
    for letter in elf_rucks[0]:
        if letter in elf_rucks[1]:
            if letter in elf_rucks[2]:
                return letter


pt2_priority = []
for i in range(0, len(raw_data), 3):
    pt2_priority.append(letter_priority[get_badge(raw_data[i:(i+3)])])

print(f'Part 2: Badge priority sum is {sum(pt2_priority)}')

