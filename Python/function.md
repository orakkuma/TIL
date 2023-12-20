# function
## 함수를 쓰는 이유
- 가독성
- 재사용성
- 유지보수

## 함수의 선언과 호출
- 함수 선언 - def
- 들여쓰기로 함수의 body(code block) 작성
- 함수는 매개변수(parameter)를 넘겨줄 수 있다.
- 함수는 동작 후에 `return`을 통해 `결과값`을 전달
- 반드시 `하나의 객체(값)`을 반환.
  - return값이 없으면, None을 반환
- 함수 호출은 func_name()으로 한다.

```python
def <func_name>(parameter1, parameter2):
    <code_block>
    return value
```

## 함수의 Output

### 함수의 return
함수는 반환되는 값이 있으며, 이는 어떠한 종류의 객체라도 상관없다.

단 오직 `단 한 개의 객체`만 반환.

함수가 return 되거나 종료되면, 함수를 호출한 곳으로 돌아간다.

func은
- **return** 이 없으면 끝까지 실행, **None**을 반환.
- **return**이 있으면, 그 자리에서 바로 종료.

```python
def inf():
    while True:
        print('무한')
        return

print(inf())
#무한
#None
```
```python
def inf():
    print('infinite')
    return 1
    print('loop')
infinite()

# infinite
# 1
# 뒤에 loop print 선언했지만 return 1 이 있으므로 무조건 return에서 반환.
```

## Input of Function
### parameter(매개변수), argument(전달인자)

#### parameter
```python
def func(x):
    return x + 2
```
- x 는 parameter
- 입력을 받아 func 내부에서 활용할 변수라고 생각하면 됨.
- 함수의 정의 부분에서 볼 수 있다.

#### argument
```python
func(2)
```
- 2는 argument(전달인자)
- 실제로 전달되는 `입력값`이라고 생각하면 됨.
- 함수를 호출 하는 부분에서 볼 수 있다.

### 함수의 인자.

#### 위치 인자(Positional Arguments)

- 기본적으로 인자는 위치에 따라 함수 내에 전달.
```python
def cylinder(r, h):
    return 3.14 * r**2 * h
print(cylinder(5, 2))
print(cylinder(2, 5))
# 두개의 결과값은 다르다.
```

#### 기본 인자 값(Default Argument Values)
- 함수를 정의할 때, 기본값을 지정하여 함수를 호출할 때 인자의 값을 설정하지 않도록 하여, 정의된 것 보다 더 적은 개수의 인자들로 호출할 수 있다.

```python
def func(p1 = v1):
    return p1
```

```python
def greeting(name='익명'):
    print(f'{name}, 안녕?')
    
greeting()
greeting('철수')

# 익명, 안녕?
# 철수, 안녕?
```

#### 키워드 인자
- 함수를 호출할 때 키워드 인자를 활용, 직접 변수의 이름으로 특정 인자를 전달.

- 단 `키워드 인자`를 활용한 다음 `위치 인자`를 활용할 수는 없다.

#### 정해지지 않은 여러 개의 인자 처리
- 가변(임의) 인자 리스트(Arbitrary Argument Lists)
  - print() 처럼 개수가 정해지지 않은 임의의 인자를 받기 위해서 `함수를 정의할 때 *args`를 활용
  - 가변 인자 리스트는 `tuple`로 처리.
```python
def func(a, b, c, *d):
    print(a, b, c)
    print(d)
func(1, 2, 3, 4, 5, 6, 7, 8, 9)

# 1 2 3
# (4, 5, 6, 7,8 ,9)
```

```python
def my_func(*args):
    return args
    
print(my_func(1, 2, 'a', [1, 2, 3]))
print(type(my_func(1, 2, 'a', [1, 2, 3])))

# (1, 2, 'a', [1, 2, 3])
# <class 'tuple'>
```

- 가변(임의) 키워드 인자(Arbitrary Keyword Arguments)
  - 정해지지 않은 키워드 인자들은 `함수를 정의할 때 **kwargs`를 활용
  - 가변 키워드 인자는 `dict`로 처리, 매개변수에 `**`로 표현

```python
def func(**kwargs)```