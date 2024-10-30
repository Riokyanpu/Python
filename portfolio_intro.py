# portfolio.py

# 1. 自己紹介
print("## 自己紹介")
print("はじめまして！Python学習を始めました。")
print("hello paizaラーニング")
print("ハロー、paizaラーニング")

# 2. 学習進捗
print("\n## 学習進捗")
print("1. Chapter 1: Pythonとは？")
print("2. Chapter 2: Pythonでプログラムを書いてみよう")
print("3. Chapter 3: コメントでプログラムを見やすく！")
print("4. Chapter 4: HTMLを表示してみよう")
print("5. Chapter 5: 変数を使えるようになろう")
print("6. Chapter 6: サイコロを作ろう")

# 3. 冒険ログ（HTML表示、変数、ランダム生成の利用例）
print("\n## 冒険ログ")

# Chapter 4: HTML表示の例
print("\n<h1>冒険の始まり</h1>")
print("<p>勇者は、荒野を歩いていた</p>")
print("<b>モンスター</b>があらわれた")

# Chapter 5: 変数を使用したストーリー展開
player = "戦士"
print(f"\n<p>{player}は、荒野を歩いていた</p>")
print(f"<p>{player}は、モンスターと戦った</p>")
print(f"<p>{player}は、モンスターをたおした</p>")

# Chapter 6: ランダムな数値を生成するサイコロの要素
import random
enemy_count = random.randint(10, 50)
print(f"\n<p>スライムが{enemy_count}匹あらわれた！</p>")

# HTMLの複数行表示
print('''<h1>冒険の終わり</h1>
<p>勇者と戦士は新たな冒険の準備をしている。</p>''')

# 4. 次のチャプターの予告
print("\n## 今後の学習")
print("次のチャプターでは、基本的なデータ型や変数の使い方を学んでいきます。")
