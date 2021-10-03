def convert(num,base):
    temp = "0123456789ABCDEF"
    q,r = divmod(num,base)
    re = temp[r]
    if q!=0:
        re += convert(q,base)
    return re

def makeconvert(num,base):
    t=""
    for i in range(num):
        re = convert(i,base)
        re = re[::-1] #문자열을 역순으로 만들어 주세요.
        t+=re
    return t


def solution(n,t,m,p): #"011011100101110111"
  re=""#re:= 내가 외칠 문자열을 위한 빈 문자열 생성
  src = makeconvert(m*t,n)#m*t(참가자와 회전수만큼 n진수의 문자열 배치를 구한다. - makeconvert함수 이용)
  index = p-1 #index는 순번-1
  for ti in range(t):#반복 - 회전수만큼
    re = re + src[index]#re:=외칠 숫자를 추가
    index = index + m#다음 외칠 숫자:=현재인덱스 + 참가인원수
  return re#re를 반환
print(solution(2,4,2,1))
print(solution(16,8,2,1))