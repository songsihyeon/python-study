## Python study

>프로그래머스 문제를 해결하여 파이썬 공부를 하고있습니다.

>study Python to solve the problem of programmers.


## 1) str_check

**문자열인지 아닌지 판별해주는 함수**

> isdigit() 이라는 함수를 사용. 숫자일 때 True 반환, 문자열일 때 False 반환

> isalpha() 라는 isdigit()과는 반대인 함수도 존재함..!


## 2) no_continuous

**list의 연속된 값을 제거해주는 함수**

> list slice를 사용.
```
    ex1) a[1:3] == 1 ~ 2, a[1:] == 1 ~, a[:3] == ~ 2, a[:] == all
    ex2) a[1:10:2] == 1 ~ 9 까지 2 만큼 증가
    ex3) a[-1] == list의 맨 뒤, a[-1:]  == list의 맨 뒤부터(추가), a[:-2] == list 맨 뒤부터 2개 제외
```

> ex_list.append("ex")를 사용. ex_list라는 list에 ex라는 원소를 추가하는 함수


## 3) check_count

**문자열의 특정한 문자들의 수가 같은 지 판별하는 함수**

> lower()을 사용. 문자열을 소문자로 변환해주는 함수
```
    upper() - lower() 과 반대로 문자열을 대문자로 변환해주는 함수
```

> count()를 사용. 문자열에 괄호 안에 있는 문자가 몇 개인 지 카운팅 해주는 함수


## 4) find_kim

**문자열에서 특정한 문자의 인덱스 값을 찾는 함수**

> index()를 사용. 괄호 안에 있는 문자가 문자열 몇 번째 인덱스인 지 반환해주는 함수

> format()을 사용. 중괄호 안에 포매팅을 지정, 인자로 값을 삽입하는 함수