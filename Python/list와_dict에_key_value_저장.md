# list와 dictionary에 key, value 값을 저장해보자!

## 1. list
```
def input_value():
    value = input('value를 입력하세요 : ')
    return value

my_list = []

num_entries = int(input("저장할 값의 개수를 입력하세요."))

for num in range(num_entries):
    value = input_value()
    my_list.append(value)

print(my_list)
```

💬 만약 리스트에 dictionary 형태를 저장하고자 한다면?

```
def input_key_value():
    key = input("key를 입력하세요. : ")
    value = input("value를 입력하세요. : ")
    return key, value

my_list = []

num_entires = int(input("저장할 key-value 쌍의 개수를 입력하세요 : "))

for num in range(num_entries):
    dictionary = {} # 빈 딕셔너리 생성
    key, value = input_key_value()
    dictionary[key] = value # 입력 받은 key, value를 딕셔너리에 저장
    my_list.append(dictionary) # 딕셔너리를 리스트에 추가

print(my_list) # [{'1': '2'}, {'1': '2'}, {'1': '2'}]
```

## 2. dictionary
```
def input_key_value():
    key = input("Key를 입력하세요 : ") # key 입력 받기
    value = input("Value를 입력하세요 : ") # value 입력 받기
    return key, value # 입력받은 key, value 값 반환

my_dict = {} # 빈 dictionary 준비

num_entries = int(input("저장할 key-value 쌍의 개수를 입력하세요 : ")) # 저장할 key-value 쌍 개수 입력 받기

for num in range(num_entries):
    key, value = input_key_value() # input_key_value 함수 호출하여 key, value 값 받기
    my_dict[key] = value # key와 value를 dictionary에 저장

print(my_dict)
```
