from numpy import *
def two_dArray(nums,elenment):

    for i in range(len(nums)):
        for j in range(len(nums[i])):
            if nums[i][j] == elenment:
                return f"Element are found! in row: {i} collom: {j}"
    return "Sorry"

nums = zeros(shape=(2,3),dtype=int)
for i in range(len(nums)):
    for j in range(len(nums[i])):
        n = int(input("Enter Element: "))
        nums[i][j] = n
print(two_dArray(nums,5))