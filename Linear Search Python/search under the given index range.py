def SearchInRange(nums,find,s,e):

    r = 0
    for i in range(s,e+1):
        if nums[i]==find:
            print("Element are Found! in Given Range")
            r+=1
    if(r==0):
        print("Sorry Element are not Found! in Given Range")

arr = [5,6,8,7,4,9,3,1]
n= 1
s = 2
e = 7
SearchInRange(arr,n,s,e)