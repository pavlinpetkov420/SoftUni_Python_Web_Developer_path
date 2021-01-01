diff = int(input())
start = 97
end = start + diff
for i in range(start, end):
    for j in range(start, end):
        for k in range(start, end):
            fs = chr(i)
            ss = chr(j)
            ts = chr(k)
            combination = ""
            combination += fs + ss + ts
            print(combination)
