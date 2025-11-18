import networkx as nx

with open('downloads\le450_5a.col.txt', 'r', encoding='utf-8') as f:
    for linha in f:
        if(linha.__contains__('number of vertices')):
            num = linha[24:27]
            print(num)
        
c = []
for i in num:
    c.append(i)

print(c)

        