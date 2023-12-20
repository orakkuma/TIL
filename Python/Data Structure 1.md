# Data Structure
데이터 구조란 데이터에 편리하게 접근하고, 변경하기 위해서 데이터를 저장하거너ㅏ 조작하는 방법을 말한다.
> **Program = Data Structure + Algorithm**
> - Niklaus Wirth

- 알고리즘에 빈번히 활용되는 순서가 있는(ordered) 데이터 구조 
    - 문자열(String)
    - 리스트(List)
- 데이터 구조에 적용 가능한 Built-in Function

## String
변경할 수 없고(immutable), 순서가 있고(ordered), 순회 가능한(iterable)

## 조회/탐색
- .find(x)

    x의 첫 번째 위치를 반환. 없으면, `-1`을 반환

- .index(x)
    x의 첫번째 위치를 반환. 없으면 errer

## 문자열 변경
- .replace(old, new[, count])

- .strip([chars])

- .split([chars])

- 'separator'.join(iterable)

- .capitalize(), .title(), .upper()

- .lower(), .swapcase()

## **`List`**
변경 가능하고(mutable), 순서가 있고(ordered), 순회 가능한(iterable)

### 값 추가 및 삭제
- .append(x)
- .extend(iterable)
- .insert(i, x)
- .remove(x)
- .pop(i)
- .clear()

### 탐색 및 정렬
- .index(x)
- .count(x)
- .sort()
- .reverse()

### 리스트 복사
- slice 연산자 사용 [:]
- .copy()

## List Comprehension
list comprehension은 표현식과 제어문을 통해 리스트를 생성한다.

여러 줄의 코드를 한 줄로 줄일 수 있습니다.

---

### 활용법

```python
[expression for 변수 in iterable]

list(expression for 변수 in iterable)
```

```python
cubic_list = []

for num in numbers:
    cubic_list.append(num ** 3)

print(cubic_list)

# [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
```
```python
cubic_list = [num**3 for num in numbers]
# = num**3 for num in range(1, 11)
cubic_list
```

## List comprehension + 조건문
**활용법**

```python
[expression for 변수 in iterable if 조건식]
```

```python
vowels = 'aeiou'
words = 'Life is too short, you need python!'
blank = ''

for char in words:
    if char not in vowels:
        blank += char

print(blank)

# Lf s t shrt, y nd pythn!
```
```python
vowels = 'aeiou'
words = 'Life is too short, you need python!'

blank = [char for char in words if char not in vowels]
print(''.join(blank))
```
---
---

```python
# 아래에 코드를 작성하시오.
# =====
chars = input('숫자를 띄어쓰기로 구분하여 입력해 주세요')

# 1. 띄어쓰기로 구분하여 리스트로 만든다.
# 2. 리스트를 다 더한다? (x) 리스트 내용물을 정수로 바꾼다.(O)
# 3. 모든 값을 다 더한다.

char_list = chars.split()
sum(map(int, char_list))
```
```python
sum(map(int, input().split()))
```

## filter(function, iterable)

- iterable에서 function의 반환된 결과가 `True` 인 것들만 구성하여 반환합니다.


* `filter object` 를 반환합니다.

## zip(*iterables)
* 복수의 iterable 객체를 모아(`zip()`)줍니다.

* 결과는 튜플의 모음으로 구성된 `zip object` 를 반환합니다.

## lambda 표현식
간단한 함수의 경우, 짧게 줄여 쓸 수 있습니다.

기존의 정의한 함수를 람다표현식으로 바꾸는 방법
1. 맨 앞에 `lambda`라고 적는다.
2. `def`와 함수 이름과 소괄호까지 지운다.
3. `return`도 지운다.

람다 표현식으로 바꿀 함수는 아래 조건을 만족해야 합니다.
1. 매개변수가 1개 이상이어야 한다.
2. `return`구문 포함 한줄이어야 한다.

