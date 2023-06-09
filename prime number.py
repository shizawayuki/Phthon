# 素数の判定
# 1から100まで繰り返し、素数の数値を表示するプログラムを作成しましょう。

prime_number = 100
for i in range(2, prime_number):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i, end=' ')


for i in range(2, 101):
    is_prime = True  # 素数かどうかのフラグ
    # i = 10
    # 2~9までで、割ってみて
    # 割れきれたら素数じゃない
    # print(f'i={i}')
    for j in range(2, i):
        # print(f'  j={j}')
        if i % j == 0:
            is_prime = False

    if is_prime:
        print(i)