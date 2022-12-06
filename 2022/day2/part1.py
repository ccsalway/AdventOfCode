values = {
    'X': 1,  # rock
    'Y': 2,  # paper
    'Z': 3.  # scissors
}

scores = {
    'A': {'Y': 6, 'Z': 0, 'X': 3},  # rock
    'B': {'Z': 6, 'X': 0, 'Y': 3},  # paper
    'C': {'X': 6, 'Y': 0, 'Z': 3}  # scissors
}

total_score = 0.0

with open('input.txt') as f:
    for line in f.read().splitlines():
        o, y = line.split(' ')
        total_score += values[y] + scores[o][y]

assert total_score == 12740
print(total_score)
