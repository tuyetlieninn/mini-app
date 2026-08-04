#ex6
# số chẵn
def get_evens(nums):
    evens = []
    for x in nums:
        if x % 2 == 0:
            evens.append(x)
    return evens
nums = list(map(int, input().split()))
print(get_evens(nums))

#ex7
#Tìm số lớn nhất 

def get_largest(nums):
    largest = nums[0]
    for x in nums:
        if x > largest:
            largest = x
    return largest
nums = list(map(int, input().split()))
print(get_largest(nums))


#ex8
#Lấy các số lớn hơn số đứng trước nó

def get_increasing(nums):
    result = []
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            result.append(nums[i])
    return result
nums = list(map(int, input().split()))
print(get_increasing(nums))
