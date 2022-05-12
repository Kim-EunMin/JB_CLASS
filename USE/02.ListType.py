blackpink_members = ['지수','제니']



# 리스트형 추가
blackpink_members.append('로제')
print('append \t:',blackpink_members)

blackpink_members.insert(1,'리사')            #인덱스 위치까지 지정해줄 수 있음
print('insert \t:', blackpink_members)


#리스트형 삭제
blackpink_members.remove('제니')              #들어간 값으로 삭제
print('remove \t:', blackpink_members)

pickup = blackpink_members.pop(0)             #index 번호로 삭제
print('pop    \t:', blackpink_members, end = ' ----> ')           #원래 print함수의 end 값 디폴트는 뉴라인이다.
print(pickup)                                                     #뉴라인기능 안썻기때문에 화살표 옆에 pickup 값이 출력이 된다



#리스트에서 특정 위치의 요소를 변경하기
solarsys = ['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성']

planet = '화성'
pos = solarsys.index(planet)
solarsys[pos] = 'Mars'
print(solarsys)                                           #화성의 인덱스번호를 뽑아서 -> Mars 로 넣는다.


#리스트의 특정 위치에 요소 삽입하기(insert)
pos = solarsys.index('목성')
solarsys.insert(pos, '소행성')
print(solarsys)                                           #목성앞에 소행성을 넣을 수 있음





