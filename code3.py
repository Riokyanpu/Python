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
print(number * 20)