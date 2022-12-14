with open('input.txt') as f:
    rows = f.read().splitlines()

t, s, e = [], [], ()

# topo matrix
for y in range(len(rows)):
    t.append([])
    for x in range(len(rows[y])):
        ltr = rows[y][x]
        h = ord(ltr)  # height at position
        if ltr in ['S', 'a']:
            s.append((y, x))  # add to starting positions
            h = ord('a')
        elif ltr == 'E':
            e = y, x  # ending position
            h = ord('z')
        t[-1].append(h)

ks = []
for start in s:

    # path matrix
    p = [[int(n) for n in '0' * len(row)] for row in rows]
    p[start[0]][start[1]] = 1  # starting position

    # step counter
    k = 0
    while p[e[0]][e[1]] == 0:
        k += 1
        unreachable = 1
        for y in range(len(rows)):
            for x in range(len(rows[y])):
                if p[y][x] == k:
                    n = t[y][x]
                    # left
                    if x > 0 and p[y][x - 1] == 0 and t[y][x - 1] <= n + 1:
                        unreachable = 0
                        p[y][x - 1] = k + 1
                    # up
                    if y > 0 and p[y - 1][x] == 0 and t[y - 1][x] <= n + 1:
                        unreachable = 0
                        p[y - 1][x] = k + 1
                    # right
                    if x < len(rows[y]) - 1 and p[y][x + 1] == 0 and t[y][x + 1] <= n + 1:
                        unreachable = 0
                        p[y][x + 1] = k + 1
                    # down
                    if y < len(rows) - 1 and p[y + 1][x] == 0 and t[y + 1][x] <= n + 1:
                        unreachable = 0
                        p[y + 1][x] = k + 1
        if unreachable == 1:
            break
    if unreachable == 0:
        ks.append(k)

shortest = sorted(ks)[0]
print(shortest)

assert shortest == 321
