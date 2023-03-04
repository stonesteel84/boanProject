# boanProject

## [Metasplotable](https://sourceforge.net/projects/metasploitable/files/latest/download)
- id : msfadmin / pw : msfadmin

## 셸코드 만들기
> msfvenom -p linux/x32/exec CMD='/bin/sh' -f python

### ASLR(메모리가 랜덤하게 생성되기 때문에 끄기)
> echo 0 | sudo tee /proc/sys/kernel/randomize_va_space
