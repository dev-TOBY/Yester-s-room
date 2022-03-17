#Chapter03_02

# 파이썬 문자형 (중요)

# 문자열 생성
str1 = "I am python"
str2 = 'Python'
str3 = """How are you?"""
str4 = '''Thank you!'''

print(type(str1), type(str2), type(str3), type(str4))
print(len(str1), len(str2), len(str3), len(str4)) # 공백을 포함한 문자의 총 길이(length)
print()

# 빈 문자열
str1_t1 = ''
str2_t2 = str()

print(type(str1_t1), len(str1_t1))
print(type(str2_t2), len(str2_t2))

# 이스케이프 문자 사용
"""
참고 : Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\000 : 널 문자
...
"""
# 예시)
print("I'm boy") #print('I'm boy')에서 문자 내의 작은 따옴표가 겹치지 때문에 사용불가
print('I\'m boy') # \를 사용해서 뒤의 작은 따옴표 이스케이프 형식으로 바꿔줌
print()
print('a \t b') # \t = tab키 만큼 띄움
print('a \n b')
print('a \"\" b')
print()

escape_str1 = "Do you have a \"POCKETMON\"?"
escape_str2 = 'What\'s on TV?'

print(escape_str1)
print(escape_str2)
print()

# 탭, 줄 바꿈
t_s1 = 'Click \t start!'
t_s2 = 'News Line \n Check!'

print(t_s1)
print(t_s2)
print()

# Raw String -> 이스케이프문자를 사용하지 않기위한 변수 선언
raw_s = r'D:\python\test' # 역슬러시가 들어갔지만 r때문에 이스케이프문자가 아님

print(raw_s)

# 멀티라인 입력 -> 역슬래시 사용
multi_str = \
"""
"But God chose the foolish things
of the world to shame the wise;
God chose the weak things of the world
to shame the strong."
Corinthians 1:27
"""
print(multi_str)
print()

# 문자열 연산
str_o1 = 'python'
str_o2 = 'Apple'
str_o3 = 'How Are You Doing'
str_o4 = 'Seoul Busan Daejeon Jinju'

print(str_o1 * 3)
print(str_o1 + str_o2)
print('y' in str_o1)
print('z' in str_o1)
print('P' not in str_o2) # 대소문자를 따로 보기 때문에 대문자 P는 없다
print()

# 문자열 형 변환 -> str() 안에 원하는 값만 넣어주면 변환됨
print(str(66), type(str(66))) # 정수 66이 아니라 문자로서 66을 의미
print(str(10.1), type(str(10.1))) # 실수 10.1이 아니라 문자로서 10.1을 의미
print(str(True), type(str(True))) # bool의 True가 아니라 문자로서 True를 의미
# 문자열 함수(upper, isalnum, startswith, count, endswith, isalpha...)
print('Capitalize:', str_o1.capitalize()) # 첫문자 대문자화
print('endswith?:', str_o2.endswith('e'))
print('replace:', str_o1.replace("thon", "good"))
print('sorted:', sorted('python'))
print('split:', str_o4.split(" ")) # 함수에 들어간 값을 기준으로 나눠줌

# 반복(시퀀스)
im_str = "Good Boy!"

print(dir(im_str)) #__iter__가 출력되면 시퀀스 가능

# 출력
for i in im_str: print(i)

# 슬라이싱
str_sl = "Nice Python" # <- 문자열의 갯수는 0부터 셈
      #  "012345678910"
# 슬라이싱 연습
print(str_sl[0:3]) # 뒷순자보다 -1 갯수만큼 출력됨 (0부터 시작하기 때문 )
print(str_sl[5:11])
print(str_sl[5:]) # 5부터 끝까지 출력
print(str_sl[:11]) # 처음부터 5까지 출력
print(str_sl[:len(str_sl)]) # = 전체길이
print(str_sl[:len(str_sl)-1]) # 전체길이 -1
print(str_sl[0:9:3]) # [0부터:4까지:2칸단위로 출력]
print(str_sl[-5:])
print(str_sl[0:-5])
print(str_sl[::3]) # 처음부터 끝까지 3칸 간격으로 출력
print(str_sl[::-1]) # 음수는 역방향

# 아스키 코드(or 유니코드)
a = 'z'
print(ord(a)) # 아스키 코드로
print(chr(122)) # 문자로
