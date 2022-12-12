with open('input.txt') as f:
    crates, moves = f.read().split('\n\n')

lines = crates.splitlines()[::-1]  # reverse
rows = [list(line[1::4]) for line in lines[1:]]  # ignore first line of numbers
stacks = [list(filter(lambda i: i.strip(), t)) for t in list(zip(*rows))]

for line in moves.splitlines():
    _, q, _, s, _, f = line.split(' ')  # eg. move 11 from 1 to 4
    qn, sn, fn = [int(x) for x in [q, s, f]]
    stacks[fn - 1].extend(stacks[sn - 1][qn * -1:])
    del stacks[sn - 1][qn * -1:]

result = ''.join([s[-1] for s in stacks])
print(result)

assert result == 'SSCGWJCRB'
