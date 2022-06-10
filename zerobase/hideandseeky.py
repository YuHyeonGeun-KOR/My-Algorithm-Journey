from collections import deque
import queue
def solution(x1, y1, x2, y2):
    cdx = [-1 , 1 , 0 , 0 ]
    cdy = [ 0 , 0 , 1 ,-1 ]
    
    ydx = [-1 , -1 , 1 , 1 ]
    ydy = [-1 , 1 , -1 , 1 ]
    

    cqueue = deque()
    yqueue = deque()
    cdic = {}
    ydic = {}
    cset =set()
    yset = set()
    cdic[0] = set()
    ydic[0] = set()
    cdic[0].add((x1,y1))
    ydic[0].add((x2,y2))
    cqueue.append((0,x1,y1))
    yqueue.append((0,x2,y2))

    while True:
        cnow  = cqueue.popleft()
        ynow  = yqueue.popleft()

        ctime  , cx , cy = cnow[0] , cnow[1], cnow[2]
        ytime  , yx , yy = ynow[0] , ynow[1], ynow[2]

        if (cx, cy) in ydic[ctime]:
            return ctime
        if (yx, yy) in cdic[ytime]:
            return ytime
        
        if ctime + 1 not in cdic:
            cdic[ctime + 1 ] = set()

        if ytime + 1 not in ydic:
            ydic[ytime + 1] = set()
                
        for i in range(4):
            ncx = cx + cdx[i]
            ncy = cy + cdy[i]

            if -1000 <=  ncx <= 1000  and -1000 <= ncy <= 1000 and (ncx , ncy) not in cset:
                cdic[ctime+1].add((ncx, ncy))
                cset.add((ncx,ncy))
                cqueue.append((ctime+1 , ncx, ncy))

        for i in range(4):
            nyx = yx + ydx[i]
            nyy = yy + ydy[i]

            if -1000 <=  nyx <= 1000  and -1000 <= nyy <= 1000 and (nyx , nyy) not in yset :
                ydic[ytime+1].add((nyx, nyy))
                yset.add((nyx,nyy))
                yqueue.append((ytime+1 , nyx, nyy))



        
    answer = 0
    return answer

print(solution(2 , 4 , 5 , -1))