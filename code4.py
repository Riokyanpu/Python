# coding: utf-8
# if文による条件分岐
number = 2
if number == 1:
    print( "成功")  #条件式が成立したときの処理
else:
    print( "失敗")  #条件式が成立しなかったときの処理

import random
number = random.randint(1, 3)
print("あなたの順位は" + str(number) + "位です")
if number == 1:
    print("おめでとう")

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

import random
number = random.randint(1,3)
if number == 1:
	print( "")	#条件式が成立したときの処理
elif number == 2:
    print("Neither") # 条件式2が成立した時の処理(ニーザーどちらでもない)
else:
	print( "キライ")	#条件式がどれも成立しなかったときの処理


import random
number = random.randint(1, 5)
print("あなたの順位は" + str(number) + "位です")
if number == 1:
    print("おめでとう")
elif number == 2:
    print("あと少し")
else:
    print("よくがんばったね")

# if文による条件分岐　比較演算子
import random
time = random.randint(1,24)
if time < 12:
	print("午前中")	#条件式が成立したときの処理
elif time == 12:
    print("正午!")
elif time > 12:
    print("午後!")


import random
age = random.randint(18, 22)    # ageに、何才かを18~22の範囲でランダムに代入
text = "飲酒不可"
if age >= 20:
    print(str(age) + "才は飲酒可能")
else:
    # それ以外だったときの処理
    print(str(age) + "才は" + text)
