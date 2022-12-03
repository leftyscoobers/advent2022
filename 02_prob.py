# Rock paper scissors with mysterious input plan

opponent_shape = {'A': 'rock', 'B': 'paper', 'C': 'scissors'}
my_shape = {'X': 'rock', 'Y': 'paper', 'Z': 'scissors'}

win = [('rock', 'paper'), ('paper', 'scissors'), ('scissors', 'rock')]
lose = [('rock', 'scissors'), ('paper', 'rock'), ('scissors', 'paper')]
shape_points = {'rock': 1, 'paper': 2, 'scissors': 3}


def get_plays(input_line):
    opp, me = input_line.split(' ')
    return opponent_shape[opp], my_shape[me]


raw_data = [l.strip() for l in open('02_input.txt', 'r').readlines()]

all_game_pts = []
for game in raw_data:
    game_pts = 0
    elf, me = get_plays(game)
    pts_for_my_shape = shape_points[me]
    if (elf, me) in win:
        game_pts = 6 + pts_for_my_shape
    elif (elf, me) in lose:
        game_pts = 0 + pts_for_my_shape
    else:
        game_pts = 3 + pts_for_my_shape

    all_game_pts.append(game_pts)


print(f'Part 1: Total points in proposed games is {sum(all_game_pts)}')

# Now the second column is not my play but how the round should end
# lose - X, tie - Y, win - Z


def get_points_from_outcome(input_line):
    opp, outcome = input_line.split(' ')
    opp_shape = opponent_shape[opp]
    pts = 0
    if outcome == 'Y':
        pts = 3 + shape_points[opp_shape]
    elif outcome == 'X':
        my_play = [pair for pair in lose if pair[0] == opp_shape][0][1]
        pts = 0 + shape_points[my_play]
    else:
        my_play = [pair for pair in win if pair[0] == opp_shape][0][1]
        pts = 6 + shape_points[my_play]
    return pts


pt2_game_pts = [get_points_from_outcome(game) for game in raw_data]

print(f'Part 2: Total points from pre-determined outcomes is {sum(pt2_game_pts)}')


