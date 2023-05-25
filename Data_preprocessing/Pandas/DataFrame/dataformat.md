## 데이터 종류
### 1. 정형 데이터(Structured Data)
- 데이터 베이스의 정해진 규칙에 맞게 들어간 데이터 중 수치만으로 의미 파악이 쉬운 데이터
- 형식이 정해져 있다
- Excel, CSV, TXT
### 2. 반정형 데이터(Semi - Structured Data)
- 서버간 데이터 전달에 주로 사용
- JSON, XML, HTML
### 3. 비정형 데이터 (Unstructured Data)
- 정해진 규칙이 없다
- 이미지, 한글(.hwp)

## 파일 포맷 형식 다루기
### 1. 정형 데이터
1️⃣ **Excel**

구글 colab에서 업로드한 파일 불러오기
```
from google colab import files
file = files.upload()
```

**excel 읽기**
```
pd.read_excel('파일명')
```
시트별 츌력
```
df_excel_sheet1 = pd.read_excel('파일명.xlsx', sheet_name = '시트1') # 첫번째 시트
df_excel_sheet2 = pd.read_excel('파일명.xlsx', sheet_name = '시트2') # 첫번째 시트
```
시트 여러개 출력
```
df_excel_sheets = pd.read_excel('파일명.xlsx', sheet_name = [0, 1])
df_excel_sheets = pd.read_excel('파일명.xlsx', sheet_name = [0, '시트2'])
```
시트 다 가져오기
```
df_excel_sheets_all = pd.read_excel('파일명.xlsx', sheet_name = None)
```
