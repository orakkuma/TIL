# Pandas 기초

```python
import pandas as pd
from pandas import Series, DataFrame
import numpy as np
```

```python
# Series => 1차원 배열
s = Series([4, 5, -7, 3])
s

# 0    4
# 1    5
# 2   -7
# 3    3
# dtype: int64
```
```python
s.values
# array([ 4,  5, -7,  3], dtype=int64)

s.index
# RangeIndex(start=0, stop=4, step=1)
```

```python
s = Series([4, 5, -7, 3], index = ['d', 'b', 'a', 'c'])
s

# d    4
# b    5
# a   -7
# c    3
# dtype: int64

# index를 직접 지정 가능
```
```python
s['d']
# 4

s[['c', 'a', 'b']]
# c    3
# a   -7
# b    5
# dtype: int64
```

```python
# s는 Series 객체지만, np함수들에도 사용할 수 있다.

np.exp(s)
# d     54.598150
# b    148.413159
# a      0.000912
# c     20.085537
# dtype: float64

np.max(s)
# 5

'd' in s, 'e' in s
# (True, False)
```

```python
d = Series({'서울' : 123, '인천' : 234, '부산' : 30})
sd = Series(d)
sd
# 서울    123
# 인천    234
# 부산     30
# dtype: int64

dosi = ['부산', '인천', '서울', '대전', '대구']
sd = Series(d, index = dosi)
sd
# 부산     30.0
# 인천    234.0
# 서울    123.0
# 대전      NaN
# 대구      NaN
# dtype: float64

sd.index = ['가', '나', '다', '라', '마']
sd.index.name = '글자'
sd
# 글자
# 가     30.0
# 나    234.0
# 다    123.0
# 라      NaN
# 마      NaN
# Name: 미세먼지, dtype: float6
# => index의 이름 지정
```

```python
# DataFrame => 포/스프레드세트. 여러 col / data row(레코드)
# Series가 여러개 있는 Dict
data = {
    'state' : ['ohio', 'ohio', 'ohio', 'nevada', 'nevada', 'nevada'],
    'year' : [2000, 2001, 2002, 2001, 2002, 2003],
    'pop' : [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]
}

frame = DataFrame(data)
frame
# 	state	year	pop
# 0	ohio	2000	1.5
# 1	ohio	2001	1.7
# 2	ohio	2002	3.6
# 3	nevada	2001	2.4
# 4	nevada	2002	2.9
# 5	nevada	2003	3.2

DataFrame(data, columns=['year', 'state', 'pop'])
# 	year	state	pop
# 0	2000	ohio	1.5
# 1	2001	ohio	1.7
# 2	2002	ohio	3.6
# 3	2001	nevada	2.4
# 4	2002	nevada	2.9
# 5	2003	nevada	3.2
# => column 순서 변경
```

```python
frame2 = DataFrame(data, columns=['year', 'state', 'pop', 'dept'], index = ['one', 'two', 'three', 'four', 'five', 'six'])
frame2
# 	    year	state	pop	dept
# one	2000	ohio	1.5	NaN
# two	2001	ohio	1.7	NaN
# three	2002	ohio	3.6	NaN
# four	2001	nevada	2.4	NaN
# five	2002	nevada	2.9	NaN
# six	2003	nevada	3.2	NaN


frame2['state']
# one        ohio
# two        ohio
# three      ohio
# four     nevada
# five     nevada
# six      nevada
# Name: state, dtype: object

frame2.year
# one      2000
# two      2001
# three    2002
# four     2001
# five     2002
# six      2003
# Name: year, dtype: int64

frame2.loc['three']
# year     2002
# state    ohio
# pop       3.6
# dept      NaN
# Name: three, dtype: object
```

```python
f3 = pd.DataFrame(np.arange(16).reshape((4, 4)), index=['ohio', 'colorado', 'utah', 'new york'], columns=['a', 'b', 'c', 'd'])
f3
# 	        a	b	c	d
# ohio    	0	1	2	3
# colorado	4	5	6	7
# utah	    8	9	10	11
# new york	12	13	14	15


f3 = f3.drop(['new york', 'utah'])
f3
#         	a	b	c	d
# ohio    	0	1	2	3
# colorado	4	5	6	7
# 별말 없으면, row 삭제 => '새로운 DdataFrame' 반환


# col 삭제하려면, axis=1 옵션을 준다.
f3.drop(['a', 'd'], axis=1)
#         	b	c
# ohio    	1	2
# colorado	5	6
# utah	    9	10
# new york	13	14
```

```python
f1 = pd.DataFrame(np.arange(16).reshape((4, 4)), index=['ohio', 'colorado', 'utah', 'new york'], columns=['a', 'b', 'c', 'd'])
f1
# 	        a	b	c	d
# ohio    	0	1	2	3
# colorado	4	5	6	7
# utah	    8	9	10	11
# new york	12	13	14	15

f1[['a', 'c']]
#         	a	c
# ohio	    0	2
# colorado	4	6
# utah	    8	10
# new york	12	14

f1['colorado' : 'utah']
# 	        a	b	c	d
# colorado	4	5	6	7
# utah	    8	9	10	11

# 조건 => row
f1[f1['c'] > 5]
# 	        a	b	c	d
# colorado	4	5	6	7
# utah	    8	9	10	11
# new york	12	13	14	15

f1[f1<5] = 0
f1
#         	a	b	c	d
# ohio	    0	0	0	0
# colorado	0	5	6	7
# utah	    8	9	10	11
# new york	12	13	14	15
```
---
```
# loc, iloc => 특수 index(색인) 필드
# numpy 와 유사하게 축의 라벨을 활용하여 DF의 row/col을 선택 가능.
# 축 이름을 사용할때는 loc
# 정수 index를 사용할 때는 iloc
```
```python
f1.loc['colorado', ['b', 'c']]
# b    5
# c    6
# Name: colorado, dtype: int32

f1.iloc[2, [3, 0, 1]]
# d    11
# a     8
# b     9
# Name: utah, dtype: int32

f1.iloc[[1, 2], [3, 0, 1]]
#         	d	a	b
# colorado	7	0	5
# utah	    11	8	9

f1.iloc[:, :3]
# 	        a	b	c
# ohio	    0	0	0
# colorado	0	5	6
# utah	    8	9	10
# new york	12	13	14

f1.iloc[:, :3][f1['c'] > 10]
# 	        a	b	c
# new york	12	13	1
```
```python
df1 = pd.DataFrame(np.arange(9.).reshape((3,3)), columns=list('bcd'), index=['ohio', 'texas', 'colorado'])
df2 = pd.DataFrame(np.arange(12.).reshape((4,3)), columns=list('bce'), index=['utah', 'ohio', 'texas', 'oregon'])
df1, df2
#             b    c    d
#  ohio      0.0  1.0  2.0
#  texas     3.0  4.0  5.0
#  colorado  6.0  7.0  8.0,
#            b     c     e
#  utah    0.0   1.0   2.0
#  ohio    3.0   4.0   5.0
#  texas   6.0   7.0   8.0
#  oregon  9.0  10.0  11.0
```
```pyton
```