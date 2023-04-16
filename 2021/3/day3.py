import copy

bits = []

file = open("input.txt", "r")

for line in file:
    bits.append(line.rstrip("\n"))

# gamma = ""
# epsilon = ""

# for i in range(len(bits[0])):
#     ones = 0
#     zeroes = 0

#     for bit in bits:
#         if int(bit[i]) == 0:
#             zeroes += 1
#         elif int(bit[i]) == 1:
#             ones += 1

#     if ones > zeroes:
#         gamma += '1'
#         epsilon += '0'
#     elif zeroes > ones:
#         gamma += '0'
#         epsilon += '1'


o2_list = copy.deepcopy(bits)
co2_list = copy.deepcopy(bits)

o2_value = 0
co2_value = 0

for i in range(len(bits[0])):
    ones = 0
    zeroes = 0

    for bit in o2_list:
        if int(bit[i]) == 0:
            zeroes += 1
        elif int(bit[i]) == 1:
            ones += 1

    if ones > zeroes:
        o2_list = list(filter(lambda x: x[i] == '1', o2_list))
    elif zeroes > ones:
        o2_list = list(filter(lambda x: x[i] == '0', o2_list))
    elif ones == zeroes:
        o2_list = list(filter(lambda x: x[i] == '1', o2_list))

    ones = 0
    zeroes = 0
    
    for bit in co2_list:
        if int(bit[i]) == 0:
            zeroes += 1
        elif int(bit[i]) == 1:
            ones += 1

    if ones > zeroes:
        co2_list = list(filter(lambda x: x[i] == '0', co2_list))
    elif zeroes > ones:
        co2_list = list(filter(lambda x: x[i] == '1', co2_list))
    elif ones == zeroes:
        co2_list = list(filter(lambda x: x[i] == '0', co2_list))

    if len(o2_list) == 1:
        o2_value = o2_list[0]
    
    if len(co2_list) == 1:
        co2_value = co2_list[0]


o2_dec = int(o2_value, 2)
co2_dec = int(co2_value, 2)


print(o2_dec * co2_dec)