total = 0

with open('input.txt') as f:
    for line in f.read().splitlines():
        f, s = line.split(',')
        f1, f2 = [int(n) for n in f.split('-')]
        s1, s2 = [int(n) for n in s.split('-')]
        if (s1 <= f1 <= s2 and s1 <= f2 <= s2) or \
                (f1 <= s1 <= f2 and f1 <= s2 <= f2):
            total += 1

print(total)

assert total == 503
