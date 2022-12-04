# Input is a pair of "sections" two elves have to clean.
# Ex 2-4,6-8
# Find the number of pairs where one set is completely contained in the other.

raw_data = [line.strip().split(',') for line in open('04_input.txt', 'r').readlines()]


def sections_as_set(string_sections):
    start_str, end_str = string_sections.split('-')
    return set(range(int(start_str), int(end_str)+1))


repeats = []
overlaps = []
for pair in raw_data:
    set1 = sections_as_set(pair[0])
    set2 = sections_as_set(pair[1])

    if set1.issubset(set2) or set2.issubset(set1):
        repeats.append(pair)

    if len(set1.intersection(set2)) > 0:
        overlaps.append(pair)

print(f'Pairs with fully overlapping sets: {len(repeats)}')
print(f'Pairs with at least some intersection: {len(overlaps)}')


