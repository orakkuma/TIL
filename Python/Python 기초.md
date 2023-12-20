# Python의 기초

**jupyter 브라우저로 열기 - git bash에서 01-python 폴더에서 python3 -m notebook 실행**

## 주석
- 주석은 #으로 표현
## 코드 라인
```python
print('hello world')
  =hello world

print('hello \
  world)
  = hello world
#불가피하게 줄을 바꾸고 싶을 땐 '\' 사용
```

## 변수(variable)
### 변수에 문자열 할당
`x = 'python`

`type(x)` => str

### 다른 변수에 같은 값을 동시에 할당
```python
x = '20231207'
y = '20231207'

print (x, y)

x = y = 20231207
print(x, y)
```
20231207 20231207

### 다른 변수에 다른 값을 동시에 할당
```python
x, y = 1, 2

print(x, y)
```
1 2

#### 응용 - 변수의 값을 서로 바꾸기
```python
x = 1
y = 2

x, y = y, x

print(x, y)
```
```python
x = 1
y = 2
x = x * y
y = x / y
x = x / y

#or

x = 1
y = 2
x = x + y
y = x - y
x = x - y
```

## 데이터 타입
### 숫자
#### int 정수
#### float 실수
- ex) 3.5, 314e-2(= 3.14)
- 실수의 연산
  - round(값, 소수점자릿수)

## string 문자열
- 문자열은 ' or " 을 활용하여 표현 가능


```python
first_name = 'euiseok'
last_name = 'Jung'

print(first_name, last_name)
print(type(last_name))

# euiseok Jung
# <class 'str'>
```
```python
# input 값은 무조건 string
age = input()
print(age)
print(type(age))
# input => 27
# 27
# <class 'str'>
```
**다시 강조 input => 무조건 string**

- 철수가 말했다. '안녕?' => 표현해보기
  - `print('철수가 말했다. '안녕?'')` => error
  - `print("철수가 말했다. '안녕?'")` => 실행

- 여러줄 출력
  ```python
  print('''hello
  hello
  hello''')
  
  # hello
  # hello
  # hello

  'hey' * 2 + 'yo' # heyheyyo
  ```
- string interpolation
  - str.format(), f-strings
  ```python
  name = 'euiseok'
  score = 100
  'my name is {}, score is {}.'.format(name, score)
  # my name is euiseok, score is 100.
  
  f'''my name is {name}, score is{score}.'''
  # my name is euise0k, score is 100
  ```

## Boolean
False = 0, 0.0, (), {}, [], '', None..

*비어있다/없다 의 뉘앙스면 다 false*

그 외엔 다 True

**(0), '0' = True**
```python
bool(None)
# False

bool([''])
# True
```
## Operator 연산자
### 산술 연산자
|연산자|내용|
|----|---|
|+|덧셈|
|-|뺄셈|
|\*|곱셈|
|/|나눗셈|
|//|몫|
|%|나머지(modulo)|
|\*\*|거듭제곱|

- 나눗셈 (`/`) 은 항상 float를 돌려줍니다.
- 정수 나눗셈 으로 (소수부 없이) 정수 결과를 얻으려면 `//` 연산자를 사용합니다.

### 비교 연산자
|연산자|내용|
|----|---|
|`<`|미만|
|`<=`|이하|
|`>`|초과|
|`>=`|이상|
|`==`|같음|
|`!=`|같지않음|
|`is`|객체 아이덴티티|
|`is not`|부정된 객체 아이덴티티|

### 논리 연산자
|연산자|내용|
|---|---|
|a and b|a와 b 모두 True시만 True|
|a or b|a 와 b 모두 False시만 False|
|not a|True -> False, False -> True|

### 단축평가
- 첫 번째 값이 확실할 때, 두 번째 값은 확인 하지 않는다.
- 조건문에서 뒷 부분을 판단하지 않아도 된다.
```python
True and True and True and False and True
#                여기까지는 True
#                          False가 나온 순간 뒤는 볼 필요 없이 False

'a' and 'b' 
# 'a' True, 'b' True, and로 연결 -> 마지막으로 나온 값이 출력 따라서 'b'

'a' or 'b'
# 'a' True, 'b' True, or로 연결 -> 'a'

'a' and 10 and True and 0 and 4 and 3.14 and 'asdf'
#                     False
# 결과 = 0, 0에서 반환

0 or '' or False or '0' or None
#                   True
# '0'
```

### 복합 연산자
복합 연산자는 연산과 대입이 함께 이뤄진다. 

가장 많이 활용되는 경우는 반복문을 통해서 갯수를 카운트하거나 할 때 활용된다.

|연산자|내용|
|----|---|
|a += b|a = a + b|
|a -= b|a = a - b|
|a \*= b|a = a \* b|
|a /= b|a = a / b|
|a //= b|a = a // b|
|a %= b|a = a % b|
|a \*\*= b|a = a ** b|

```python
# print의 위치가 어디냐에 따라서 결과값이 달라짐. 반드시 이해하기
cnt = 0
while cnt < 5:
    print(cnt)
    cnt += 1

#0 1 2 3 4

cnt = 0
while cnt < 5:
    cnt += 1
    print(cnt)

# 1 2 3 4 5
```
### 기타 연산자
'a' + 'b' => 'ab'

[1,2,3] + [4,5,6] => [1,2,3,4,5,6]








---
```
오늘의 remember me
input 값은 stirng - line 100
bool(['']) => True - line 142
주말에 None 타입 복습하기
복합연산자 while문 이해하기 - line 218

**C++ 할 때도 특히 if, while 반복문에 취약했음...**
```