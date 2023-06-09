# range関数は、数値が順番に入ったリストを作るようなイメージ
# r = range(10)
# r = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(r)

# 指定回数の繰り返しは、iという変数名を使うのが一般的
# iには、0から9まで入る(合計10回)
for i in range(10):
    print(i)

# range(1, 10)ならば、1から9までiに入る(合計9回のループ)
# range(1, 11)ならば、1から10までiに入る(合計10回のループ)

dic = {
    '商品A': 3,
    '商品B': 10,
    '商品C': 7,
    '商品D': 5
}

print('商品一覧')
# 辞書のkeysメソッドは、for key in ['商品A', '商品B', '商品C', '商品D']
for key in dic.keys():
    print(key)

# キーの一覧を取り出すときは、わざわざkeysメソッド呼ばないほうが多い
# for 変すうめい in 辞書オブジェクト
for key in dic:
    print(key)


print('\n商品と在庫数の一覧')
for key, value in dic.items():  # このitemsを使ったを暗記したい
    print('商品名：' + key + '\t在庫数：' + str(value))


# dic.items()
# 次のようなリストを作る
# tuple_list = [
#     ('商品A', 3),
#     ('商品B', 10),
#     ('商品C', 7),
#     ('商品D', 5)
# ]
#
# for key, value in tuple_list:
#     print(key)
#     print(value)
#
#
# key, value = ['商品A', 3]
