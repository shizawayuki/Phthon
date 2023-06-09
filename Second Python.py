def hello():
    print("hello world")

hello()

def is_prime(number):
    # 引数のnumberが素数ならTrueを返す
    for j in range(2, number):
        # print(f'  j={j}')
        if i % j == 0:
            return False

    # 割り切れなかったら（素数じゃなかったら）ここに到達する
    return True


for i in range(2, 101):
    if is_prime(i):
        print(i)


# 変数や関数名は、全て小文字で、単語の間にアンスコをつける
# get_tax
# my_name

def get_tax(price):
    tax = int(price * 0.1)
    return tax


a = get_tax(75)
b = get_tax(1980)
print(a)
print(b)