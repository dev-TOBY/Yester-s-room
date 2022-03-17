# Chapter03-1
#숫자형

# 파이썬 지원 자료형
"""
int : 정수
float : 실수
complex : 복소수
bool : 불린
str : 문자열(시퀀스)
list : 리스트(시퀀스)
tuple : 튜플(시퀀스)
set : 집합
dict : 사전
"""

# 데이터 타입
str1 = "python"
bool = True
str2 = 'anaconda'
float_v = 10.0 # 10 = 정수(int), 10.0 = 실수(float) ---> 다름
int_v = 7
list = [str1, str2]
print(list)
dict = {"name" : "Machine learning", 'version' : 2.0}
tuple = (7, 8, 9)
set = {3, 5, 7}
print()

# 데이터 타입 출력
print(type(str1))
print(type(bool))
print(type(str2))
print(type(float_v))
print(type(int_v))
print(type(dict))
print(type(tuple))
print(type(set))

# 숫자형 연산자
"""
+
-
*
/
// : 몫
% : 나머지
abs(x) : 절대값
pow(x, y) = x ** y  = x의 y제곱
"""

# 정수 선언
i = 77
i2 = -14
big_int = 12345670980980984858037

# 정수 출력
print(i)
print(i2)
print(big_int)
print()

# 실수 선언
f = 0.99999
f2 = 3.14
f3 = -3.99
f4 = 3 / 9

# 실수 출력
print(f)
print(f2)
print(f3)
print(f4)
print()

# 연산 실습
i1 = 39
i2 = 939
big_int1 = 3333334433333333355555555555
big_int2 = 9387987921239735487358735973
f1 = 1.1234
f2 = 3.939

# +
print('+++++++')
print('i1 + i2 :', i1 + i2)
print('f1 + f2 :', f1 + f2)
print('big_int1 + big_int2 :', big_int1 + big_int2)
print()

# *
print('*******')
print('i1 * i2 :', i1 * i2)
print('f1 * f2 :', f1 * f2)
print('big_int1 * big_int2 :', big_int1 * big_int2)
print()

# 형 변환 실습
a = 3.
b = 6
c = .7
d= 12.7

# 타입 출력
print(type(a), type(b), type(c), type(d))
print()
# 형 변환  (예시) 실수 -> 정수, 정수 -> 실수)
print(float(b))
print(int(c))
print(int(a))
print(int(d))
print()
print(int(True)) # True = 1, False = 0
print(int(False))
print()
print(float(True))
print(float(False))
print()
print(complex(3))
print(complex('3'))
print(complex(False))
print()

# 수치 연산 함수
print(abs(-7))
x, y = divmod(100, 8) # 100 / 8
print(x, y) # x = 몫, y = 나머지
print(pow(5, 3), 5 ** 3) # = 5의 3제곱
print()

# 외부 모듈
import math

print(math.pi)
print(math.ceil(5.1)) # X(5.1) 이상의 수 중에 가장 작은 정수
