# 시작
```HTML
<!DOCTYPE html>

<html>
    <!-- Head > Metadat  -->
    <head>
        <!-- 글자 인코딩 -->
        <meta charset="utf-8">
        <!-- 문서의 제목(tab 제목으로 활용) -->
        <title>Hello world</title>
    </head>

    <!-- Body > 실제 문서 표시됨 -->
    <body>
        안녕하세요. 반갑습니다.
    </body>
</html>
```
- HTML 요소는 non-semantic 요소와 semantic 요소로 구분할 수 있다.

- non-semantic
  > div, span 등이 있으며 이들 태그는 content에 대하여 어떤 설명도 하지 않는다.

- semantic 요소
  > form, table, img 등이 있으며 이들 태그는 content의 의미를 명확히 설명한다.

- ```<body>```
  > body tag는 HTML 문서의 내용을 나타내며 웹페이지에 단 하나만 존재한다. 메타데이터를 제외한 웹페이지를 구성하는 대부분의 요소가 body 요소 내에 기술된다.
## heading
VScode와 다른 에디터에는 Emmet이 기본으로 설치되어 있음.
```HTML
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>01 Heading</title>
</head>
<body>
    <h1>가장 큰 제목</h1>
    <!-- h1 = markdown에서 # -->
    <h2>하위제목1</h2>
    <h3>33333</h3>
    <h4>a5555555555</h4>
    <h6>6666666</h6>
    <h2>하위제목2</h2>

    <h2>하위제목3</h2>
</body>
</html>
```
- h = markdown의 # 과 같은 역할

## content
```HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <p>
        <!-- <p>는 문단 나눌 때-->
        안녕하세요 반갑습니다.
    </p>

    <p>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Ea culpa optio maxime animi! Amet alias quis ducimus natus nam pariatur consequuntur, nihil, numquam quibusdam cupiditate quasi, aspernatur deleniti fugit mollitia?
    </p>

    <p>
        <!-- Semantic (의미를 갖는) -->
        이 부분은 <strong>강조1</strong> 할거고
        <br>
        이 부분은 <em>강조2</em> 할거야
        <br>
        <!-- Non Semantic (의미가 없는) -->
        이 부분은 <b>굵게</b> 하고
        <br>
        이 부분은 <i>이탤릭</i>으로 표시할거야.
        <br>
        HTML <small>small</small> formatting
        <br>
        HTML <mark>Marked</mark> Formatting
    </p>
    <p>
        The del element represents deleted (removed) text.</p>
    <p>
        My favorite color is <del>blue</del> red.
    </p>
     <p>
        This is <sub>subscripted</sub> text.
     </p>
    <p>
        This is <sup>superscripted</sup> text.
    </p>
    <blockquote>
      <p>
        Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        </p>
    </blockquote>
    <pre>
        def func(x, y):
            return x + y
    </pre>
</body>
</html>
```
- ```<br>``` 강제 개행. 하지만 여러줄을 띄우고 싶을 땐 쓰는거 권장하지 않음.
- ```<b>, <i>```는 그냥 겉보기만 바꿔주는 역할
- ```<strong>, <em>```은 외형적으로는 위와 같지만, 웹표준을 준수하고자 strong, em을 쓰는 것이 권장.
- ```<small>``` small text 지정한다.
- ```<mark>``` 하이라이팅(형광펜 표시)
- ```<del>``` deleted (removed) text를 지정한다.(삭선 표시)
- ```<sub>, <sup>```sub 태그는 subscripted(아래에 쓰인) text를 sup 태그는 superscripted(위에 쓰인) text를 지정한다.(아래첨자, 위첨자 효과)
- ```<blockquote>``` 긴 인용문 블록으로 지정.


## link
```HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>03 link</title>              
</head>
<body>
    <!-- Hyper Text => Hyper Link : a Tag (Anchor) -->
    <p>
        <!-- 기본 링크 -->
        구글로 가려면 <a href="https://google.com">GOOGLE</a>을 클릭하세요
    </p>
    <p>
        <!-- 새탭에서 열기 -->
        <a href="https://naver.com"target="_blank">NAVER</a>
    </p>
    <p>
        <!-- 비어있는 링크 생성 -->
        <a href="#">목적지 미정</a>이지만 우선 링크 생성
    </p>
</body>
</html>
```
- target 어트리뷰트는 링크를 클릭했을 때 윈도우를 어떻게 오픈할 지를 지정한다.
  >```<_self>``` 링크를 클릭했을 때 연결문서를 현재 윈도우에서 오픈한다.(기본값)

  > ```<_blank>``` 링크를 클릭했을 때 연결문서를 새로운 윈도우나 탭에서 오픈한다.


