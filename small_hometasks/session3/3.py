def count_letters(src_str):
    ch_dict = {}
    while len(src_str) > 0:
        ch = src_str[0]
        num = src_str.count(ch)
        ch_dict[ch] = num
        temp = ''
        for i in src_str:
            if not i == ch:
                temp += i
        src_str = temp        
    return ch_dict