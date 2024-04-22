## INSERTION SORT ##
nums=[1,78,9,23,7,0,992]
def performINsertionSort(nums):
    n=len(nums)
    for index in range(1,n):
        temp=nums[index]
        position=index-1
        while position>=0 and nums[position]>temp:
            nums[position+1]=nums[position]
            position-=1
        nums[position+1]=temp
        print(nums)            
print("before sorting")
print(nums)
performINsertionSort(nums)
print("after sorting")
print(nums)            
