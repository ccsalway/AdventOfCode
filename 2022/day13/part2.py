def flatten(seq):
    if seq == []:
        return [-1]
    if isinstance(seq[0], list):
        return flatten(seq[0]) + flatten(seq[1:])
    return seq[:1] + flatten(seq[1:])


all = [[2], [6]]
with open('input.txt') as f:
    for group in f.read().split('\n\n'):
        all.extend([flatten(eval(p)) for p in group.splitlines()])

x = []
for idx, a in enumerate(sorted(all)):
    if a == [2]:
        x.append(idx + 1)
    if a == [6]:
        x.append(idx + 1)

total = x[0] * x[1]
print(total)

assert total == 22344
