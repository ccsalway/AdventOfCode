with open('input.txt') as f:
    input = f.read()

for i in range(len(input)):
    if len(set(input[i:i + 4])) == 4:
        break

result = i + 4
assert result == 1625
print(result)
