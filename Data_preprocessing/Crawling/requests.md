# Crawling

- 웹 상의 데이터 수집
- 웹 페이지 접속 (요청)➡️ (응답) ➡️ 웹 페이지 원하는 데이터 위치 ➡️ 값 가져오기 ➡️ 데이터 형식 파악/변환 ➡️ 데이터 저장
- 브라우저에 접속(url) ex) http://github.com 
  -  http://(프로토콜) :  웹 상에서 데이터를 주고 받을 때 사용하는 약속!

> 클라이언트 -- URL(요청 Request) --> 서버
> 
> 클라이언트 <-- 메인 페이지(응답 Response) -- 서버

## 요청 라이브러리 : Requests
클라이언트의 HTTP 요청을 보내는데 사용

```
import requests

html = requests.get('url')
html # <Response [200]>
```
성공 : 200 실패 : 400,500 + 데이터

## GET요청 POST요청
### GET요청
- 내가 원하는 정보가 url 안에 들어있다.
- https://shopping.naver.com/home
### POST요청
- 내가 보내는 요청이 들어있지 않다.
- https://naver.com/login < ID, PW를 URL에 담지 않는다.
- 보안이 필요한 경우, 요청 내용이 길 경우 사용
- POST 요청 보내는 방법
```
import json

body = {'id' : 'aaa', 'pw' : 1234}
post = requests.post('url', data=json.dumps(body))
```
