with open('input.txt') as f:
    input = f.read()

for i in range(len(input)):
    if len(set(input[i:i + 4])) == 4:
        break

result = i + 4
print(result)

assert result == 1625
