# Chapter03 - 04
# 파이썬 튜플
# 리스트와의 비교 중요 -> 리스트 = [], 튜플 = ()
# 튜플자료형(중복o, 순서o, 수정x, 삭제x) -> 불변

# 선언
a = ()
b = (1,) #  원소가 하나일 땐 콤마를 찍어줘야 튜플로 인식
c = (11, 12, 13, 14)
d = (100, 1000, 'ace', 'base', 'captain')
e = (100, 1000, ('ace', 'base', 'captain'))
print(type(a), type(b))
print('----------')

# 인덱싱
print('d -', d[1])
print(d[1] + d[1] + d[0])
print(e[-1])
print('e -', list(e[-1][1])) # 튜플을 리스트로 변환
print('----------')

# 수정 x
# d[0] = 1500 입력시 에러남

# 슬라이싱
print('d -', d[1:3])
print('d -', d[2:])
print('e -', e[2][0:2])
print('----------')

# 튜플 연산
print('c + d =', c + d)
print('c * 3 =', c * 3)
print('----------')

# 튜플 함수
a = (5, 1, 3, 2, 4)
print('a -', a)
print('a -', a.index(2)) # 원소 2의 위치가 어디냐
print('a -', a.count(2)) # 원소 2의 갯수가 몇개냐
print('----------')

# 팩킹
t = ('qwe', 'asd', 'zxc', 'qux')

print(t)
print(t[0])
print(t[-1])
print('----------')

# 언팩킹
(x1, x2, x3, x4) = t
print(type(x1), type(x2), type(x3), type(x4))
print(x1, x2, x3, x4)
print('----------')

# 팩킹, 언팩킹
t2 = 1, 2, 3  # 괄호가 있던 없던 튜플
t3 = 4,
x1, x2, x3 = t2
x4, x5, x6 = 4, 5, 6

print(t2)
print(t3)
print(x1, x2, x3)
print(x4, x5, x6)
