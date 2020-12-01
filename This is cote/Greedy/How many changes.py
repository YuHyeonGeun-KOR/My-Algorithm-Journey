change = int(input())
Count_coin= 0


def coin (price,coin_price,coin):
    coin_num = price//coin_price
    coin = coin + coin_num

    return coin


def balance (price,coin_price):
    bal = price%coin_price

    return bal

step1 = coin(change,500,Count_coin)
bal_1 = balance(change,500)

step2 = coin(bal_1,100,step1)
bal_2 = balance(bal_1,100)

step3 = coin(bal_2,50,step2)
bal_3 = balance(bal_2,50)

result = coin(bal_3,10,step3)

print(result)





