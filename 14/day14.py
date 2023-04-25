from collections import Counter

file = open("input.txt", "r")

rules = {}

template = ""

for line in file:
    line = line.rstrip("\n")
    
    if line.startswith("OFSVVSFO"):
        template = line
        continue

    k, v = line.split(" -> ")
    rules[k] = v

# final_out = template
# temp = template

# cursor = 1

# for s in range(10):
#     for i in range(len(temp) - 1):
#         chars = temp[i:i+2]

#         if chars in rules:
#             final_out = final_out[:cursor] + rules[chars] + final_out[cursor:]
        
#         cursor += 2

#     temp = final_out
#     cursor = 1

# c = Counter(final_out)

# print(c)

G = {}

for i in range(len(template) - 1):
    chars = template[i:i+2] 
    if chars in rules:
        if chars in G:
            G[chars] += 1
        else:
            G[chars] = 1

for i in range(40):
    G2 = {}

    for k in G:
        if k in rules:
            insert = rules[k]
            G2[k[0] + insert] = G2[k[0] + insert] + G[k] if (k[0] + insert) in G2 else G[k]
            G2[insert + k[1]] = G2[insert + k[1]] + G[k] if (insert + k[1]) in G2 else G[k]
    G = G2

CF = Counter()

for k in G:
    CF[k[0]] += G[k]

CF[template[-1]] += 1

print(max(CF.values())-min(CF.values()))