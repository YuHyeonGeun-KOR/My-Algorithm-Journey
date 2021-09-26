import sys
input = sys.stdin.readline

n, m  = map(int,input().split())

string_list = []


dna_info = {0:"A" , 1:"C" , 2:"G" , 3:"T"}
for i in range(n):
    string_list.append(input())

result_dna = ""
max_ham = 0
for i in range(m):
    alpa = [0] * 4
    for j in range(n):
        if string_list[j][i] == "A":
            alpa[0] +=1
        elif string_list[j][i] == "C":
            alpa[1] +=1
        elif string_list[j][i] == "G":
            alpa[2] +=1
        elif string_list[j][i] == "T":
            alpa[3] +=1

    add_string = dna_info[alpa.index(max(alpa))]

    result_dna += add_string
    max_ham += n - max(alpa)

print(result_dna)
print(max_ham)