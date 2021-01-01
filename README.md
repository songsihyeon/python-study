# python-study

프로그래머스를 이용해 파이썬 공부를 하고있습니다.
Python Study Using Programmers.


# 1
str_check - 문자열인지 아닌지 판별해주는 함수
1) isdigit() 이라는 함수를 사용. 숫자일 때 True 반환, 문자열일 때 False 반환
2) isalpha() 라는 isdigit()과는 반대인 함수도 존재함..!


# 2
no_continuous - 받은 list의 연속된 값을 제거해주는 함수
1) list slice를 사용.
    ex1) a[n:m] == n ~ m-1, a[n:] == n ~, a[:n] == ~ n, a[:] == all
    ex2) a[n:m:p] == n ~ m-1 까지 p 만큼 증가
    ex3) a[-1] == list의 맨 뒤, a[-1:]  == list의 맨 뒤부터(추가), a[:-n] == list 맨 뒤부터 n개 제외
2) ex_list.append("ex")를 사용. ex_list라는 list에 ex라는 원소를 추가하는 함수