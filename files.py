mat = []
f = open("file.txt", "r")
for line in f:
    mat.append(line.replace('\n', '').split(' '))
for i in range(len(mat[0])):
    new_line=[]
    for j in range(len(mat)):
        new_line.append(mat[j][i])
    print(' '.join(new_line))