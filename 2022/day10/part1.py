with open('input.txt') as f:
    input = f.read().splitlines()

r = [1]

for line in input:
    if line.startswith('addx'):
        _, n = line.split(' ')
        r.extend([0, int(n)])
    else:  # noop
        r.append(0)

total = 0
for c in [n for n in range(len(r)) if n % 40 == 20]:
    total += c * sum(r[0:c])  # signal strength
print(total)

assert total == 14420
