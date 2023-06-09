# sは、仮引数とも呼ぶ
def message(s=None):
    if s is None:  # s == Noneと書きたくなったら、isを使う
        print('文字列が未入力です')
    else:
        print('入力文字列は「' + s + '」です')


# 'Hello World'は実引数とも呼ぶ
# 関数呼び出しの際に、引数名=値のように渡すことができる
message(s='Hello World')
message()

class Character:
    name = ''

    def speak(self, comment):
        print(self.name + ':' + comment)


# Characterのインスタンスを、taro変数に代入
taro = Character()  # インスタンス化

# クラスのデータ属性になくても、自由に属性を追加できる
taro.first_name = 'タロー'
taro.last_name = 'タナカ'
print(taro.first_name)
print(taro.last_name)

class Character:

    # ダンダーイニット。特殊メソッドと呼ぶ
    def __init__(self, name):
        self.name = name

    # メソッドの第一引数は、ほぼ必ず、インスタンス自身が渡される
    def speak(self, comment):
        print(self.name + ':' + comment)


# インスタンスの属性は、基本的にはコンストラクタの__init__で行う
# 他のメソッド内から、インスタンスの属性を設定することもあります
# taro.name = 'ziro' のように外側から設定することは少ないです
taro = Character('tarou')
taro.speak(comment='ハロー')

# self.nameと同じ。結果的に、'tarou'が取得できる
print(taro.name)