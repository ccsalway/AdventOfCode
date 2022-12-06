values = {
    'A': {'Z': 2, 'X': 3, 'Y': 1},  # rock
    'B': {'Z': 3, 'X': 1, 'Y': 2},  # paper
    'C': {'Z': 1, 'X': 2, 'Y': 3}   # scissors
}

scores = {
    'Z': 6,  # win
    'Y': 3,  # draw
    'X': 0  # lose
}

total_score = 0.0

with open('input.txt') as f:
    for line in f.read().splitlines():
        o, y = line.split(' ')
        total_score += values[o][y] + scores[y]

assert total_score == 11980
print(total_score)
