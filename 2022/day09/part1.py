with open('input.txt') as f:
    input = f.read().splitlines()

m = {'R': [1, 0], 'D': [0, -1], 'L': [-1, 0], 'U': [0, 1]}
r = [[0, 0] for _ in range(2)]
p = {(0, 0)}

for line in input:
    d, n = line.split(' ')
    for _ in range(int(n)):
        # move head
        r[-1][0] += m[d][0]
        r[-1][1] += m[d][1]
        # move rest
        for x in range(1, len(r)):
            h, t = r[-x], r[-x - 1]
            if not -2 < h[0] - t[0] < 2:  # x too far away
                t[0] += 1 if h[0] > t[0] else -1
                if h[1] != t[1]:  # need to move diagonal
                    t[1] += 1 if h[1] > t[1] else -1
            if not -2 < h[1] - t[1] < 2:  # y too far away
                t[1] += 1 if h[1] > t[1] else -1
                if h[0] != t[0]:  # need to move diagonal
                    t[0] += 1 if h[0] > t[0] else -1
        p.add(tuple(r[0]))

total = len(p)
print(total)

assert total == 5930
