import sys
import heapq
input = sys.stdin.readline

n,k = map(int,input().split())

order = list(map(int, input().split()))

count_list = [0] * k
max_order = 1e9

socket = []
socket_number = []
count = 0 
order_index = 0
for i in order:
    order_index +=1
    if len(socket_number) != n:
        if i in socket_number:
            for soc in socket:
                if soc[1] == i:
                    socket.remove(soc)
                    break

        try:
            find_index = order.index(i , order_index, len(order)-1)
        except:
        
            find_index = max_order

        heapq.heappush(socket,[-find_index ,i])
        
        if i not in socket_number:
            socket_number.append(i)
    else:
        if i not in socket_number:
            socket_index, s_number = heapq.heappop(socket)
            socket_number.remove(s_number)
            
            try:
                find_index = order.index(i , order_index, len(order)-1)
            except:
                
                find_index = max_order

            heapq.heappush(socket,[-find_index ,i])
            
            
            socket_number.append(i)
            count +=1
        else:
            for soc in socket:
                if soc[1] == i:
                    socket.remove(soc)
                    break
            try:
                find_index = order.index(i , order_index, len(order)-1)
            except:
                find_index = max_order
            
            heapq.heappush(socket,[-find_index ,i])
    
    
    
print(count)