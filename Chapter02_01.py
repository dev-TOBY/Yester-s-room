# chaper02_01
# 파이썬 완전 기초
# print 사용법

# 기본출력방법
print('python Start')
print("Python Start")
print()  #개행(한칸 띄우기)
print('''Python Start''')
print("""Python Start""")
print()

# seperator option
print('P', 'Y', 'T', 'H', 'O', 'N', sep='-')
print('010', '5798', '6720', sep='-')
print('2022', '02', '14', sep='/')
print()

# end option
print('Welcome to', end=' ')
print('My Space', end='!')
print(' ^^ ')
print()

# file option
import sys

print('Learn Python', file=sys.stdout)
print()

# format 사용(d, s, f)
# d=정수 ex)3, s=문자열 ex)'python', f=실수 ex)3.14353 ->소수가 나와있는 것을 f로처리
print('%s %s' % ('one', 'two'))
print('{} {}'.format('three', 'four'))
print('{1} {0}' .format('five', 'six'))
print()

# %s 사용법
print('%10s' % ('nice')) #%숫자s는 글자포함해서 숫자만큼 칸을 쓰겠다는 것
print('{:>10}' .format('nice'))
print()
print('%-10s' % ('nice')) #음수일 때는 오른쪽부터의 공백
print('{:10}' .format('nice'))
print()
print('{:?>15}' .format('Money')) #공백에 특정문자채우기
print('{:^11}' .format('Money')) #중앙정렬
print('%.5s' % ('pythonstudy')) # 점을 찍어서 해당수만큼만 사용하고 나머지 절삭
print('{:10.5}' .format('pythonstudy')) #공간은 10개 확보하고 5개만 출력
print()

# %d 사용법
print('%d %d %d' % (1,2,3))
print('{} {} {}' .format(1,2,3))
print('%10d' % (12))
print('{:10d}' .format(12))
print()

# %f 사용법
print('%f' % (3.123456789)) #정수부, 소수부를 입력하지 않아서 정해진만큼만 출력
print('{:f}' .format(3.123456789))
print('%1.10f' % (3.123456789)) #정수부, 소수부를 입력해줘야 원하는만큼 출력
print()
print('%08.5f' % (3.123456789)) #8칸을 쓰고 5칸은 소수자리로 쓰겠다
print('{:08.5f}' .format(3.123456789))
