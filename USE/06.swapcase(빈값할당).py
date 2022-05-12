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





#--------------------------------------------------------------------------------------------------------------#

books = list()     #1단계 : 책목록 선언  

books.append({'제목':'파이썬 프로그램', '출판연도':'2016', '출판사':'A', '쪽수':200, '추천유무':False})
books.append({'제목':'플랫폼 비즈니스', '출판연도':'2013', '출판사':'B', '쪽수':584, '추천유무':True})
books.append({'제목':'빅데이터 마케팅', '출판연도':'2014', '출판사':'A', '쪽수':296, '추천유무':True})
books.append({'제목':'외식경영 전문가', '출판연도':'2010', '출판사':'B', '쪽수':526, '추천유무':False})
books.append({'제목':'십억만 벌어보자', '출판연도':'2013', '출판사':'A', '쪽수':248, '추천유무':True})


#아래와 같이 선언해놓고 하는게 좋음
recommends = list()        #책 리스트 선언
all_pages  = int()         #전체 쪽수 변수 선언
pub_companies = set()      #출팝사 집합 선     (set 이니까 unique 한 값만 뽑아낼 수 있음)



for book in books:
    if book['추천유무']:                # boolean 타입이니까 굳이 '==True'를 안써도 됨 (자동으로 true 인 애들만 가져온다)
        recommends.append(book['제목'])
    all_pages += book['쪽수']
    pub_companies.add(book['출판사'])
