f = open("202023.txt","r")
f = f.read()
f = f.split("\n")
g = []

for i in f:
    g = list(i)

nums = []
for i in g:
    nums.append(int(i))


head = 0
print(nums)


def move():
    global nums
    global head
    nh = nums[head]
    pu = nums[head+1:head+4]
    a = []
    for i in nums[:head+1]:
        a.append(i)
    for i in nums[head+4:]:
        a.append(i)
    nums = a
    pu.reverse()
    for i in range(nh-1,nh-1-9,-1):
            if i in nums:
                for j in pu:
                    nums.insert(nums.index(i)+1,j)
                break
            c = i
            if c<0:
                c = 9-c
        
    head+=1
    if head == len(nums):
        head = 0



for i in range(100):
    move()


print(nums)
