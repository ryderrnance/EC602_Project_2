P = [3, 0, 2, 1]
Q = [8, 7, 6]

A, B = sorted([P, Q], key=len)

for i, x in enumerate(reversed(A), 1):
   B[-i] += x

print(B)
