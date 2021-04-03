def solution(s):
    string = list(s)
    string_length = []
    
    result = []

    if len(s) == 1:
        return 1
    for window in range(1,len(string)//2 + 1):
        result = ""
        start = 0
        count = 1

        for i in range(len(string)//window) :
            left = string[start:start+window]
            right = string[start+window:start + window + window]
            if left ==  right:
                count += 1
            else:     
                if count > 1:
                    result += str(count)
                result +=  "".join(left)
                count = 1    
                if len(right)<window and len(right) != 0 :
                    result+="".join(right)
                    
            start += window   
        string_length.append(len(result))
   
    return min(string_length)

    


s = "aabbaccc"
print(solution(s))