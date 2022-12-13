def check(seq1, seq2):
    longer = max(len(seq1), len(seq2))
    for i in range(longer):
        s1 = seq1[i] if len(seq1) > i else -1
        s2 = seq2[i] if len(seq2) > i else -1
        if isinstance(s1, list):
            if isinstance(s2, list) and len(s1) == 0 and len(s2) > 0:
                print(s1, s2, True)
                return True
            if not isinstance(s2, list):
                s2 = [s2]
        if isinstance(s2, list):
            if isinstance(s1, list) and len(s2) == 0 and len(s1) > 0:
                print(s1, s2, False)
                return False
            if not isinstance(s1, list):
                s1 = [s1]
        if not isinstance(s1, list):
            if s1 == s2:
                continue
            if s1 < s2:
                print(s1, s2, True)
                return True
            if s1 > s2:
                print(s1, s2, False)
                return False
        else:
            result = check(s1, s2)
            if result is not None:
                return result
    return None


x = []
with open('input.txt') as f:
    groups = f.read().split('\n\n')
    for idx, group in enumerate(groups):
        lhs, rhs = group.splitlines()
        if check(eval(lhs), eval(rhs)):
            x.append(idx + 1)

result = sum(x)
print(result)

assert result == 5198
