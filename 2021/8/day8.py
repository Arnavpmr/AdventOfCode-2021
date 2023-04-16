file = open("input.txt", "r")

def check_chars(str1, str2):
    for i in range(len(str1)):
        if str1[i] not in str2:
            return False
    
    return True


total = 0

for line in file:
    input = line.split(" | ")[0].rstrip("\n")
    output = line.split(" | ")[1].rstrip("\n")

    num = ""

    d = {}
    d_reverse = {}

    input_lst = input.split()

    for code in input_lst[::-1]:

        original_code = code

        code = "".join(sorted(code))

        if len(code) == 2:
            d[code] = 1
            d_reverse[1] = code
            input_lst.remove(original_code)
        elif len(code) == 4:
            d[code] = 4
            d_reverse[4] = code
            input_lst.remove(original_code)
        elif len(code) == 3:
            d[code] = 7
            d_reverse[7] = code
            input_lst.remove(original_code)
        elif len(code) == 7:
            d[code] = 8
            d_reverse[8] = code
            input_lst.remove(original_code)

    while len(input_lst) > 0:
        for code in input_lst[::-1]:

            original_code = code

            code = "".join(sorted(code))
            
            if len(code) == 5:
                if 1 in d_reverse and check_chars(sorted(d_reverse[1]), code):
                    d[code] = 3
                    d_reverse[3] = code
                    input_lst.remove(original_code)
                elif 6 in d_reverse:
                    if check_chars(code, sorted(d_reverse[6])):
                        d[code] = 5
                        d_reverse[5] = code
                        input_lst.remove(original_code)
                    else:
                        d[code] = 2
                        d_reverse[2] = code
                        input_lst.remove(original_code)
            elif len(code) == 6 and 1 in d_reverse:
                if check_chars(sorted(d_reverse[1]), code):
                    if 3 in d_reverse:
                        if check_chars(sorted(d_reverse[3]), code):
                            d[code] = 9
                            d_reverse[9] = code
                            input_lst.remove(original_code)
                        else:
                            d[code] = 0
                            d_reverse[0] = code
                            input_lst.remove(original_code)
                else:
                    d[code] = 6
                    d_reverse[6] = code
                    input_lst.remove(original_code)
    
    num = ""

    for out in output.split():
        num += str(d["".join(sorted(out))])

    total += int(num)
    
print(total)