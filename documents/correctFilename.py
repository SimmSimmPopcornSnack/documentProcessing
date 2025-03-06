import os

def circled_number_to_int(circled_num):
    # Unicode offset: '⑩' (0x2469) corresponds to 10
    if '①' <= circled_num <= '⑳':  # Covers 1 to 20
        return ord(circled_num) - 0x2460 + 1
    elif '㉑' <= circled_num <= '㉟':  # Covers 21 to 35
        return ord(circled_num) - 0x3250 + 21
    elif '㊱' <= circled_num <= '㊿':  # 36 to 50 (Unicode: U+32B0 to U+32BF)
        return ord(circled_num) - 0x32B0 + 36
    else:
        raise ValueError("Unsupported circled number")

def include_circled_number(str):
    ret = []
    for s in str:
        if ('①' <= s <= '⑳') or ('㉑' <= s <= '㉟') or ('㊱' <= s <= '㊿'):
            ret.append(s)
    return ret

directory = ".\documents\input"
os.chdir(directory)
for filename in os.listdir('.'):
    cir_num = include_circled_number(filename)
    if len(cir_num) > 0:
        s = cir_num[0]
        s_num = str(circled_number_to_int(s))
        filename_new = filename.replace(s, s_num + " ")
        os.rename(filename, filename_new)
