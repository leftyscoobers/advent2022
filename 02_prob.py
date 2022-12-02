# Rock paper scissors wtih
# Opponent rock - A, paper - B, scissors - C
# Your play rock - X, paper - Y, scissors - Z

raw_data = [l.strip() for l in open('02_input.txt', 'r').readlines()]

my_wins = ['C X', 'A Y', 'B Z']
my_ties = ['A X', 'B Y', 'C Z']
my_loss = ['B X', 'C Y', 'A Z']
shape_points = {'X': 1, 'Y': 2, 'Z': 3}

all_game_pts = []
for game in raw_data:
    game_pts = 0
    my_play = game.split(' ')[1]
    round_shape_pts = shape_points[my_play]
    if game in my_wins:
        game_pts = 6
    elif game in my_ties:
        game_pts = 3

    all_game_pts.append(game_pts + round_shape_pts)

print(f'Part 1: Total points in proposed games is {sum(all_game_pts)}')

# Now the second column is not my play but how the round should end
# lose - X, tie - Y, win - Z

# Prioritizing re-writing as little of the above as possible over making this neat
# God this is ugly
pt_game_pts = []
for game in raw_data:
    opponent = game.split(' ')[0]
    outcome = game.split(' ')[1]
    game_pts = 0

    if outcome == 'X':
        pairs = [(pair.split(' ')[0], pair.split(' ')[1]) for pair in my_loss]
        this_game = [p for p in pairs if opponent in p][0][1]
    if outcome == 'Y':
        pairs = ... # had to stop for now

