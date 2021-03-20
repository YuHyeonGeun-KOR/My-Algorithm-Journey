n= int(input())

time = [[]for i in range(n)]
m_hour_1 = 0
m_min_1 = 60
m_hour_2 = 24
m_min_2 = 60
for i in range(n):
    time[i] = input()
    if m_hour_1 < int(time[i][0:2]):
        m_hour_1 = int(time[i][0:2])
        m_min_1 = int(time[i][3:5])
    elif m_hour_1 == int(time[i][0:2]) and m_min_1 < int(time[i][3:5]):
        m_min_1 = int(time[i][3:5])
    
    
    
    if m_hour_2 > int(time[i][8:10]):
        m_hour_2 = int(time[i][8:10])
        m_min_2 = int(time[i][11:13])
    elif m_hour_2 == int(time[i][8:10]) and m_min_2 > int(time[i][11:13]):
        m_min_2 = int(time[i][11:13])







if m_hour_1 > m_hour_2 or m_hour_2 < m_hour_1:
    print(-1)
elif (m_hour_1 == m_hour_2 and m_min_1 >m_min_2)  :
    print(-1)
else:
    if len(str(m_hour_1)) ==1:
        hour_1 = "0"+str(m_hour_1)
    else :
        hour_1 = str(m_hour_1)

    if len(str(m_min_1)) ==1:
        min_1 = "0"+str(str(m_min_1))
    else :
        min_1 = str(m_min_1)

    if len(str(m_hour_2)) ==1:
        hour_2 = "0"+str(m_hour_2)
    else :
        hour_2 = str(m_hour_2)

    if len(str(m_min_2)) ==1:
        min_2 = "0"+str(m_min_2)
    else :
        min_2 = str(m_min_2)

    
    result =hour_1 + ":" + min_1 + " ~ " +  hour_2  + ":" + min_2 
    print(result)