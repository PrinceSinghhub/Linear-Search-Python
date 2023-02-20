def SearchElement(arr,element):

    for i in range(len(arr)):
        if arr[i]==element:
            return f"The index of given element is: {i}"

    return False

arr = [5,6,8,7,4,9,3,1]
n = 9
print(SearchElement(arr,n))