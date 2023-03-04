# boanProject

## [Metasplotable](https://sourceforge.net/projects/metasploitable/files/latest/download)
- id : msfadmin / pw : msfadmin

## 셸코드 만들기
> msfvenom -p linux/x32/exec CMD='/bin/sh' -f python

### ASLR(메모리가 랜덤하게 생성되기 때문에 끄기)
> echo 0 | sudo tee /proc/sys/kernel/randomize_va_space

## 어태치 방법
1. 파이썬의 pwn를 import해서 짜는 프로그램에서 pause()를 사용해서 잠시 멈춘다(enter치면 다시 실행됨)
2. 2. gdb ./~~ <pid>
3. 디버깅을 하고 싶은 부분에 break point를 설정한다. b * main + 38
4. 'conti' 명령어를 쳐서 디버거를 계속 실행시킨다
5. pwn 프로그램에 엔터를 누른다 (sendline)
6. 익스플로잇이 성공했는지 확인한
