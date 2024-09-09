# 자바 변수를 생성할 때, 자료형을 지정한다.
# ex. int number = 1;

# 자바 스크립트 변수를 생성할 때
# ex. let number = 1, const string = ""

# 파이썬 변수를 생성할 때
# ex. number = 1

# 파이썬 기초 자료형
# 숫자형(정수형, int 형)
# number = 0
# number = 1
# number = -1

# 숫자형(실수형, float형)
# number = 1.0
# number = -1.0

# 문자열(str, string)
# string = "문자들의 나열을 의미한다."
# string = '큰타옴표 또는 작은 따옴표를 감싸서 문자열로 만든다.'

# 문자열 포매터(자바스크립트 템플릿 리터럴)
# 문자열 내부 특정 위치에 표현식을 넣는 문법
# 표현식 -> 값, 변수, 연산식(산술, 비교, 논리 등등)

number = 1
string = f"{number} + {number} = {number + number}"

# 불린형(bool, boolean, 논리형)
# boolean a = true; //자바
# a = true; //자바 스크립트
# a = True //파이썬

# 참, 거짓 2개의 값만 가지는 자료형
# 다른 자료형의 불린형으로의 형 변환
# 거짓(False) 변환되는 값이 정해져있다.
# 0, 0,0, "" -> 거짓
# " "(공백) -> 참

# 파이썬에서 다른 자료형으로의 형 변환
# 자료형명(값)
# 정수형 변환 int()
# 실수형 변환 float()
# 문자열 변환 str()
# 불리언 변환 bool()

# 형변환 시 주의사항
# 정수형으로 변환할 수 없는 경우
# 문자열의 경우, 정수형 형태(모양)의 값이 아니면 변환할 수 없다
# print(int("1.0")) -> 에러
# pring(int(float("1.0")))

# 실수형을 정수형으로 변환하면 내림이 발생한다.
print(int(1.1))
print(int(1.5))
print(int(1.9))

# 파이썬 반올림 함수
print(round(1.5))
print(round(2.5)) # 반올림 결과 2. 오사오입
print(round(3.5))

# 우리가 아는 반올림은 사사오입
# 4 이하는 내림
# 5 이하는 올림

# 오사오입
# 소수점 5의 앞 숫자가 홀수면 올림
# 소수점 5의 앞 숫자가 짝수면 내림

# 파이썬 내림 함수 floor
import math
print(math.floor(1.5 + 0.5))
print(math.floor(2.5 + 0.5))

# 파이썬 동시 할당
# 한 줄에서 두 개 이상의 변수에 값을 할당하는 방법
a, b = 2, 1
a, b, c = 3, 2, 1

a, b, c = [1, 2, 3] # 언패킹
print(a, b, c)

# 사용자 입력
# 백준, SWEA -> 입력을 위한 코드 필요
# 숫자가 N개 있을 때~~
# 테스트 캐이스가 T개 있다.

# 하나의 값에 대해 입력
# N = input()

# 입력 주의사항
# 입력으로 받은 데이터는 문자열(str)이다.
# 정수 입력이 필요한 경우 형변환 필요
# N = int(input())
# print(type(N))

