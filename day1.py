#test1

print(3 + 1)        
print(3 * 3)        
print(2 ** 3)       
print("Hello, world!")


#ex1
#Cho một số nguyên, in "YES" nếu chữ số cuối của nó là 7 và in "NO" nếu không.
a=int(input("..."))
if a % 10 == 7:
    print("yes")
else:
    print("no")    

#ex2 
# Cho biết tọa độ của ba điểm A, B, C trên một đoạn thẳng. In khoảng cách từ điểm
# A đến điểm gần nó nhất.
A = int(input("A = "))
B = int(input("B = "))
C = int(input("C = "))
distB = abs(A - B)
distC = abs(A - C)

print(min(distB, distC))

#ex3
#Viết chương trình tính tổng các số trong một danh sách
numbers = [2, 5, 8, 10, 12]
total = sum(numbers)
print("Sum =", total)


#ex4
#Viết game đoán số may mắn (guess the number)
#Máy tính nghĩ một số random từ 1 cho đến 15 và hỏi bạn đoán. Máy tính sẽ nói
#cho bạn khi bạn đoán sai là số may mắn là phải lớn hơn hoặc nhỏ hơn. Bạn sẽ
#chiến thắng nếu bạn đoán đúng số đó trong 5 lượt chơi.
import random

random_num = random.randint(1, 15)
attempts = 5

print("From 1 to 15. UU have 5 choices.")

for i in range(attempts):
    guess = int(input(f"Turn {i+1}, enter your guess: "))

    if guess == random_num:
        print("Congratulations! CCorrectly!")
        break
    elif guess < random_num:
        print("No! Higher")
    else:
        print("No! Lower")

else:
    print("Game over.")
    print("LLucky number is", random_num)

#ex5
#Một cửa hàng sẽ giảm giá 10% nếu tổng chi phí mua hàng lớn hơn 10.000
#Người dùng về số lượng từ bàn phím
#Giả sử, một đơn vị mặt hàng sẽ có giá 100 đồng.
#In tổng chi phí hóa đơn cho người dùng.

sl = int(input("Enter quantity: "))
price = sl * 100

if price > 10000:
    price = price * 0.9  

print("Total cost =", int(price))



