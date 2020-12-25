arr=[0,1,4,13,15,12,16]
d={a:[i] for i,a in enumerate(arr)}
print(d)
lst=arr[-1]
for i in range(len(arr),30000000):
    if len(d[lst])==1:
        spoken=0
    else:
        spoken=d[lst][-1]-d[lst][-2]
    if spoken in d:
        d[spoken].append(i)
    else:
        d[spoken]=[i]
    lst=spoken
print(spoken)
