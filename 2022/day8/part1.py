with open('input.txt') as f:
    input = f.read().splitlines()

gh = [[int(x) for x in list(line)] for line in input]
gv = list(zip(*gh))
vs = 0

for row in range(len(gh)):
    for col in range(len(gh[0])):
        t = gh[row][col]  # tree
        r = gh[row][col + 1:]  # right
        d = gv[col][row + 1:]  # down
        l = gh[row][0:col][::-1]  # left
        u = gv[col][0:row][::-1]  # up
        for n in [r, d, l, u]:
            if not n or max(n) < t:
                vs += 1
                break

print(vs)

assert vs == 1827
