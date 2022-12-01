raw_data = [d.strip() for d in open('01_input.txt', 'r').readlines()]

# Get total calories in rations for each elf
rations = []
elf_start = 0
for d in raw_data:
    if d == '':
        # Add current count of calories to rations list and reset for next elf
        rations.append(elf_start)
        elf_start = 0
        pass
    else:
        elf_start += int(d)

# Part 1: Find max calories for any elf
print(f'Max calories: {max(rations)}')

# Now find top three elves total
rations.sort(reverse=True)
print(f'Top three elves total: {sum(rations[:3])}')
