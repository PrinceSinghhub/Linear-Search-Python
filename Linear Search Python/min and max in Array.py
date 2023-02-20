def Find_Min_Max(arr):
    min = arr[0]
    max = arr[0]

    for i in arr:
        if i < min:
            min = i

    for j in arr:
        if j>max:
            max = j

    return f"Min: {min} Max: {max}"


arr = [5,6,8,7,4,9,3,1,0,-1,800]
print(Find_Min_Max(arr))