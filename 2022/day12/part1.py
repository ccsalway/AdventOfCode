with open('input.txt') as f:
    rows = f.read().splitlines()

m, p, s, e = [], [], (), ()

for y in range(len(rows)):
    m.append([])
    for x in range(len(rows[y])):
        col = rows[y][x]
        v = ord(col)
        if col == 'S':
            v = ord('a')
            s = y, x
        elif col == 'E':
            v = ord('z') + 1
            e = y, x
        m[-1].append(v)

for y in range(len(m)):
    p.append([])
    for x in range(len(m[y])):
        p[-1].append(0)
p[s[0]][s[1]] = 1  # starting position

k = 0
while p[e[0]][e[1]] == 0:
    k += 1
    for y in range(len(rows)):
        for x in range(len(rows[y])):
            if p[y][x] == k:
                n = m[y][x]
                # left
                if x > 0 and p[y][x - 1] == 0 and m[y][x - 1] <= n + 1:
                    p[y][x - 1] = k + 1
                # up
                if y > 0 and p[y - 1][x] == 0 and m[y - 1][x] <= n + 1:
                    p[y - 1][x] = k + 1
                # right
                if x < len(rows[y]) - 1 and p[y][x + 1] == 0 and m[y][x + 1] <= n + 1:
                    p[y][x + 1] = k + 1
                # down
                if y < len(rows) - 1 and p[y + 1][x] == 0 and m[y + 1][x] <= n + 1:
                    p[y + 1][x] = k + 1

print(k)

assert k == 330
