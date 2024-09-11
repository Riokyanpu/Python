# coding: utf-8
# if文による条件分岐
number = 2
if number == 1:
    print( "成功")  #条件式が成立したときの処理
else:
    print( "失敗")  #条件式が成立しなかったときの処理
    
# coding: utf-8
# if文による条件分岐
import random
number = random.randint(1,5) * 100
print("あなたの得点は" + str(number) + "ポイントです")
if number == 500:
    print("ok!")
elif number ==400:
    print("そこそこ")    
elif number ==200:
    print("どちらでもない")        
else:
    print("NO") 