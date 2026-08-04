#ex1 Làm game chọn nhóm. Có một danh sách gồm 8 người chơi, hãy lựa chọn ngẫu 
# nhiên 4 người chơi không trùng nhau để cho vào nhóm A, còn lại cho vào nhóm BB
#1
import random
players = [ "1", "2", "3", "4", "5", "6", "7", "8"]
random.shuffle(players)
grA = players[:4]
grB = players[4:]
print("grA:")
for i in grA:
    print(i)
print("grB:")
for i in grB:
    print(i)
#2 
import random
def grs(players):
    random.shuffle(players)
    return players[:4], players[4:]
players = [ "1", "2", "3", "4", "5", "6", "7", "8"]
groupA, groupB = grs(players)
print("Group A:", groupA)
print("Group B:", groupB)

#ex2 Tìm vị trí của giá trị chẵn đầu tiên trong mảng 1 chiều các số nguyên. 
# Nếu mảng không có giá trị chẵn thì sẽ trả về -1
def first_nums(so):
    for i in range(len(so)):
        if so[i] % 2 == 0:
            return i, so[i]
    return -1
so = list(map(int, input().split()))
result, value = first_nums(so)
print(result)
print(value)

#ex3 Viết chương trình tính tổng S = 1 + 1/2 + 1/3 + ...+ 1/n với n là số nguyên dương nhập từ bàn phím.
#  bài này e cần gợi ý hơn tại không chắcchắc
def total(a):
    S = 0
    for i in range(1, a + 1):
        S += 1 / i
    return S
a = int(input("nums a : "))
result = total(a)
print(result)

#ex4 Liệt kê tất cả các ước số của số nguyên dương n.
def num(a):
    result = []
    for i in range (1, a + 1):
       if a % i == 0:
         result.append(i)
    return result
a = int(input("nums : "))
numlist = num(a)
print(numlist)

#ex5 Phân tích một số thành tích các thừa số nguyên tố
def nums(a):
    result = []
    i = 2
    while i <= a:
        while a % i == 0:
          result.append(i)
          a //= i
        i += 1
    return result
a = int(input("nums :"))  
lst = nums(a)
print(lst)



#ex6 You are driving a little too fast, and a police officer stops you. Write code to
# compute the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big
# ticket. If speed is 60 or less, the result is 0. If speed is between 61 and 80
# inclusive, the result is 1. If speed is 81 or more, the result is 2. Unless it is your
# birthday -- on that day, your speed can be 5 higher in all cases.
# => bỉthday speed -5 check speed => 0 1 2 

def ticket(speed, birthday):
    if birthday:
        speed -= 5
    if speed <= 60:
        return 0
    elif speed <= 80:
        return 1
    else:
        return 2
speed = int(input("V :"))
check_birth = input ("birthday ? (Y/N :) ")
birthday = (check_birth.lower() == "Y")
result = ticket(speed, birthday)
print(result)

#ex7 Given 3 int values, a b c, return their sum. However, if one of the values is 13
#then it does not count towards the sum and values to its right do not count. So
#for example, if b is 13, then both b and c do not count.
# hieu la tổng a b c (neu a = 13 không tính b = 13 không tính b c nếu = 13 khong tinh c)


def nums(a, b, c):
    if a == 13:
        return 0
    if b == 13:
        return a
    if c == 13:
        return sum([a, b])
    return sum([a, b, c ])
a = int(input("a= "))
b = int(input("b= "))
c = int(input("c= "))
print(nums(a, b, c))


#ex8 Sắp xếp mảng 1 chiều tăng dần (khong dung sortsort) ? cần check ạ

def nums(num):
    n = len(num)
    for i in range(n):
        for k in range(0, n - i - 1):
            if num[k] > num[k + 1]:
                num[k], num[k + 1] = num[k + 1], num[k]
    return num  

listnums = list(map(int, input("nums: ").split()))
result = nums(listnums)
print(result)

#ex9 Given a string, return a new string where the first and last chars have been exchanged.
# đầu cuối thay đổi đầu a[0] giữa[1,-1] cuối[-11]
def moji(aa):
    if len(aa) <= 1:
        return aa
    return aa[-1] + aa[1:-1] + aa[0]
text = input("Text:  ")
print(moji(text))

#ex10 Viết chương trình nhập vào bán kính đường tròn, tính toán và in ra chu vi và diện
# tích hình tròn. C = 2pir SS=pỉr^2 pi = math.pi

import math
def circle(r):
    C = 2 * math.pi * r
    S = math.pi * r * r
    return C, S
r = int(input("R = "))
C, S = circle(r)
print("C : ")
print("S : ")

#ex11 Làm trò chơi búa, đá, giấy Người chơi có 5 lượt chơi với máy tính, sau 5 lượt chơi thì thống kê người chơi
# đã thắng, hòa, thua bao nhiêu lượt với máy tính. 0 bua 1 keo 2 bao

import random
def user(player, lap):
    if player == lap :
        return "draw"
    if (player == 0 and lap == 1) or \
       (player == 1 and lap == 2) or \
       (player == 2 and lap == 0):
        return "win"
    return "lose"
wins = 0
draws = 0
loses = 0
print("0 : Hammer  1 : Scissors 2 :Paper")
for i in range(5):
    print(f"\nround {i+1}:")
    player = int(input("your turn 0  1  2 "))
    lap = random.randint(0, 2)
    print("lap turn", lap)
    
    result = user(player, lap)

    if result == "win":
        print("you win!")
        wins +=1
    elif result == "draw":
        print("Draw")
        draws += 1
    else:
        print("You Lose!")
        loses += 1
print(  "   Total   "  )
print ("Win:", wins)
print(" Draw:",draws)
print("Loses",loses)

#ex12 Viết một hàm có tên capital_indexes. Hàm nhận một tham số duy nhất là một
#chuỗi. Hàm của bạn sẽ trả về một danh sách tất cả các chỉ số (index) trong chuỗi
#có chữ in hoa.
def capital_indexes(s):
    result = []
    for i in range(len(s)):
        if s[i].isupper():
            result.append(i)
    return result

text = input("Text: ")
print(capital_indexes(text))
