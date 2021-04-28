from bisect import bisect_left ,bisect_right

word_length = [[] for _ in range(10001)]
word_reverse = [[] for _ in range(10001)]

def solution (words , queries):
    answer = []
    for i in words:
        word_length[len(i)].append(i)
        word_reverse[len(i)].append(i[::-1])

    for i in range(10001):
        word_length[i].sort()
        word_reverse[i].sort()

    
    for i in queries:
        if i[0] == '?':
            left_checker = i[::-1].replace('?' , 'a')
            right_checker = i[::-1].replace('?','z')
            left_index = bisect_left(word_reverse[len(i)],left_checker)
            right_index = bisect_right(word_reverse[len(i)],right_checker)
            count = right_index-left_index
        else:
            left_checker = i.replace('?' , 'a')
            right_checker = i.replace('?','z')
            left_index = bisect_left(word_length[len(i)],left_checker)
            right_index = bisect_right(word_length[len(i)],right_checker)
            count = right_index-left_index        
        answer.append(count)

    return answer

words = ["frodo", "frozz", "frozz", "frozen", "frame", "kakao"]
queries = ["fro??"]

print(solution(words, queries))