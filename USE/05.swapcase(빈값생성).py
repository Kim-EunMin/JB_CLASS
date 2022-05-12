text = input('영어 대소문자로 이루어진 문장을 입력하세요')

print('모두 대문자로 출력\n' + text.upper())
print('모두 소문자로 출력\n' + text.lower())



new_s = str()                                # 신규 문자열 형 변수 선언  (빈값으로 만들어서 여기에 채워넣을 것이다.)

for c in text:                               # 한글자씩 뜯어서 가져온다.
    if c.islower():    
        new_s += c.upper()                   #소문자이면 -> c를 대문자로 바꿔서 new_s 에 붙인다.
    else:
        new_s += c.lower()  

        
print('대소문자바꿔서 출력\n'+new_s)       #새롭게 할당된 new_s 라는 변수를 출력
# print(text.swapcase())


