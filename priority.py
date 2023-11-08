#Priority formula
import math


priority = []
A = 54
M = 1994
Zo = 10112166
C = 9

for i in range(11):
    LCG = ((A * Zo) + C) % M
    X = LCG / M
    Zo = LCG
    Y = ((3 - 1) * X) + 1
    if Y - math.floor(Y) >= 0.5:
        Y = math.ceil(Y)
        priority.append(Y)
    else:
        Y = math.floor(Y)
        priority.append(Y)

for i in range(len(priority)):
    print(priority[i])
