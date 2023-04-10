matrix= [] 
n = int(input())
for _ in range(n):
    matrix.append(list(map(int, input().split())))
sink = []
for row in range(n):
    count_sink = 0
    for col in range(n):
        if matrix[row][col] != 0:
            count_sink += 1
            break
    if count_sink == 0:
        sink.append(row + 1)
sink.sort()

source = []
for col in range(n):
    count_source = 0
    for row in range(n):
        if matrix[row][col] != 0:
            count_source += 1
            break
    if count_source == 0:
         source.append(col + 1)
source.sort()

print(len(source), *source)
print(len(sink), *sink)
