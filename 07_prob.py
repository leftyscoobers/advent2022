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


def check_for_nums(file_list_in_dir):
    check_vals = [f.isnumeric() for f in file_list_in_dir]
    if all(check_vals):
        return True
    else:
        return False


def check_all_numeric(file_sys_dict):
    dir_all_nums = []
    for key, value in file_sys_dict.items():
        check_vals = check_for_nums(value)
        if not check_vals:
            return False
    return True


file_sys_sizes = deepcopy(file_sys)
all_good = check_all_numeric(file_sys_sizes)
loops = 0
while not all_good:
    loops += 1
    print(loops)
    for dir, ls in file_sys_sizes.items():
        if check_for_nums(ls):
            continue
        else:
            for f in ls:
                # print(f"list item {f}")
                if f.isnumeric():
                    continue
                else:
                    sub_files = file_sys_sizes[f]
                    orig_dir_list = file_sys_sizes[dir]
                    # print(f"original_list: {file_sys_sizes[dir]}")
                    orig_dir_list.remove(f)
                    new_size_list = orig_dir_list + sub_files
                    file_sys_sizes[dir] = new_size_list
                    # print(f"new list: {file_sys_sizes[dir]}")
    all_good = check_all_numeric(file_sys_sizes)

# But we're not done yet! :-(
# Now get the total size of each directory
# dir_totals = {}
# for dir, sizes in file_sys_sizes.items():
#     if dir == 'home':
#         continue
#     else:
#         dir_totals[dir] = sum([int(s) for s in sizes])
#
# # Now get sum of all dirs smaller than 100,000
# print(f'Total from small dirs = {sum([s for s in dir_totals.values() if s < 1e5])}')

