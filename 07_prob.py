# Capture size of all directors in terminal output (that we also have to parse)
from copy import deepcopy

term_output = [l.strip() for l in open('07_input.txt', 'r').readlines()]


# Recreate the file system as a dictionary (all strings for now)
file_sys = {}
previous_location = 'home'
curr_location = 'home'
for line in term_output:
    if curr_location not in file_sys:
        file_sys[curr_location] = []

    if '$ cd' in line:
        prev_loc_copy = previous_location
        previous_location = curr_location
        if '/' in line:
            curr_location = 'home'
        elif '..' in line:
            curr_location = prev_loc_copy
        else:
            curr_location = line.split(' ')[2]
    elif 'dir ' in line:
        dir_name = line.split()[1]
        file_sys[curr_location].append(dir_name)
    elif '$ ls' in line:
        continue
    else:
        size_as_str = line.split()[0]
        file_sys[curr_location].append(size_as_str)

print(f"Created file system dictionary")

# Now get all the numeric strings
# Could do recursively, which breaks my brain every time, or just a while loop?


def consolidate_nums(file_list):
    sum_so_far = sum([int(x) for x in file_list if x.isnumeric()])
    strings_left = [x for x in file_list if not x.isnumeric()]
    return [str(int(sum_so_far))] + strings_left


def is_all_nums(file_list):
    return all([x.isnumeric() for x in file_list])


size_limit = 1e5
file_sys_sizes = deepcopy(file_sys)
del file_sys_sizes['home']

for i, dir in enumerate(file_sys_sizes.keys()):
    print(f"{dir} with original {file_sys[dir]}")

    # Loop through until we have only one number (adding as we go)
    while not is_all_nums(file_sys_sizes[dir]):
        starting_list = file_sys_sizes[dir]
        for f in starting_list:
            if f.isnumeric():
                continue
            else:
                sub_list = file_sys_sizes[f]
                old_list = file_sys_sizes[dir]
                old_list.remove(f)
                file_sys_sizes[dir] = old_list + sub_list
        consolidated = consolidate_nums(file_sys_sizes[dir])
        file_sys_sizes[dir] = consolidated

    print(f"finished key {dir}, index {i}")
    # some of these are still going to be > 1....


# But we're not done yet! :-(