# 연산자
# 산술
# 사칙연산, 목 계산, 나머지 계산, 제곱 계산
print(9 // 6) # 목 계산
print(9 % 6) # 나머지 계산
print(9 ** 3) # 제곱

# 비교
# 같다, 다르다, 초과, 미만, 이상, 이하
x = 2
print(1 < x < 3)
print(2 <= x <= 3)

# 논리
# and, or, not
print(True and True) # and: 두 값이 참이면 참을 생성
print(True or False) # or: 하나의 값이 참이면 참을 생성

print(1 and 0) # True and False -> False
print(2 and 3)
print(2 or 1)
print(0 or 2)

print(not True)
print(not False)

# 반복 가능한(iterable) 자료형
# 컨테이너 자료형
# 순서가 있는 자료형
# 리스트, 문자열, 튜플, range()

# 파이썬 리스트: 동적 배열을 기반으로 만든 자료형
# 파이썬 리스트 생성: 대괄호 [] / list()
# 리스트 내부의 원소들은 쉼표(,)로 구분해서 작성
list = [1, 2, 3, 4]
# 자료형 구분없이 데이터를 저장할 수 있다.
list = [1, 1.0, "1", True, [1, 2]]

# 원소 추가 / 삭제
# 추가: 리스트.append(값)
list = []
list.append(1)

# 삭제
list = [1, 2, 3]
# 리스트.pop(): 마지막 원소를 꺼낸다
list.pop()
print(list)
# pop() 메서드는 원소를 반환한다
number = list.pop()
print(number)

list.append(2)
# pop(위치) 메서드는 위치에 해당하는 원소를 꺼낸다
number = list.pop(0)
print(number)

# 한번에 하나의 값만 추가할 수 있다.
# list.append(1, 2, 3, 4, 5) -> 오류 발생

# 리스트에 다른 리스트의 원소를 추가하는 메서드
# 리스트.extend(다른 리스트)
list_1 = [2, 3, 4, 5]
list.extend(list_1)
print(list)

# 리스트를 append()로 추가하면 리스트 자체가 추가된다
list.append(list_1)
print(list)

# 리스트 더하기(+) / 곱하기(*)
# 새로운 리스트를 '생성'한다 (기존의 리스트를 수정하는 것과는 다름에 주의)
list = [1, 2]
print(list * 10)
print(list + list)

# 리스트의 인덱싱(원소에 대한 접근)
list = [1, 2, 3]
# 인덱스는 0부터 시작이다
# 마지막 인덱스는 리스트의 길이(원소의 개수) - 1
# 파이썬 음수 인덱스: 뒤에서 부터 찾아간다
print(list[0])
print(list[-1])
print(list[-2])

#len(반복 가능한 자료형): 원소의 개수를 반환한다
end_index = len(list) - 1
print(list[end_index])

# 파이선 리스트 슬라이싱
# 자바스크립트 slice()
# 자바 copyOfRange()
# 일정 부분을 분할하는(자르는) 방법
list = [1, 2, 3, 4, 5]
# 슬라이싱 문법: [start : end : step]
# start 위치 ~ end - 1 위치까지 step만큼 분할
# 첫 번째부터 세 번째까지 분할
print(list[0:3]) # step 생략. 기본값 1이 적용된다.

# 범위를 벗어난 슬라이싱? -> 오류가 x
print(list[0:99])
print(list[1:99])

# 처음부터 마지막까지 간격이 2인 슬라이싱
print(list[0:5:2])

# 음수 인덱스를 통해 슬라이싱
list = [1, 2, 3, 4, 5]
# 음수 인덱스 -5 -4 -3 -2 -1

# [3, 4, 5] 음수 인덱스를 통해 슬라이싱
print(list[-3:-1])
# 간격도 음수로 넣어야 하는건 아닐까?
print(list[-3:-1:-1])
# 음수로 슬라이싱을 하려면?
print(list[-1:-4:-1])
# step이 음수면 반대로 분할이 된다
print(list[::]) # 전체를 의미 [1, 2, 3, 4, 5]
print(list[::-1]) # [5, 4, 3, 2, 1]

# 파이썬 리스트(참조 자료형)의 복사
# 얕은 복사
list_A = [1, 2, 3]
list_B = list_A
print(list_A, list_B)
list_A[0] = 0
list_A[-1] = 99
print(list_A)
print(list_B)

# 깊은 복사
list_A = [1, 2, 3]
# 슬라이싱은 새로운 리스트를 생성
list_B = list_A[::]
list_B[0] = 0
print(list_A, list_B)

# 반복 가능한 자료형 문자열
string = "1 2 3 4"
# 문자열도 인덱싱과 슬라이싱 가능하다
# 문자열은 원소의 수정(추가, 삭제)이 불가능하다
# 더하기 연산을 통해 추가하는 것 처럼 보이게 할 수 있다
string2 = "5 6 7"
# 더하기 연산은 새로운 문자열을 '생성'
string3 = string + string2
print(string3)

# 알고리즘 풀이에 유용한 문자열 메서드

# 문자열.split("기준 문자열")
# 기준 문자열을 기준으로 문자열을 분할 후 리스트를 생성
string = "1,2,3,4,5"
print(string.split(","))
# 기준 문자열 생략하면 공백을 기준으로 분할
string2 = "1 2 3 4 5 6"
print(string2.split())

# "기준문자열".join(리스트)
# 리스트 원소들을 기준 문자열로 구분해서 새로운 문자열을 생성한다
# 리스트는 문자열로 이루어져야 한다
string = ",".join(["1", "2", "3"])
print(string, type(string))

