def apply_mask(num, mask):
    num = list(bin(num)[2:].zfill(36))
    x_locs = []
    for i in range(36):
        if mask[i] != '0':
            if mask[i] == 'X':
                x_locs.append(i)
            num[i] = mask[i]

    res = set()
    for key in [bin(x)[2:].zfill(len(x_locs)) for x in range(2**len(x_locs))]:
        temp_num = list(num)
        for i in range(len(x_locs)):
            temp_num[x_locs[i]] = key[i]
        res.add(int(''.join(temp_num), 2))

    return res


with open('202014.txt') as fin:
    finished = False
    mem = {}
    while not finished:
        mask_finished = False
        while not mask_finished:
            lst = fin.readline().strip().split(' = ')
            if lst[0] == 'mask':
                mask_finished = True
                mask = lst[1]
            elif not lst[0]:
                mask_finished = True
                finished = True
            else:
                orig_address = int(lst[0][4:-1])
                val = int(lst[1])
                for address in apply_mask(orig_address, mask):
                    mem[address] = val

    print(sum(mem.values()))
