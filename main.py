scores = open("D:\Documents\KHTN\Junior\[CS420]Artificial_Intelligence\Project\-HCMUS-AI_Pj\map\map11.txt", "r")
# print(file.read())
# print(type(file.read()))
line = scores.readline()
mapsize = line.split("x")
n = int(mapsize[0])
m = int(mapsize[1])
print("n = ",n," m= ",m)

map = []
i =0
j =0
while j < n:
    row = []
    line = scores.readline()
    digit = line.split(",")
    while i < m:
        row.append(int(digit[i]))
        i +=1
    map.append(row)
    j +=1
    i = 0
print(map[2][5],"hyh")

