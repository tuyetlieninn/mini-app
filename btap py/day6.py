#ex1 You are given two integers n and k Construct a binary string s of length n
#such that both of the following conditions hold:
#The absolute difference between the number of characters 0 and the number of characters 1 in s is at most 1
#There are exactly k pairs of adjacent equal characters in s Formally, there are exactly k indices i( 1≤i≤n−1) satisfying si=si+1
#Or determine that no such string exists.
#phan tich sang tieng viet chuỗi số nhị phân cân bằng 1 và 0 có k cặp kí tự liền kề giống nhau?
# 0 = 1 -> n chẵn = n/2  lẻ (n+1)/2 và (n-1)/2 ?
# k cặp giống nhau 00 11 ?
# thiệc là bài này 80% e tham khảo AI ạạ
def construct_string(n, k):
    if n % 2 == 0:
        c0 = c1 = n // 2
    else:
        c0 = n // 2 + 1
        c1 = n // 2
    max_k = (c0 - 1) + (c1 - 1)
    if k > max_k:
        return None  
    if k == 0:
        s = []
        for i in range(n):
            s.append('0' if i % 2 == 0 else '1')
        return ''.join(s)
    if k <= c0 - 1:
        block = '0' * (k + 1)
        c0 -= (k + 1)
    else:
        block = '1' * (k + 1)
        c1 -= (k + 1)
    rest = []
    turn = '1' if block[0] == '0' else '0'
    while c0 > 0 or c1 > 0:
        if turn == '0' and c0 > 0:
            rest.append('0')
            c0 -= 1
        elif turn == '1' and c1 > 0:
            rest.append('1')
            c1 -= 1
        turn = '0' if turn == '1' else '1'

    return block + ''.join(rest)

numss = int(input()) 
numsss = int(input())

print(construct_string(numss, numsss ))

#You are given an array a of length n consisting only of −1 and 1. You may perform the following operation on a
#any number of times: Choose an index i satisfying 1≤i≤n−1. Assign ai=−ai and ai+1=−ai+1

#ex2  Viết chương trình sinh các xâu nhị phân có độ dài n.
n = int(input("n: "))
for x in range(2 ** n):
    s = bin(x)[2:]          
    s = s.zfill(n)          
    print(s)

#ex3  Viết một chương trình nhập vào một danh sách các số và tạo một danh sách mới chỉ gồm phần tử đầu tiên và cuối cùng của danh sách đó. Viết chương trình sử dụng hàm.
def first_last(nums):
    if len(nums) == 0:
        return []          
    if len(nums) == 1:
        return [nums[0]]   
    return [nums[0], nums[-1]]
lst = list(map(int, input("list: ").split()))
result = first_last(lst)
print("new list:", result)

#ex4 A bigram in a string is a pair of adjacent characters. For example, the string helloello contains 8 bigrams: he, el, ll, lo, oe, el, ll, lo.

#Monocarp has cards with letters: c1 cards with the letter a, c2 cards with the letter b, ..., ck cards with the k
# -th letter of the Latin alphabet. He wants to make a string from these cards, using each card exactly once. The resulting string must contain at least two equal bigrams. The order of characters in each bigram matters; for example, the string aba does not have two equal bigrams.

#Determine whether it is possible to make a string that satisfies these requirements.
#phan tich tạo chuỗi kí tự liên tiếp mỗi bigram 1 lần n tổng -> tổng n-1 khác tối đa k^2 -> không trùng n-1<= k^2 ngược lại

t = int(input())
for _ in range(t):
    k = int(input())
    c = list(map(int, input().split()))
    n = sum(c) 
    if n - 1 > k * k:
        print("YES")
    else:
        print("NO")


