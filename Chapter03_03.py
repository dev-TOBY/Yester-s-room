# Chapter03_03

# 파이썬 리스트
# 자료구조에서 중요
#리스트 자료형(순서o, 중복o, 수정o, 삭제o)

# 리스트 선언
a = [] #빈리스트선언
print(type(a))
b = list() #빈리스트선언
c = [70, 75, 80, 85] # 구성요소가 4개
print(len(c))
d = [100, 10000.1 , 'ace', 'captain'] # 서로 다른 자료형을 한 리스트에 정렬 가능
e = [100, 10000.1 , ['ace', 'base', 'captain']] # 리스트 내부에 리스트 가능
f = [4, 10.2, 'coffee', True]
print('---------')


# 인덱싱(내가 원하는 자료를 꺼내오는 과정)
print('d -', type(d), d)
print('d -', d[1])
print('d -', d[0] + d[1] + d[1])
print('d -', d[-1])
print('e -', e[-1][1]) # 리스트 안에서 리스트 목록 출력
print('e -', list(e[-1][1]))
print('---------')

# 슬라이싱
print('d -', d[0:3])
print('d -', d[2:])
print('e -', e[-1][0:3] )
print('---------')

# 리스트 연산 -> 리스트를 연산하면 리스트가 결과로 나온다
print('c + d =', c + d)
print('c * 3 =', c * 3)
print('GoGo + c[0] =', 'GoGo' + str(c[0]))
print('---------')

# 값 비교
print(c == c[:3] + c[3:])
print(c)
print(c[:3] + c[3:])
print('---------')

# Identity(ID)

temp = c
print(temp, c)
print(id(temp))
print(id(c))
print('---------')

# 리스트 수정, 삭제

c[0] = 4
print('c -', c)
c[1:2] = ['a', 'b', 'c']
print('c -', c)
c[1] = ['a', 'b', 'c']
print('c -', c)
c[1:3] = [] # 리스트 삭제
print('c -', c)
del c[2] # 리스트 삭제 2
print('c -', c)
print('---------')

# 리스트 함수
a = [5, 2, 3, 1, 4]

print('a -', a )
a.append(6) # 리스트 추가 ->맨 뒤에 추가
print('a -', a )
a.sort() # 오름차순으로 정렬
print('a -', a )
a.reverse() # 역순으로 정렬
print('a -', a )
print('a -', a.index(3), a[3]) # 둘 다 인덱싱
a.insert(2, 7) # 리스트 삽입(위치, 내가 추가할 값)
print('a -', a )
print('---------')
a.remove(6) # 리스트가 많을 때 일일히 눈으로 보고 숫자를 세서 del에 넣을 수 없기 때문에 remove 함수로 해당 값을 바로 삭제
print('a -', a )
print('a -', a.pop() ) # 가장  끝값을 빼버림
print('a -', a )
print('a -', a.count(2)) # 내가 찾는 값의 갯수를 알아 볼 때

ex = [8, 9]
a.extend(ex) # 값을 삽입하는 함수
print()
print('a -', a )

# 다양한 삭제 방법 : remove(가장 많이 사용), pop(알고리즘에서 사용), del

# 반복문 활용
while a:
    data = a.pop() # 반복문 사용으로 끝부분 원소부터 하나씩 모두 꺼내옴
    print(data)
