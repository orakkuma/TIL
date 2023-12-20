# 함수2
- 함수와 스코프
- 재귀 함수

1. 함수와 스코스(scope)
   - 함수는 코드 내부에 scope를 생성한다. 함수로 생성된 공간은 `local scope`라고 하며, 그 외의 공간인 `global scope`와 구분된다.
     - `global scope` : `코드 어디서든` 참조할 수 있는 공간
     - `local scope` : 함수가 만든 스코프로, 함수 내부에서만 참조할 수 있는 공간
     - `global variable` : global scope에 정의된 변수
     - `local vaiable` : local scope에 정의된 변수

```python
a = 10

def func(b):
    #b, c => local
    c = 20
    print(a, b, c)
func(a)

# 10 10 20
```

```python
x = 10
print('global', x)

def func():
    x = 20
    print('local', x):
func()

print('global', x)

'''
global 10
local 20
global 10
'''
```

   1. 코드가 정의 외부에 있다. `global`
   2. 코드가 함수 정의 내부에 있다. `local`
   3. 함수를 호출하면 scope를 만들며, `종료되면 scope 사라진다.`
   4. local -> global 참조는 가능하다. `반대`는 불가능
   5. local 과 global에 같은 변수/함수 등이 있다면, 함수 내부에서는 `local`을 더 우선시 한다.

### 변수의 수명주기
- 변수의 이름은 각자의 lifecycle이 있다.
  - built-in scope : 파이썬이 실행된 이후부터 영원히 유지
  - global scope : 모듈이 호출된 시점 이후 혹은 이름 선언된 이후부터 인터프리터가 끝날 때 까지 유지
  - local scope : 함수가 호출될 때 생성, 함수가 종료될 때까지 유지


## 이름 검색 규칙
파이썬에서 사용되는 식벽자들은 namespace에 저장되어 있다.

아래와 같은 순서로 이름을 찾아나가며, LEGB Rule 이라고 부른다.
- `L`ocal scope : 함수
- `E`nclosed scope : 특정 함수의 상위 함수
- `G`lobal scope : 함수 밖의 변수 혹은 import된 모듈
- `B`uilt-in scope : 파이썬 안에 내장되어 있는 함수

```python
a = 10
b = 20

def enclosed():
    print('부모 함수')
    
    a = 100
    print(a)
    
    def local():
        c = 40
        print(a, b, c)
    local()
    
enclosed()

'''
부모 함수
100
100 20 40
'''
```
```python
a = 10
b = 20

def func():
    global a
    a = 100
    b = 200
    print(a,b)
func()

print(a,b)
'''
100 200
100 20
'''
```

* 기본적으로 함수에서 선언된 변수는 Local scope에 생성되며, 함수 종료 시 사라진다..
* 해당 스코프에 변수가 없는 경우 LEGB rule에 의해 이름을 검색.
    * 변수에 접근은 가능하지만, 해당 변수를 수정할 수는 없다.
    * 값을 할당하는 경우 해당 스코프의 이름공간에 새롭게 생성되기 때문.
    * **단, 함수 내에서 필요한 상위 스코프 변수는 인자로 넘겨서 활용.** (클로저 제외)
* 상위 스코프에 있는 변수를 수정하고 싶다면 global, nonlocal 키워드를 활용 가능.
    * 단, 코드가 복잡해지면서 변수의 변경을 추적하기 어렵고, 예기치 못한 오류가 발생.



# 재귀 함수(recursive function)
재귀 함수는 함수 내부에서 자기 자신을 호출하는 함수를 말한다.

알고리즘을 설계 및 구현에서 유용하게 활용된다.


## factorial

$$
\displaystyle n! = \prod_{ k = 1 }^{ n }{ k }
$$

$$
\displaystyle n! = 1*2*3*...*(n-1)*n
$$

### 반복문을 이용한 팩토리얼 계산

```python
def fact(n):
    result = 1
    for i in range(1, n+1):
        result += 1
        
    return result
fact()
```
```python
def fact_new(n):
    
    result = 1
    
    while n > 1:
        result += n
        n -= 1
    return result
    
fact_new()
```

### 재귀를 이용한 팩토리얼 계산

```python
def factorial(n):
    if n == 1:
        return 1
    return n = factorial(n-1)
'''
n = 5
5 != 1 -> retrun 5 = factorial(4)

n = 4
4 != 1 -> return 4 = factorial(3)

n = 3
3 != 1 -> return 3 = factorial(2)
.
.
n = 1 return 1
```

## Fibonacci Sequence

$$
\displaystyle F_0 = F_1 = 1
$$

$$
F_n=F_{n-1}+F_{n-2}\qquad(n\in\{2,3,4,\dots\})
$$

```python
def fib(n):
    # base case
    if n == 0:
       return 0
    elif n == 1:
        return 1
    
    return fib(n-1) + fib(n-2)
```

```python
def fib_loop1(n):
    result = [0, 1]
    for _ in range(n-1):
        result.append(result[-1] result[-2])
    return result[n]
```

```python
def fib_loop2(n):
    a, b = 0, 1
    while n > 1:
        a, b = b, a + b
        n -= 1
    retrun b
fib_loop2()
```

