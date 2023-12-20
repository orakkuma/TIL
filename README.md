# Git 업로드 방법

1. 깃허브에서 업로드 하고 싶은 폴더명의 repository를 생성한다.
2. 깃허브에 업로드 하고 싶은 폴더에 마우스 오른쪽 버튼 bash here
3. git init
4. git status
5. touch README.md(일단 업로드 할 파일 아무거나 생성)
6. git add README.md
7. git commit -m "First commit"
8. git remote add origin https://(repository URL)
9. git remote https://(repositor URL)
10. git remote
11. git remote -v
12. git push origin master

## repository 안의 폴더에 업로드 하는 방법
1. 해당 repository로 이동합니다.
2. 새로 만든 폴더로 이동하고, 폴더 내부로 들어갑니다.
3. 폴더 안에 파일을 업로드하려면 폴더 내부의 "Add file" 버튼을 클릭하고, "Upload files"를 선택합니다.
4. 파일을 선택하여 업로드하거나, 파일을 드래그앤드롭하여 업로드합니다.

### Git을 통한 파일 추가 및 푸시
1. 로컬에 Git repository를 클론
   ```
   git clone <repo URL>
   cd <repo 폴더명>
   ```

2. 새로 만든 폴더로 이동, 해당 폴더 안에 파일을 추가
   ```
   mkdir <folder name>
   cd <f.n>

   touch <file name>
   ```

3. 파일을 추가한 후 Git에 추가/커밋
   ```
   git add .
   git commit -m "~"
   ```

4. 변경사항을 원격 저장소에 푸시
   ```
   git push origin master
   ```

동기부여 영상 : https://www.youtube.com/watch?v=V9AGvwPmnZU
