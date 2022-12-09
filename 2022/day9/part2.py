with open('input.txt') as f:
    input = f.read().splitlines()

r = [[0, 0] for _ in range(10)]
p = {(0, 0)}

for line in input:
    d, n = line.split(' ')
    for _ in range(int(n)):
        # move head
        if d == 'R':
            r[-1][0] += 1
        elif d == 'U':
            r[-1][1] += 1
        elif d == 'L':
            r[-1][0] -= 1
        elif d == 'D':
            r[-1][1] -= 1
        # move rest
        for x in range(1, len(r)):  # 1 2 3 4 5 6 7 8 9 10
            # move right
            if r[-x][0] - r[-x - 1][0] >= 2:
                r[-x - 1][0] += 1  # move right 1
                if r[-x][1] > r[-x - 1][1]:
                    r[-x - 1][1] += 1  # move up 1
                if r[-x][1] < r[-x - 1][1]:
                    r[-x - 1][1] -= 1  # move down 1
            # move up
            if r[-x][1] - r[-x - 1][1] >= 2:
                r[-x - 1][1] += 1  # move up 1
                if r[-x][0] > r[-x - 1][0]:
                    r[-x - 1][0] += 1  # move right 1
                if r[-x][0] < r[-x - 1][0]:
                    r[-x - 1][0] -= 1  # move left 1
            # move left
            if r[-x][0] - r[-x - 1][0] <= -2:
                r[-x - 1][0] -= 1  # move left 1
                if r[-x][1] > r[-x - 1][1]:
                    r[-x - 1][1] += 1  # move up 1
                if r[-x][1] < r[-x - 1][1]:
                    r[-x - 1][1] -= 1  # move down 1
            # move down
            if r[-x][1] - r[-x - 1][1] <= -2:
                r[-x - 1][1] -= 1  # move down 1
                if r[-x][0] > r[-x - 1][0]:
                    r[-x - 1][0] += 1  # move right 1
                if r[-x][0] < r[-x - 1][0]:
                    r[-x - 1][0] -= 1  # move left 1
        p.add(tuple(r[0]))

total = len(p)
print(total)

assert total == 2443
