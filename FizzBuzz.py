# 1から100までfor文で繰り返し、
# 3の倍数のときは「Fizz」
# 5の倍数のときは「Buzz」
# 15の倍数のときは「FizzBuzz」
# それ以外は数値を表示するプログラムを作りましょう。
#
# 出力例.
#
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz






for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("Fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


