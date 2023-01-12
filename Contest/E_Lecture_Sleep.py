secret = int(input().split(" ")[1])
therom = list(map(lambda num: int(num) , input().split(" ")))
wake =list(map(lambda num: int(num) , input().split(" ")))
maxsum, currentsum  = 0, 0
left, right = 0, 0
for indx, value in enumerate(wake):
    if value == 1:
        currentsum += therom[indx]
maxsum = currentsum
while right < len(wake):
    while right < secret:
        if wake[right] == 0:
            currentsum += therom[right]
        maxsum = max(maxsum, currentsum)
        right += 1
    if wake[left] == 0:
        currentsum -= therom[left]
    if right < len(wake) and wake[right] == 0:
        currentsum += therom[right]
    maxsum = max(maxsum, currentsum)
    left += 1
    right += 1
print(maxsum)