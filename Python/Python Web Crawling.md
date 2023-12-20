# 브라우저 크롤링

## requests
- 파이썬에서 **HTTP**를 사용하기 위해 쓰는 라이브러리.
- **request(요청)**을 보내면 **response(응답)**을 객체로 받는다.
- 어떤 방식(method)의 HTTP를 요청하냐에 따라 쓰이는 함수가 달라진다.
  - GET : requests.get()
    - 현재는 get만 배운 상태
  - POST : requests.post()
  - PUT : requests.put()
  - DELETE : requests.delete()

- dictionary = key : value로 구성 된다.

- BeautifulSoup
  - 웹사이트 크롤링 후 HTML로 부터 **원하는 데이터를 가져오기 위해** 데이터를 추출하고 **파싱(parsing)** 할 때 도움을 주는 오픈소스 라이브러리
  
- bs4 모듈
  - HTML을 **파싱**할 때 사용. bs4모듈이 파싱 해놓은 데이터 중에서 원하는 데이터만을 가져와 사용할 수 있게 도움. 
- select() 함수
  - select를 사용하면 원하는 데이터를 추출할 수 있다.
  - soup = BeautifulSoup(ex, 'html.parser')
  - soup.select('p')
    - p는 HTML 태그


- GET의 사용법
  ```python
  import requests
  from bs4 import BeautifulSoup

  URL = ''
  # 브라우저 URL 받아온다.
  
  page = requests.get(URL).text
  # 해당 사이트에 접속해 페이지를 다운
  # 다운 받은 dadta중 text 만 추출
  data = BeautifulSoup(page, 'html.parser')
  # HTML 코드 형태로 구분
  
  r = data.select_one('#~')
  # F12를 눌러 스크래핑 하고 싶은 영역의 HTML 태그를 복사.

  print(r.text)
  ```

  - 응용 - tellegram을 이용
  ```python
  import requests
  from bs4 import BeautifulSoup

  TOKEN = '내 토큰 값'

  MY_ID = '내 ID 값'

  URL_tellegram = ''
  URL_shop = ''
  # 다양한 영역에서 활용 가능
  # 오늘은 쇼핑몰에서 내가 원하는 제품의 가격을 스크래핑

  x = requests.get(URL_shop).text
  data = BeautifulSoup(x, 'html.parser')

  name = data.select_one('')
  price = data.select_one('')

  message = name + price
  message2 = message + '원'

  requests.get(URL_tellegram + message2)
  ```