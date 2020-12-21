import requests

def get_favorite():
    result_s = {}
    result_e = {}
    max_s = [0, 0]
    max_e = [0, 0]
    def getdata(url):
        return requests.get(url).json()
    def input_d(data):
        for time in data:
            for s, e, t in data[time]:
                if s in result_s:
                    result_s[s] += 1
                else:
                    result_s[s] = 1

                if e in result_e:
                    result_e[e] += 1
                else:
                    result_e[e] = 1
    url1 = "https://grepp-cloudfront.s3.ap-northeast-2.amazonaws.com/programmers_imgs/competition-imgs/2021kakao/problem2_day-1.json"
    url2 = "https://grepp-cloudfront.s3.ap-northeast-2.amazonaws.com/programmers_imgs/competition-imgs/2021kakao/problem2_day-2.json"
    url3 = "https://grepp-cloudfront.s3.ap-northeast-2.amazonaws.com/programmers_imgs/competition-imgs/2021kakao/problem2_day-3.json"
    input_d(getdata(url1))
    input_d(getdata(url2))
    input_d(getdata(url3))

    for key in result_s:
        if result_s[key] > max_s[1]:
            max_s[0] = key
            max_s[1] = result_s[key]

    for key in result_e:
        if result_e[key] > max_e[1]:
            max_e[0] = key
            max_e[1] = result_e[key]

    return max_s[0], max_e[0]

s, e = get_favorite()

print(s, e)