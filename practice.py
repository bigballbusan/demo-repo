#숫자형 자료형
print(3)
print(3*5)
print(4+5*3)
#문자형자료
print('사람')
print("아파트")
print("zzzzzz")
print("z"*9)
#참거짓
print(3>7)
print(4<5)
print(True)
print(False)
print(not True)
print(not False)

#변수
#우리집 가족 구성원을 소개해주세요
print("우리집 가족 구성원은 엄마 아빠 그리고 아들입니다.")
print("아들의 취미는 헬스입니다.")
member1="엄마"
member2="아빠"
member3="아들"
hobby="헬스"
print("우리집 가족 구성원은"+member1+member2+"그리고"+member3+"입니다.")
print(member3+"의"+hobby+"는 헬스입니다.")

#연산자
print(1+3)
print(5*2)
print(5/2)
print(5%2)
print(5**2) #5^2
print(5//2) #몫 구하기 
print(5!=1) #!=아니다 True
print(not (5!=1)) #False
print((3>5)and(5>3)) #true
print((3>5)&(5>3))#true
print((3>5)or(5>3))#true 
print(7>6>4) #true
print(7>6>8) #false

#간단한 수식
number=2+3*6
print(number)
number=number+2 #22
number+=2  #24
print(number) #24
number*=2
print(number) #48
number/=2
print(number)#24
number%=2
print(number)#0

#숫자처리함수
print(abs(-5)) #5
print(round(3.14)) #3
print(round(4.99)) #5
print(pow(4,2)) #4^2
print(max(3,4))#4
print(min(3,5))#3

from math import*
print(floor(4.13))#4
print(ceil(4.5))#5
print(sqrt(16))#4

#렌덤함수 
print(rand()) #0.0~1.0중 임의의 수 
print(rand()*10) #0.0~10.0중 임의의 수
print(int(random()*10)) #





