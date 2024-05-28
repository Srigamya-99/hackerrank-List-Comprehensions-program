#linear search
nums=[12,10,6,26,321]
target=26
falg=-1
n=len(nums)
for index in range(n):
    if nums[index]==target:
        flag=index
        break
if flag==-1:
    print("Not Found")
else:
    print("Target Found at:", flag)
        
