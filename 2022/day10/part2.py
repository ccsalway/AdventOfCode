with open('input.txt') as f:
    input = f.read().splitlines()

r = [1]

for line in input:
    if line.startswith('addx'):
        _, n = line.split(' ')
        r.extend([0, int(n)])
    else:  # noop
        r.append(0)

w, d = 40, []
for c, x in enumerate(r):
    p = (c // w) * w + sum(r[0:c + 1])
    d.append('#' if p - 1 <= c <= p + 1 else ' ')

for t in range(len(d) // w):
    print(''.join(d[t * w:t * w + w]))

# RGLRBZAU
