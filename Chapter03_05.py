# Chapter03 - 5
# 파이썬 딕셔너리
# 범용적으로 가장 많이 사용
# 딕셔너리 자료형(순서x, 키 중복허용x, 수정o, 삭제o)
# {} = 딕셔너리, [] = 리스트, () = 튜플

# 선언  --> {키:값(벨류)}
a = {'Name' : 'yester', 'Phone' : '01012345678', 'Birth' : '950927'}
b = {0 : 'Hello'} # 숫자도 키 허용
c = {'arr' : [1, 2, 3, 4]} # 키만 존재하면 값은 어떤 자료형태든 가능
d1 = {
    'Name' : 'Kim',
    'Age' : 26,
    'Birth' : 950927,
    'Job' : 'Agent'
}

d2 = dict([
    ('Name', 'Kim'),
    ('Age', 26),
    ('Birth', 950927),
    ('Job', 'Agent')
]) # 파이썬 문법에서의 정석적인 방법 중 하나이지만 가독성이 좋진 않음

d3 = dict(
    Name='Kim',
    Age=26,
    Birth=950927,
    Job='Agent'
) # 가장 선호하는 방식

print('a -', type(a), a)
print('b -', type(b), b)
print('c -', type(c), c)
print('d -', type(d1), d1)
print('d1 -', type(d2), d2)
print('d2 -', type(d3), d3)

# 출력
print('a -', a['Name'])
print('a -', a.get('Name'))
print('a -', a.get('Name1')) # 키 값을 잘못넣어도 에러가 나지않고 none이라 출력되기 때문에 좀 더 안정적인 개발작업 가능
print('b -', b[0])
print('b -', b.get(0))
print('d3 -', d3.get('Birth'))

# 딕셔너리 추가
a['Address'] = 'Suwon'
print('a -', a)
a['Rank'] = 1
print('a -', a)
print()

# 키의 갯수는?
print('a -', len(a))
print('b -', len(b))
print('c -', len(c))
print('d3 -', len(d3))

# 딕셔너리 함수
# dict_keys, dict_values, dict_items = 반복문(__iter__)에서 사용 가능

print('a -', a.keys())
print('b -', b.keys())
print('c -', c.keys())
print('d3 -', d3.keys())
print()
print('a -', list(a.keys()))
print()
print('a -', a.values())
print('b -', b.values())
print('c -', c.values())
print('d3 -', d3.values())
print()
print('a -', list(a.values()))
print('b -', list(b.values()))
print()
print('a -', a.items())
print('b -', b.items())
print()
print('a -', list(a.items()))
print('b -', list(b.items()))
print()
print('a -', a.pop('Name'))
print('c -', c.pop('arr'))
print('a -', a)
print('c -', c)
print()
print('d3 -', d3.popitem()) # 임의로 하나 꺼냄 - 딕셔너리는 순서가 없기 때문
print('d3 -', d3)
print()
print('a -', 'Birth' in a)
print('a -', 'Bath' in a)
print('d3 -', 'Address' in d3)
print()

# 수정
a['Rank'] = 2
print('a -', a)
print()

a.update(Rank='TOP')
print('a -', a)
print()

temp = {'Birth': 910215}
a.update(temp)
print('a -', a)
