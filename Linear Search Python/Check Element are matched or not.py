def SearchElement(arr,element):

    for i in range(len(arr)):
        if arr[i]==element:
            return f"Element are Matched!"

    return f"Element are not Matched!"

arr = [5,6,8,7,4,9,3,1]
n = 900
print(SearchElement(arr,n))