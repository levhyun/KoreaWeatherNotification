import requests
import json
import AnswerDir as dir

# API 키
apikey = "474d59dd890c4108f62f192e0c6fce01"

# 날씨를 확인할 나라,도시 리스트
# locationList = ["Seoul,KR", "Tokyo,JP", "New York,US"]
locationList = ["Seoul"]

#언어
lang = 'kr'

# API
api = "http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}&lang={lang}"

# 켈빈 온도 -> 섭씨 온도
k2c = lambda k: k - 273.15

for location in locationList:
    # API URL
    url = api.format(city=location, key=apikey, lang=lang)

    # API 요청 후 데이터 추출
    r = requests.get(url)

    # JSON 형식으로 변환
    data = json.loads(r.text)

    # 결과 출력
    print("도시 :", data["name"])

    # 충고
    for key in dir.answer:
        if key == data["weather"][0]["id"]:
            print(dir.answer[key])

    print('최저 기온은 {:.2f}℃이며 최고 기온은 {:.2f}℃이며 습도는 {}%입니다.'.format(k2c(data["main"]["temp_min"]), k2c(data["main"]["temp_max"]), data["main"]["humidity"]))