def scatterPalindrome(strToEvaluate):
    def check(start, end, word):
        res = 0
        if len(record) <= 1:
            res += 1

        if start < end:
            if word[start] not in record:
                record[word[start]] = 1
                res += check(start+1, end, word)
                del record[word[start]]
            else:
                del record[word[start]]
                res += check(start+1, end, word)
                record[word[start]] = 1
        return res

    answer = []
    for word in strToEvaluate:
        record = {}
        result = 0
        for end in range(len(word)):
            if word[end] not in record:
                record[word[end]] = 1
            else:
                del record[word[end]]
            result += check(0, end, word)
        answer.append(result)
    return answer






print(scatterPalindrome(['aabb', 'abc', 'bbrrg']))