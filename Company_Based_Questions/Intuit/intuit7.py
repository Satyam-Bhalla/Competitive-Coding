
t = int(input())

for tc in range(t):
    l = int(input())
    array = input().split()
    for i in range(l): array[i] = int(array[i])

    start, end = 0, 1
    result = ""
    while end < l:
        if (end+1) == l:
          if array[start] < array[end]:
            result += "(" + str(start) + " " + str(end) + ")"
          break
    
        elif array[start] >= array[end]:
            start, end = start+1, end+1
    
        elif array[end] < array[end+1]:
            end += 1
    
        elif array[end] > array[end+1]:
            result += "(" + str(start) + " " + str(end) + ")" + " "
            start, end = end+1, end+2

    if result: print(result)
    else: print("No Profit")