# coding: utf-8
#HTMLを表示する
print("<h1>hello world</h1>")
print("<p>世界の皆さん")
print("<b>こんにちは</b></p>")

# 問題
print("<p>勇者は、荒野を歩いていた</p>")
#シングルクォーツの場合
print('''<h1>hello world</h1>
<p>世界の皆さん
<b>こんにちは</b></p>''')

#print関数で改行しない場合
print("<h1>hello world</h1>","<p>世界の皆さん</p>","<b>こんにちは</b></p>")

#print関数の括弧中でダブルクォーター後にカンマとendとダブルクォーター✖️２
print("<h1>hello world</h1>",end="")
print("<p>世界の皆さん",end="")
print("<b>こんにちは</b></p>",end="")


# coding: utf-8
# 変数を使う
player = "戦士"
player2 = "魔法使い"
print(player + "は、荒野を歩いていた")
print(player + "、モンスターと戦った")
print(player + "は、モンスターをたおした")

print(player2 + "は、荒野を歩いていた")
print(player2 + "、モンスターと戦った")
print(player2 + "は、モンスターをたおした")