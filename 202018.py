part2 = True
with open("202018.txt") as f:
    inp = f.read()

lines = [line for line in inp.split("\n") if line]




class T:
    def __init__(self, v):
        self.v = v
    def __add__(self, other):
        return T(self.v + other.v)
    def __sub__(self, other):
        return T(self.v * other.v)
    def __mul__(self, other):
        return T(self.v + other.v)



total = 0
for line in lines:
    for d in range(10):
        line = line.replace(f"{d}", f"T({d})")
    # here i replace multiplication with subtraction and when i multiply, it 
    line = line.replace("*", "-")
    if part2:
        line = line.replace("+", "*")
    t += eval(line, {"T": T}).v
print(total)


