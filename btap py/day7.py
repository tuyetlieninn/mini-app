#ex1ex1
#Sometimes some words like "localization" or "internationalization" are so long that writing them many times in one text is quite tiresome.

#Let's consider a word too long, if its length is strictly more than 10 characters. All too long words should be replaced with a special abbreviation.

#This abbreviation is made like this: we write down the first and the last letter of a word and between them we write the number of letters between the first and the last letters. That number is in decimal system and doesn't contain any leading zeroes.

#Thus, "localization" will be spelt as "l10n", and "internationalization» will be spelt as "i18n".

#You are suggested to automatize the process of changing the words with abbreviations. At that all too long words should be replaced by the abbreviation and the words that are not too long should not undergo any changes.

#từ dài hơn 10 viết tắt chữ đầu kí tự giữua chữ cuối

def check_word(word):
    if len(word) > 10:
        return word[0] + str(len(word) - 2) + word[-1]
    return word
word = input("word is: ")
print(check_word(word))

#ex2 The classic programming language of Bitland is Bit++. This language is so peculiar and complicated.

#The language is that peculiar as it has exactly one variable, called x. Also, there are two operations:Operation ++ increases the value of variable x by 1.Operation -- decreases the value of variable x by 1.
#A statement in language Bit++ is a sequence, consisting of exactly one operation and one variable x. The statement is written without spaces, that is, it can only contain characters "+", "-", "X". Executing a statement means applying the operation it contains.

#A programme in Bit++ is a sequence of statements, each of them needs to be executed. Executing a programme means executing all the statements it contains.

#You're given a programme in language Bit++. The initial value of x is 0. Execute the programme and find its final value (the value of the variable when this programme is executed).
# ++ là +1 -- trừ 1

n = int(input())
x = 0
for _ in range(n):
    s = input()
    if "++" in s:
       x += 1
    else:
       x -= 1
print(x)
   

#One day three best friends Petya, Vasya and Tonya decided to form a team and take part in programming contests. Participants are usually offered several problems during programming contests. Long before the start the friends decided that they will implement a problem if at least two of them are sure about the solution. Otherwise, the friends won't write the problem's solution.

#This contest offers n problems to the participants. For each problem we know, which friend is sure about the solution. Help the friends find the number of problems for which they will write a solution.

