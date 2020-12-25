inp = open('202019.txt').read()
 
def z(msg, rule):
    if type(rules[rule]) == str:
        if msg and msg[0] == rules[rule]:
            return [msg[1:]]
    else:
        a = []
        for b in rules[rule]:
            zm = [msg]
            for r in b:
                zm2 = []
                for x in zm:
                    if r == 'a':
                        print(rule, rules[rule])
                    zm2 += z(x, r)
                zm = zm2
                if not zm:
                    break
            if zm:
                a += zm
        return a
    return []
 
rules, msgs = inp.split('\n\n')
rules = rules.split('\n')
msgs = msgs.split('\n')
 
rules = {int(r.split(':')[0]):
            [[int(x) for x in sr.split()]
             for sr in r.split(':')[1].split('|')]
            if '"' not in r else r[-2]
         for r in rules}
 
print(sum('' in z(msg, 0) for msg in msgs))
 
rules[8] = [[42], [42, 8]]
rules[11] = [[42, 31], [42, 11, 31]]
 
print(sum('' in z(msg, 0) for msg in msgs))
