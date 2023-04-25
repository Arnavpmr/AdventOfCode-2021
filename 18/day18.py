import math
import ast

data = open("input.txt", "r").readlines()

data = [line.rstrip("\n") for line in data]


def replace(string, new_string, start, end): #replaces string from start to end with new string (including start to end)
    return string[:start] + new_string + string[end+1:]


def add_nums(num1, num2):
    return "[{0},{1}]".format(num1, num2)


def find_split(start, end, str1):
    str1 = str1[start+1:end]

    elem1, elem2 = str1.split(",", 1)

    if '[' not in elem1 and ']' not in elem1 and int(elem1) >= 10:
        return (start+1, start+len(elem1))
    elif '[' not in elem2 and ']' not in elem2 and int(elem2) >= 10:
        return (start+len(elem1)+2, start+len(elem1)+len(elem2)+1)
    else:
        return "-1"


def perform_split(start, end, str1):
    num = int(str1[start:end+1])
    new_string = "[{0},{1}]".format(num//2, math.ceil(num/2))

    return replace(str1, new_string, start, end)


def magnitude(data):
    if isinstance(data, int):
        return data
    else:
        return 3*magnitude(data[0]) + 2*magnitude(data[1])


def explode(str1):
    def find_left_val():
        pos = start

        while True:
            if str1[pos].isdigit():
                if str1[pos-1].isdigit():
                    return pos-1, pos
                
                return pos, pos

            pos -= 1

            if pos < 0: break
        
        return -1, -1


    def find_right_val(): 
        pos = end

        while True:
            if str1[pos].isdigit():
                if str1[pos+1].isdigit():
                    return pos, pos+1
                
                return pos, pos

            pos += 1

            if pos == len(str1): break
        
        return -1, -1

    openings_pos = []
    depth = 0

    for i in range(len(str1)):
        if str1[i] == "[":
            openings_pos.append(i)
            depth += 1
        elif str1[i] == "]":
            start, end = openings_pos.pop(), i
            
            if depth > 4: #explode
                elem1, elem2 = str1[start+1:end].split(",")

                result_left_start, result_left_end = find_left_val()

                if result_left_start != -1 and result_left_end != -1 and elem1.isdigit():
                    old_num = str1[result_left_start:result_left_end+1]
                    new_num = str(int(old_num)+int(elem1))
                    str1 = replace(str1, new_num, result_left_start, result_left_end)
                    start += len(new_num) - len(old_num)
                    end += len(new_num) - len(old_num)
                
                result_right_start, result_right_end = find_right_val()

                if result_right_start != -1 and result_right_end != -1 and elem2.isdigit():
                    new_num = str(int(str1[result_right_start:result_right_end+1])+int(elem2))
                    str1 = replace(str1, new_num, result_right_start, result_right_end)

                return replace(str1, "0", start, end)
            
            depth -= 1
    
    return "-1"


def split(str1):
    num = ""
    for i in range(len(str1)):
        if str1[i].isdigit():
            num = str1[i] + str1[i+1] if str1[i+1].isdigit() else str1[i]

            if int(num) >= 10:
                str1 = perform_split(i, i+len(num)-1, str1)

                return str1
    
    return "-1"


def reduce_num(raw_snail_num):
    explode_result = explode(raw_snail_num)
    split_result = split(raw_snail_num)

    if explode_result != "-1":
        return reduce_num(explode_result)
    elif split_result != "-1":
        return reduce_num(split_result)
    else:
        return raw_snail_num

raw_snail_num = data[0]

for line in data[1:]:
    raw_snail_num = reduce_num(add_nums(raw_snail_num, line))

print(magnitude(ast.literal_eval(raw_snail_num)))

largest_mag = -1

for line in data:
    for line2 in data:
        if line == line2: continue

        largest_mag = max(largest_mag, magnitude(ast.literal_eval(reduce_num(add_nums(line, line2)))))

print(largest_mag)