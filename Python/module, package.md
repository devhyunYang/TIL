# 모듈과 패키지

**모듈**
- 파이썬 코드가 담긴 파일
- 변수, 함수, 클래스의 집합

**패키지**
- 모듈의 집합
- 여러 개의 모듈을 서브디렉토리 구조로 구성하여 관련 모듈을 그룹화함

** 서브 디렉토리 구조란?
- 디렉토리를 계층적으로 구성하여 파일을 구조화하는 방법
- 각 서브 디렉토리는 특정 기능, 모듈, 패키지 관련 파일을 포함할 수 있다.

```
my_project/ ⬅️ 루트 디렉토리
    main.py
    utils.py
    data/ ⬅️ 디렉토리
        data_processing.py ⬅️ 데이터 처리와 관련된 함수를 정의한 모듈
        data_files/ ⬅️ 실제 데이터 파일을 포함하는 서브 디렉토리
            file1.csv
            file2.csv
    models/ ⬅️ 디렉토리
        model1.py
        model2.py
    tests/
        test_utils.py
        test_data/
            test_file1.csv
            test_file2.csv
```

### Jupyter Notebook 에서 패키지 설치

```
!pip install 패키지이름
```
1. 파일이 있는 폴더에 dahyun.py 텍스트 파일을 만들었다
```
<<텍스트 파일에 적은 내용>>

name = 'dahyun'
gender = 'female'
hobby = 'gym'

def about_me()
    print('저는 이런 사람입니다.')
```
2. dahyun.py를 import 하기
```
from dahyun import name, gender, hobby

name

# dahyun
```
내가 만든 함수는 함수명도 같이 import 후 사용하기!
```
from dahyun import name, gender, hobby, about_me

about_me()
# dahyun
```

3. import 방식
```
from 모듈명 import 함수
```
같은 이름을 가진 변수가 있을 수 있다! 따라서 import로만 가져와서 변수를 선언하는 방식을 더 선호한다.

```
import dahyun 

dahyun.gender
dahyun.hobby
```

별칭을 설정할 수 있다.
```
import dahyun as dh

dh.gender
dh.hobby
```

'*' 사용하기
- dahyun에 있는 모든 것을 가져옴!!
```
from dahyun import *

hobby
```
