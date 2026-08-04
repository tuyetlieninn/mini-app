#ex9
#Viết một chương trình xóa tất cả phần tử lặp lại (trùng lặp) ra khỏi danh sách.
def remove_duplicates(nums):
    result = []
    for x in nums:
        if x not in result:
            result.append(x)
    return result
nums = list(map(int, input().split()))
print(remove_duplicates(nums))

#ex10
#Viết một chương trình in ra các số chia hết cho 7 nhưng không chia hết cho 5
#nằm trong khoảng 100 cho đến 1000 (tính cả 100 và 1000).

def get_nums():
    result = []
    for x in range(100, 1001):
        if x % 7 == 0 and x % 5 != 0:
            result.append(x)
    return result

print(get_nums())

#ex11
#Viết một chương trình in tất cả các số nguyên tố nhỏ hơn n.
# Với n là số nguyên dương nhập từ bàn phím.  bài này em không chắc 
def is_a(x):
    if x <2:
        return False
    for i in range(2,int(x*0.5)+1):
        if x% i == 0:
            return False
    return True
def get_b(y):
    result = []
    for x in range(2, n):
        if is_a(x):
            result.append(x)
    return result
n= int(input())
print(get_b(n))

#exex12Cho một danh sách số nguyên: [5, 10, 15, 20, 25, 46]
# Tìm giá trị lớn nhất và nhỏ nhất của danh sách. Không được sử dụng hàm max() và min()
nums[5,10,15,20,25,4646]
def min_max(nums):
    smallest = nums[0]
    largest = nums[0]
    for x in nums:
        if x< smallest:
            smallest ==x
        elif x > largest:
            largest == x
    return smallest, largest
print(min_max(nums))

