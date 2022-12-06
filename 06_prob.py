# String parsing again - input is one long string of lowercase letters
# start of a packet = sequence of four characters that are all different
# report the number of characters from the beginning of the buffer to the end of the first such four-character marker

buffer = open('06_input.txt', 'r').readline().strip()


def buffer_index(buffer_string, n_unique=4):
    consecutive_uniq = ''
    for i, c in enumerate(buffer_string):
        if c not in consecutive_uniq:
            consecutive_uniq += c
            if len(consecutive_uniq) == n_unique:
                buffer_len = i + 1
                break
        else:
            index_of_first_repeat = consecutive_uniq.index(c) + 1
            consecutive_uniq = consecutive_uniq[index_of_first_repeat:] + c
    return buffer_len


print(f"Packet start = {buffer_index(buffer, 4)}")
print(f"Message start = {buffer_index(buffer, 14)}")
