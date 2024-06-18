# coding: utf-8
# if文による条件分岐
number = 2
if number ==1:
    print("OK!")  #条件式が成立したときの処理
else:
    print("NO")  #条件式が成立しなかったときの処理
    
# coding: utf-8
# if文による条件分岐
import random
number = random.randint(1,3) * 100
print("あなたの得点は" + str(number) + "ポイントです")
if number == 300:
    print("ok!")
elif number ==200:
    print("どちらでもない")    
else:
    print("NO") 