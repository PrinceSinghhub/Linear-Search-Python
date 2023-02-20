def linearSearch(nums,n):
    r=0
    for i in nums:
        if i == n:
            print("Element are Found!")
            r+=1
    if(r==0):
        print("Element are not found!")


arr = [5,6,8,7,4,9,3,1]
n= 800
linearSearch(arr,n)
