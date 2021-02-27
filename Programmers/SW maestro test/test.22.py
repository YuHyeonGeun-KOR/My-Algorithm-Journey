def main():
    p,n,h = map(int,input().split())

    customer = []
    time = {}
    result = {}
    for i in range(n):
        pc , hour = map(int, input().split())
        customer.append([pc,hour])
        time[pc] = h
        result[pc] = 0
    
    for i in customer:
        if i[1] <= time[i[0]]:
            time[i[0]] =  time[i[0]] - i[1]
            result[i[0]] =  result[i[0]] + (1000*i[1])

    

    for key, value  in result.items():
        print(key,value)
if __name__=="__main__":
    main()