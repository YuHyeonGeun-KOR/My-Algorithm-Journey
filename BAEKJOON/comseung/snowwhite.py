from itertools import combinations


nanJaenge = []
for i in range(9):
    nanJaenge.append(int(input()))

nanJaenge = sorted(nanJaenge)

nanJaenge_com = list(combinations(nanJaenge,7))
result  = []
for com in nanJaenge_com:
    if sum(com)  == 100:
        result = com
        break

result = sorted(result)

for i in result:
    print(i)