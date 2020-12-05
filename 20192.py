f = open("20192.txt","r")
f = f.read()
f = f.split(",")
print(f)
program = []
for i in f:
    program.append(int(i))

program_1 = program



def do_program(n,v):
    program[1] = n
    program[2] = v
    pos = 0
    try:
        while True:
            if program[pos] == 1:
                program[program[pos+3]] = program[program[pos+1]]+program[program[pos+2]]
            if program[pos] == 2:
                program[program[pos+3]] = program[program[pos+1]]*program[program[pos+2]]
            if program[pos] == 99:
                break
            pos = pos+4
        if program[0] == 19690720:
            print(n)
            print(v)
            exit()
    except:
        print(len(program)*len(program)-n*len(program)-v)

for i in range(len(program)):
    for j in range(len(program)):
        do_program(i,j)
         program = program_1
        
