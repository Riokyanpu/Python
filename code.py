#＃02:Pythonでプログラムを書いてみよう
# coding: utf-8
# hello worldと表示する
print("はじめました")
print("hello paizaラーニング")
print("ハロー、paizaラーニング")

#03:コメントでプログラムを見やすく！
# コメントを入力する
print("hello world1") #文字を表示(良いコメント書き方)
'''
print("hello world2")
print("hello world3")
'''
#複数の行をコメントアウトするときは
#3つの連続したシングルクォートで囲む

'''
importを挿入することで『random,randin』関数を使用することができる
random.random() ：0から1までのランダムな数値を出力する
random.randint(a, b) ：aからbまでの間のランダムな整数を出力する
'''


#＃04:HTMLを表示してみよう
# coding: utf-8
#HTMLを表示する
print("<h1>hello world</h1>")
print("<p>世界の皆さん、")
print("<b>こんにちは</b></P>")

print('''<h1>hello world</h1>
<p>世界の皆さん、
<b>こんにちは</b></p>''') #シングルクォーテーション３個で、複数の行を扱うことができる。

print("<h1>hello world</h>","<p>世界の皆さん、","<b>こんにちは</b><p>") #改行したくない場合、一つ『,』で区切る

#演習問題
print("勇者は、荒野を歩いていた")
print("<b>モンスター</b>があらわれた")

#05:変数を使えるようになろう
# 変数を使う
player = "戦士"
print(player +"は、荒野を歩いていた") #文字データを格納した変数と文字列は、「+」記号で連結
print(player +"は、モンスターと戦った")
print(player + "は、モンスターをたおした")


#06:サイコロを作ろう
#数の表示とサイコロ

import random
number = random.randint(10,50)
print("スライムが" + str(number) + "匹あらわれた") #str(number) ：数値を、数を表す文字に変換する

number = random.randint(1,6)
print("サイコロの目は" + str(number) + "です。")

number = random.randint(55,99)
print("モンスターに、" + str(number) + "のダメージを与えた。")

#07:演算子で計算してみよう
# 計算する
number = 100 + 20
print(number)

number = 100 + 2 * 6 
print(number)

#a変数とb変数をかけ算

a = 31
b = 17
number = a * b
print(number)

#x変数をy変数でわり算した時の余りを求める
x = 8
y = 5
# 以下に、xをyで割ったときの余りを計算し、結果を出力するコードを書いてください
number = x % y
print(number)

#1234と5678を足し算して、それを3倍した結果
a = 1234
b = 5678
number = (a + b) * 3
print(number)

