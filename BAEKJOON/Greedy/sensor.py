n = int(input())

k = int(input())

sen_position = list(map(int, input().split()))


sen_position.sort()
if ( sen_position[0] + sen_position[-1] ) % 2 ==1:
    print(( sen_position[0] + sen_position[-1] -1)//2)
else:
    print( ( sen_position[0] + sen_position[-1] )//2)