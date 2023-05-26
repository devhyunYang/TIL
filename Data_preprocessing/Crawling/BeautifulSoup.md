# BeautifulSoup
- requests.text로 가져온 텍스트 형태의 html을 수프객체로 만들어 쉽게 추출 가능하게 한다.

1️⃣ import
```
from bs4 import BeautifulSoup
```
2️⃣ 텍스트 형태 html 가져오기
```
html = requests.get('url')
text = html.text

# html.text를 정리해줌 (html.parser', 'xml')
soupt = BeautifulSoup(text, 'html.parser')
```

3️⃣ 원하는 데이터 추출
```
# title 태그 추출
soup.title 

# 문자만 추출
soup.title.string
soup.title.text
```

## find / find_all

### find
1개 (첫 번째) 찾기
````
soup.find('태그명') 
soup.태그명
````

### find_all
모든 요소 찾기
```
soup.find_all('태그명') 
```