## list
```HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>List Elements</h1>
    
    <h2>Ordered List</h2>
    <ol>
        <li>HTML 학습하기</li>
        <li>복습하기</li>
        <li>마크다운 정리하기</li>
        <li>
            내일 내용 예습하기
            <ol>
                <li>CSS</li>
                <li>Bootstrap</li>
            </ol>
        </li>
    </ol>
    <h2>Unordered List</h2>
    <ul>
        <!-- 지금까지 배운 과목/주제들 -->
        <li>Python</li>
        <li><strong>Web</strong></li>
        <li>Django</li>
        <li>DB</li>
        <li>Algorithm</li>

    </ul>
    <ol start="3">
        <li>Coffee</li>
        <li>Tea</li>
        <li>Milk</li>
    </ol>
    <ol reversed> 
        <li>Coffee</li>
        <li>Tea</li>
        <li>Milk</li>
    </ol>
</body>
</html>
```
- ```<start>``` 어트리뷰트로 리스트의 시작값을 지정할 수 있다.
- ```<reversed>``` 어트리뷰트를 지정하면 리스트의 순서값을 역으로 표현한다.

## Table
```HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>05 Table</title>
    <!-- 스타일 정의(Style Sheet) -->
    <style>
        table{
            border: 3px solid black;
            width: 50%;
            border-collapse: collapse;
        th, td {
            border: 1px solid lightcoral;
            padding: 10px;
            text-align: center;
        }
        
    </style>
</head>
<body>
    <h1>Table</h1>
    <table>
        <thead>
            <tr>
                <th>이름</th>
                <th>나이</th>
                <th>전공</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>김김김</td>
                <td>25</td>
                <td>경영</td>
            </tr>
            <tr>
                <td>박박박</td>
                <td>23</td>
                <td>심리</td>
            </tr>
            <tr>
                <td>이이이</td>
                <td>21</td>
                <td>컴공</td>
            </tr>

        </tbody>
    </table>
</body>
</html>
```
- ```<style>``` table style 정보 저장 
- 테이블 태그의 어트리뷰트
  > ```<border>``` 표 테두리 두께 지정. (CSS border property를 사용하는 것이 더 나은 방법이다.)
  > ```<rowspan>``` 해당 셀이 점유하는 행의 수 지정
  > ```<colspan``` 해당 셀이 점유하는 열의 수 지정



## Media
```HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>06 Media</title>
</head>
<body>
    <h1>Media Content</h1>
    <h2>Image</h2>
    <h2>Video (IFrame)</h2>
    <p>
        <!-- 직접 가지고있는(local) 이미지 파일의 위치 -->
        <img src="./orakkuma.jpg" alt="coding rilakkuma image" width="200">
        <!-- 인터넷에서 가져오는 이미지 파일의 주소 -->
        <img src="https://coregenicsoftwares.com/wp-content/uploads/2022/01/clipart2065222-1.png" alt="css3 logo" width="200">
    </p>
    <h2>Video (IFrame)</h2>
    <p>
        <iframe
        widhth="1000"
        height="700"
        src="https://www.youtube.com/watch?v=yzDLOi6HRFU&ab_channel=%EC%A1%B8%EB%A6%B0%EB%88%88" 
        title="youtube"
        frameborder="0"
    
        ></iframe>
    </p>
    <p>
        <audio src="assets/audio/Kalimba.mp3" controls></audio>
    </p>
</body>
</html>
```

## form
```HTML
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>07 Form</title>
</head>
<body>
    <h1>Forms</h1>
    <!-- 양식 -->
    <!-- form action="여기에 아래 데이터를 보낼 목적지 URL을 적는다." -->
    <form action="">
        <div>
            <label for="username-input">username</label>
            <input id="username-input" type="text">
        </div>
        <div>
            <label for="password">password</label>
            <input id="password" type="password">
        </div>
        <div>
            <label for="age">age</label>
            <input id="age" type="number">

        </div>
        <div>
            <label for="email">email</label>
            <input id="email" type="email">
        </div>
        <div>
            <label for="bio">자기소개</label>
            <textarea name="" id="bio" cols="30" rows="10"></textarea>
        </div>
        <div>
            <input type="submit">
        </div>
    </form>
</body>
</html>
```

