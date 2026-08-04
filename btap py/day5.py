#ex1 kiểm tra tính đối xứng Viết một hàm có tên palindrome kiểm tra tính đối xứng. Hàm trả True nếu đối
# xứng, False nếu không đối xứng. -> Lấy chuỗi đảo ngược bằng s[::-1] So sánh với chuỗi gốc
def palindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
text = input("Text :  ")
print(palindrome(text))

#ex2 Viết một chương trình chấp nhận chuỗi từ do người dùng nhập vào, phân tách nhau 
# bởi dấu phẩy và in những từ đó thành chuỗi theo thứ tự bảng chữ cái, phân tách
# nhau bằng dấu phẩy. 
# phần này mới biết ạ. nên code khong chạy ạ.
# Tách bằng split(",")khoảng trắng dư thừa bằng strip()sắp xếp bằng sorted()ghép bằng ",".join(list)
def s_words(text):
    words = [w.strip() for w in text.split(",")]
    words = sorted(words)
    return ",".join(words)
s = input("words : ")
print(s_words(s))

#ex3 Viết một hàm đếm tần số xuất hiện mỗi từ trong một file. Ghi ra file trên mỗi
# dòng là từ và tần số xuất hiện của từ đó. bài này e cần gợi ý chút ạ











#ex4 Thiết kế trò chơi đoán từ vựng như chiếc nón kỳ diệu.
# Máy tính sẽ hiện các ô chữ tương ứng với số chữ cái của từ bí mật.
# Ví dụ:
# Tên một loài động vật bơi ở biển có 4 chữ cái ?
#Từ bí mật là Fish gồm 4 chữ cái
#phan tich người chơi đoán từng chữ cái đoán đúng → chữ cái mở đoán sai → mất lượt (if)đoán hết chữ → thắng. lặp cho tới khi đoán hếthết
def hangman(secret):
    secret = secret.lower()
    guessed = ["_"] * len(secret)
    attempts = 5
    print("Welcome to Hangman!")
    print("Secret words have ", len(secret), "alphabet")
    print(" ".join(guessed))
    while attempts > 0:
        guess = input("insert 1 alp : ").lower()
        if guess in secret:
            print("that's right!")
            for i in range(len(secret)):
                if secret[i] == guess:
                    guessed[i] = guess
        else:
            attempts -= 1
            print("wrong! U have", attempts, "turn")

        print(" ".join(guessed))
        if "_" not in guessed:
            print("Conglatulations", secret)
            return True

    print("U lose! secret is :", secret)
    return False

hangman("tuyetlien")

#ex5 Viết chương trình tìm tất cả các số chia hết cho 7 nhưng không phải bội số của 5, nằm trong đoạn 2000 và 3200 (tính cả 2000 và 3200). 
# Các số thu được sẽ được in thành chuỗi trên một dòng, cách nhau bằng dấu phẩy
#phan tich x % 7==0 x % 5 !=0 tu 2000 -> 3201 range(2000, 3201) chuoi .join

def number():
    result = []
    for a in range (2000, 3201):
        if a % 7 ==0 and a % 5 != 0 :
            result.append(str(a))
    return ",".join(result)
print(number())
#ex6 Viết một chương trình có thể tính giai thừa của một số cho trước. Kết quả được in thành chuỗi trên một dòng, phân tách bởi dấu phẩy.
# Ví dụ, số cho trước là 8 thì kết quả đầu ra phải là 40320.
# phan tich dùng for và str cho kq
def numbers(n):
    result = 1
    for a in range(1, n + 1 ):
        result *= a
    return str(result)
num = int(input("num is : "))
print(numbers(num))

#ex7 Viết chương trình giải bài toán Bài toán Tháp Hà Nội (Tower of Hanoi)
# n đĩa chuyển a qua c địa nhỏ trên lớn 1 lần 1 đĩa đệ quy 
# đệ quy Đệ quy (Recursion) trong lập trình đơn giản là một hàm tự gọi lại chính nó để giải quyết một bài toán lớn
# bằng cách chia nhỏ nó thành các bài toán con tương tự.
# hieu A(n, A, B, C): A(n-1, A, C, B) Move A → C A(n-1, B, A, C)
def hanoi(n, start, temp, end):
    if n == 1:
        print(f"Move disk 1 from {start} to {end}")
        return
    hanoi(n - 1, start, end, temp)
    print(f"Move disk {n} from {start} to {end}")
    hanoi(n - 1, temp, start, end)
n = int(input("mount: "))
hanoi(n, "A", "B", "C")

