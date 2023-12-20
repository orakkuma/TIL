# 마크다운 기초(대제목)

Markdown은 .md 확장자로 생성한다.

## Heading(제목)
제목은 # 으로 시작하며, 한칸 띄고 작성한다.
총 6개의 하위 제목까지 작성할 수 있다.
편의상 가장 큰 제목을 H1이라 지칭하며, 이하 ~H6
1~6까지는 #의 갯수로 구분한다.
# H1
## H2
### H3
#### H4
##### H5
###### H6
H = Hierarchy

## 리스트
### Ordered List(순서 있는 리스트)
1. 손씻기
    1. 물을 틀고(tab 누름)
        1. 수도꼭지를 올리고.
    2. 손을 적시고
    3. 비누를 칠하고
    4. 헹군다.
1. 식당가기
1. 밥 먹기
    - 김치찌개
    - 된장찌개
4. 양치하기
3. 손씻기

##### 첫번째만 1로 시작하면 밑으로는 알아서 해줌.

### Unordered List(순서 없는 리스트)
* or - 

- 중국집
    - 짜장
    - 짬뽕
    - 볶음밥
- 한식집
- 분식집
    - 떡볶이
- 일식집
    * 스시
    * 우동
    * 돈카츠
    * 오코노미야끼


## 인라인 강조

중요한 것은 굵게 표시하고, 주의할 것은 기울이고, 코드나 명령어는 강조하고, 취소선도 긋는다.

중요한 것은 **굵게 표시하고**

*주의할 것은 기울이고*

`코드나 명령어는 강조하고`
` = backtick or backquote`

취소선은 `~~. ~~`

~~취소선도 긋는다.~~

- Bold : **
- Italic : *
- code : backtick ``
- cancel : ~~

## 본문(Paragraph)(내용)
나는 엔터를 치고 싶어
엔터를 쳤는데 실제로 줄바꿈은 되지 않았다.

줄바꿈을 하고 싶으면 엔터를 두번 쳐야한다.



## 블럭 강조
### 표 Table

#### | = (shift  + \(원화 표시) )

|id|이름|나이|
|---|---|---|
|`1`|김김김|20|
|`2`|이이이|25|
|`3`|박박박|23|

### 코드 Code Block

x = 10

y = x + 1

backtick 3개로 감싸고, 처음에 쓰는 언어를 명시하면 문법 표기도 된다.

```python
def function(x,y):
    return x + y
```

```sql
SELECT * FROM users;
```

### 수식 Latex
$ 마크를 사용한다. 레이텍 별도 작성법 학습 필요


#### 인라인 수식
공식은 $x + y$

#### 블럭 수식
$$
\mathbb{N} = \{ a \in \mathbb{Z} : a > 0 \}
$$


## 기타

### 인용문(Quote)
부등소 `>`로 작성

> 우선 유명해져라 
> 
> 그러면 사람들이 박수를 쳐 줄 것이다.

### 가로선(HR, Horizontal Line)
`---` 로 작성
---


### 이미지/링크
```
링크
[표시텍스트](링크)

이미지
![대체텍스트](이미지링크)
```


링크 : [Google](https://google.com)

이미지 : ![리락쿠마](https://i.namu.wiki/i/Moj7B6xO7evaNDCT84MTdLxEuyhKSt9S4QBrwzrtC2TK6V_QVEYXf4vInVlO0ErlI9eCnhWv2kBojjfwJ-6A5zj543qhsk6x--l_nwjpWcsYpjFpkBJM_ry_1Q5_0_aIcMPeHMAARM1T3R-9J8qTGg.webp)

로컬 사진 : ![리락쿠마](./rilakkuma.webp)

노션도 마크다운과 같기 때문에 노션도 추천
