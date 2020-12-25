f = open("202019.txt","r")
f = f.read()
f = f.split("\n")
g = []
state = 0
rules = {}
messages = []
f = map(lambda s: s.strip(), open('202019.txt', 'r'))
for line in f:
    if not line:
        break
    r = line.split()
    rules[r[0][:-1]] = ' '.join(r[1:])
for line in f:
    if not line:
        break
    messages.append(line)


rules['8'] = '42 | 42 8'
rules['11'] = '42 31 | 42 11 31'



def loop(rulea, message):
    rule = rules[rulea]
    if len(rule) == 3:
        if not message:
            return []
        if message[0] == rule[1]:
            return [message[1:]]
        return []

    
    suffixes = []
    
    for alt in rule.split('|'):
        alt_suffixes = [message]
        
        for part in alt.split():
            alt_suffixes = [new_suffix for suffix in alt_suffixes for new_suffix in loop(part, suffix)]
            if not alt_suffixes:
                break
        suffixes += alt_suffixes

    
    return suffixes
    
    
c = 0

for message in messages:
    if "" in loop("0", message):
        c+=1

print(c)
    
    



