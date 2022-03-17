#파이썬 완전 기초
#파이썬 변수

#기본 선언
n = 700

#출력
print(n)
print()
print(type(n))
print()

#동시 선언
x = y = z = 700
print(x, y, z)
print()

#선언(1)
var = 75
print(var)

#재선언(2)
var = 'change value'

#실제 출력값(3)
print(var)     #마지막에 할당된 선언이 기존의 선언과 같으면 덮어써버림
print(type(var)) #str=문자값
print()

#(윗 내용에 대한 이론적 설명)
#object references

#변수의 값이 할당된 상태일 떄
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔 출력  - 이러한 순서로 작동

#예1)
print(300) #40번의 코드를 편의성을 위해 이렇게만 표현하는 것
print(int(300))
print()

#예2)
n = 700
print(n, type(n))
print()
m = n # m = n = 700
print(m, n)
print(type(n), type(m))
print()

m = 900 #재선언
print(m, n)
print(type(n), type(m))
print()

# id(identity)확인 : 객체의 고유값 확인

m = 800
n = 655

print(id(m))
print(id(n))
print()

print(id(m) == id(n)) # ==는 같냐고 물어보는 것
print()

# 같은 오브젝트 참조
m = 800
n = 800

print(id(m))
print(id(n))
print()

print(id(m) == id(n))
print()

# 다양한 변수 선언
# Camel Case : numberOfCollegeGraduates -처음엔 소문자, 연결되는 다음 첫문자는 대문자 -> Method 선언시 주로 사용
# Pascal Case : NumberOfCollegGraduates - 모든 시작문자가 대문자 -> Class 선언시 사용
# Snake Case : number_of_college_graduates - 모두 소문자, 연결부분에 밑 -> 파이썬에서 변수 선언시 주로 사용

# 케이스별 선언의 예시) 학생의 학년은 3학년이다
studentGrade = 3
StudentGrade = 3 #파스칼 케이스를 변수에 선언하는 것은 좋지 못함
student_grade = 3

# 허용하는 변수 선언법
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 8

# 예약어는 변수명으로 사용 불가
"""
False	def	if	raise
None	del	import	return
True	elif	in	try
and	else	is	while
as	except	lambda	with
assert	finally	nonlocal	yield
break	for	not
class	from	or
continue	global	pass
"""
