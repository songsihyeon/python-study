## python-study

프로그래머스를 이용해 파이썬 공부를 하고있습니다.
Python Study Using Programmers.


## 1 str_check - 문자열인지 아닌지 판별해주는 함수

> isdigit() 이라는 함수를 사용. 숫자일 때 True 반환, 문자열일 때 False 반환

> isalpha() 라는 isdigit()과는 반대인 함수도 존재함..!


## 2 no_continuous - 받은 list의 연속된 값을 제거해주는 함수

> list slice를 사용.
```
    ex1) a[1:3] == 1 ~ 2, a[1:] == 1 ~, a[:3] == ~ 2, a[:] == all
    ex2) a[1:10:2] == 1 ~ 9 까지 2 만큼 증가
    ex3) a[-1] == list의 맨 뒤, a[-1:]  == list의 맨 뒤부터(추가), a[:-2] == list 맨 뒤부터 2개 제외
```

> ex_list.append("ex")를 사용. ex_list라는 list에 ex라는 원소를 추가하는 함수