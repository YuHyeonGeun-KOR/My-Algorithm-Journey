def solution(n, recipes, orders):
    answer = 0
    recipes_menu = []
    recipes_Cooking_time = []
    orders_menu = []
    orders_Order_time = []
    fire = [0]*n
    one = 1
    for i in recipes:
        r =  i.split()    
        recipes_menu.append(r[0])
        recipes_Cooking_time.append(r[1])
        
    
    for i in orders:
        o = i. split()
        orders_menu.append(o[0])
        orders_Order_time.append(o[1])


    while True:
        answer +=1
        if len(orders_menu) >0:
            if answer >= int(orders_Order_time[0]):
                if 0 in fire:
                    fire[fire.index(0)]= int(recipes_Cooking_time[recipes_menu.index(orders_menu[0])])
                    if len(orders_menu) == 1:
                        return answer + int(recipes_Cooking_time[recipes_menu.index(orders_menu[0])])
                    else :
                        del orders_menu[0]
                        del orders_Order_time[0]
        for i in range(len(fire)):
            if fire[i]== 0:
                pass
            else:
                fire[i] = fire[i] - 1 

        if fire.count(0) == len(fire) and len(orders_menu) == 0:
            break
        
    return answer

recipes = ["A 3","B 2"]
orders =["A 1","A 2","B 3","B 4"]

print(solution(3,recipes,orders))