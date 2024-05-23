

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