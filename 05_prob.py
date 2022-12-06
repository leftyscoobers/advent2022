# File parsing requires reading elements of "stacks" and then directions to move them around.
# To get "stacks", split on spaces

raw_data = open('05_input.txt', 'r').readlines()

# Dumb way to get num of stacks
open_bracket_per_line = [line.count('[') for line in raw_data]
n_stacks = max(open_bracket_per_line)
stack_list = [n + 1 for n in list(range(n_stacks))]
index_of_box = list(range(1, n_stacks*4-1, 4))


stacks = [''] * n_stacks
directions = []
for line in raw_data:
    if '[' in line:
        box_values = [line[i] for i in index_of_box]
        stacks = [stacks[i] + box_values[i] for i in range(n_stacks)]
    if 'move' in line:
        directions.append(line)

stacks = [s.strip() for s in stacks]

# Not a good practice overwriting the stacks but whatever


def move_blocks(direct):
    dir_split = direct.split(' ')
    n_to_move = int(dir_split[1])
    from_stack = int(dir_split[3])-1
    to_stack = int(dir_split[5])-1
    moving_boxes = stacks[from_stack][:n_to_move][::-1] # move off top, reverse
    stacks[from_stack] = stacks[from_stack][n_to_move:]
    stacks[to_stack] = moving_boxes + stacks[to_stack]


for d in directions:
    move_blocks(d)

# Get "top" of each stack
print(f"Top of stacks: {''.join([s[0] for s in stacks])}")


# Lazy - just copy above and don't reverse the boxes while moving
stacks = [''] * n_stacks
directions = []
for line in raw_data:
    if '[' in line:
        box_values = [line[i] for i in index_of_box]
        stacks = [stacks[i] + box_values[i] for i in range(n_stacks)]
    if 'move' in line:
        directions.append(line)

stacks = [s.strip() for s in stacks]

# Not a good practice overwriting the stacks but whatever


def move_blocks(direct):
    dir_split = direct.split(' ')
    n_to_move = int(dir_split[1])
    from_stack = int(dir_split[3])-1
    to_stack = int(dir_split[5])-1
    moving_boxes = stacks[from_stack][:n_to_move]
    stacks[from_stack] = stacks[from_stack][n_to_move:]
    stacks[to_stack] = moving_boxes + stacks[to_stack]


for d in directions:
    move_blocks(d)

# Get "top" of each stack
print(f"Top of stacks: {''.join([s[0] for s in stacks])}")
