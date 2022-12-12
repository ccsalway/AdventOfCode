import math

monkeys = []
inspect = []

with open('input.txt') as f:
    for m in f.read().split('\n\n'):
        lines = m.splitlines()
        items = [i.strip() for i in lines[1].split(':')[1].split(',')]
        op = lines[2].split('=')[1].strip()
        test = int(lines[3].split(' ')[-1])
        true = int(lines[4].split(' ')[-1])
        false = int(lines[5].split(' ')[-1])
        monkey = [items, op, test, true, false]
        monkeys.append(monkey)
        inspect.append(0)
        # print(monkey)

lcm = math.lcm(*[n[2] for n in monkeys])

for r in range(10000):
    for n in range(len(monkeys)):
        m = monkeys[n]
        inspect[n] += len(m[0])
        for i in m[0]:
            r = eval(m[1].replace('old', i)) % lcm
            if r % m[2] == 0:
                monkeys[m[3]][0].append(str(r))
            else:
                monkeys[m[4]][0].append(str(r))
        m[0] = []

result = math.prod(sorted(inspect)[-2:])
print(result)

assert result == 13237873355
