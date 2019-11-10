def correlate_dicts(*dicts):
    dest_dict = {}
    for inst in dicts:
        for item in inst.items():
            if item[0] in dest_dict:
                dest_dict[item[0]] += item[1]
            else:
                dest_dict[item[0]] = item[1]
    return dest_dict