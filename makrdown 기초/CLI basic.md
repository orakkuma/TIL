# CLI basic

`$` : 현재 명령어를 받을 준비가 됐다.

$가 없다면 명령어를 입력해도 아무일이 없다.


`>` 표시가 있다면 동작이 아직 끝나지 않았다.

`ctrl + c` : 현재 명령 취소(c는 cancel)


`touch` : 파일 생성


`ls` : 현재 폴더의 내용물을 보여줌 (list)


`ls -a` : 현재 폴더의 모든 내용물을 보여줌
    
    (-a : all)

`rm` : remove


`mkdir` : 폴더 생성(make directory)


`rmdir` : '빈' 폴더 삭제


`rm -r` : 파일, 폴더 삭제(속에 파일이 있어도 삭제 가능)
    
    `-r` : recursively, -r 자체로는 작동하지 않고 무언가의 뒤에 붙는 옵션

`rm -rf` : 파일/폴더 모두 강제 삭제

    `-f` = force

`ctrl + L` or `clear` : 화면 정리


`cd` : change directory, 해당 폴더로 이동


    `cd + 아무것도 안 치고 enter` : 바로 홈폴더로 이동


`cd ..` : 상위 레벨로 가기(상위 
폴더로 이동)


`..` : 상위 폴더


`.` : 현재 폴더


`~` : 홈 폴더 home directory

`*` : 모든 것

    ex) rm *.txt = 폴더 내 txt 파일 삭제

`/` : root directory, 더 이상 올라가지 못 하는 directory

`.filename` : 숨김 파일

`cp ` : copy

`cp -r` : 파일/폴더 복사

`mv` : 파일/폴더 이동

    mv a.txt ./b.txt

    -> a.txt 이름을 b.txt 로 바꾼다.

`.xxx` : `.`으로 시작 -> 숨김 파일/폴더

