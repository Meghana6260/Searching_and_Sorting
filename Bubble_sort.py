# BUBBLE SORT 
def performbubblesort(nums):
    n=len(nums)
    #n=6
    #fixing the index position 
    for fixindex in range (n-1,0,-1):
        for index in range(fixindex):
            # 0 1 2 3 4
            if nums[index]>nums[index+1]:
                temp=nums[index]
                nums[index]=nums[index+1]
                nums[index+1]=temp 
        print(nums)   
num=list(map(int,input().split()))         
nums=[1,560,38,3,65,87,9]
print("befor sorting:")
print(nums)
performbubblesort(nums)
print("after sorting")
print(nums)
