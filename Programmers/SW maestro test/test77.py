def main():
    x = int(input())
    result ={}
    sum = 0
    for i in range(x*x):
        hammer = list(map(int,input().split()))
        score = hammer.pop(0)
        time = hammer.pop(0)
        for i in hammer:
            if i not in result:
                result[i] = score
            else:
                if score > result[i]:
                    result[i] = score
    
    
    for key,value in result.items():
        sum += value
    print(sum)

if __name__=="__main__":
    main()