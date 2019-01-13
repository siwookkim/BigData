import requests
from urllib.parse import quote

def get1000Result(Keyword):
    list= []
    for num in range(0, 10):
        list = list + call(Keyword, num * 100 +1)['items']
    return list

def call(Keyword, start):
    encText = quote(Keyword)
    url = "https://openapi.naver.com/v1/search/blog?query=" + encText + "&display=100" + "&start=" + str(start)
    result = requests.get(url = url,
                          headers={"X-Naver-Client-Id": "9JHzz934DBRfY9TJK2B5",
                                   "X-Naver-Client-Secret": "W2acwV3yTC"
                                   })
    print(result)
    return result.json()

