from bisect import bisect_left , bisect_right

def count_by_range(array,left_value, right_value):
    left_index =  bisect_left(array, left_value)
    rigth_index = bisect_right(array, right_value)

    return rigth_index - left_index

def solution(words, queries):
    answer = []
    r_word = []
    len_word = [[]for _ in range(10001)]
    len_reverse = [[]for _ in range(10001)]
    
    words = sorted(words, key = lambda x :   x)
    for i in words:
        r_word.append(i[::-1])
    
    r_word = sorted(r_word, key = lambda x :   x)
    for i in words:
        len_word[len(i)].append(i)

    for i in r_word:
        len_reverse[len(i)].append(i)



    for i in queries:
        if i[0] == '?':
            left = i[::-1].replace('?' , 'a')
            right = i[::-1].replace('?','z')
            answer.append(count_by_range(len_reverse[len(i)],left, right))
        else:
            left = i.replace('?' , 'a')
            right = i.replace('?','z')     
            answer.append(count_by_range(len_word[len(i)],left, right))

        

    return answer



words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

print(solution(words, queries))