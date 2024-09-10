# coding: utf-8

# 変数の文字列を連結
player = "勇者"
print(player + "は、レベルアップした")

number = 300
print("スライム" + str(number) + "匹ある")

#1から100までの整
import random
number = random.randint(1,100)
print("スライム" + str(number) + "匹ある")

# 1から6のサイコロを作る
import random
number = random.randint(1,6)
print("サイコロの目は" + str(number) +"です。")

# coding: utf-8
#モンスターに与えるダメージを出力！
import random
number = random.randint(50,99)
print("モンスターに、" + str(number) + "のダメージを与えた。")
print("敵に、" + str(number) + "のダメージを与えた。")
# coding: utf-8
import random

# 1から10の間のランダムな匹数を生成する
number = random.randint(1, 10)  # 匹数 1 ～ 10

# 計算する
number = (100 + 5 * 4)
print(number)
print(number - 70)

#値段を計算する
apple_price = 350	#リンゴの単価
apple_num = 5	#リンゴを買う数
print("りんごの単価:" + str(apple_price) + "円")
print("りんごを買う数:" + str(apple_num) + "個")
total = apple_price * apple_num
print("合計金額" + str(total) + "円")

import random
grapes_price = random.randint(1,5) * 100	#ぶどうの単価
grapes_num = random.randint(1,10)	#ぶどうを買う数
print("ぶどうの単価:" + str(grapes_price) + "円")
print("ぶどうを買う数:" + str(grapes_num) + "個")
total = grapes_price * grapes_num
print("合計金額" + str(total) + "円")

#体重の計算
import random
number = random.randint(1, 10)	# 匹数 1 ～ 10
print("体重100キロのスライムが" + str(number) + "匹あらわれた")
# 合計体重 = 匹数 x 100
total = number * 100
print("スライムの合計体重は" + str(total) + "キロです")

# 匹数を表示する
print("体重100キロのスライムが" + str(number) + "匹あらわれた")

# 合計体重を計算する
total = number * 100

# 合計体重を表示する
print("スライムの合計体重は" + str(total) + "キロです")

# coding: utf-8
# データの種類
number = 100 + 30		#数値
strings = "ハロー" + "paiza"	#文字列
print(number)
print(strings)
print(str(number) + strings)
print(number + 70)