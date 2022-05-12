#-------------------------------------## for문 한줄에 표현하기 ----------------------------------#
books = list()    
books.append({'제목':'파이썬 프로그램', '출판연도':'2016', '출판사':'A', '쪽수':200, '추천유무':False})
books.append({'제목':'플랫폼 비즈니스', '출판연도':'2013', '출판사':'B', '쪽수':584, '추천유무':True})
books.append({'제목':'빅데이터 마케팅', '출판연도':'2014', '출판사':'A', '쪽수':296, '추천유무':True})
books.append({'제목':'외식경영 전문가', '출판연도':'2010', '출판사':'B', '쪽수':526, '추천유무':False})
books.append({'제목':'십억만 벌어보자', '출판연도':'2013', '출판사':'A', '쪽수':248, '추천유무':True})



many_page  = [book['제목'] for book in books if book['쪽수'] > 250]

recommends = [book['제목'] for book in books if book['추천유무']]

pub_companies = { book['출판사'] for book in books}      #-> set 형 써서 중복제거

all_pages = sum([book['쪽수'] for book in books])




# 위의 코드는 아래와 같음
# for book in books:
#     if book['쪽수'] > 250:
#         many_page.append(book['제목'])
#     if book['추천유무']:                # boolean 타입이니까 굳이 '==True'를 안써도 됨 (자동으로 true 인 애들만 가져온다)
#         recommends.append(book['제목'])
#     all_pages += book['쪽수']
#     pub_companies.add(book['출판사'])






#-------------------------------------## IF문 한줄에 표현하기 ----------------------------------#
color = 'red' if c_mod ==0 else 'green' if c_mod ==1 else 'blue'  


#아래와 같다.
# if c_mod == 0:
#     color = 'red'
# else:
#     if c_mod == 1:
#         color = 'green'
#     else:
#         color = 'blue'

