# 08-1.py 이후 작업



final_ticket = {}                       # 비어있는 딕셔너리 생성

for idx in range(ticket_cnt):
    lotto_num = set()                   # set으로 만들면 중복이 제거됨 ( 로또번호 6자리 전부 다르게 하기 위해서)
    while True:
        pick_num = randint(1,46)
        lotto_num.add(pick_num)         #빈set에 랜덤숫자를 집어넣는다. (중복은 제거됨)

        if len(lotto_num) == 6:
            break  #서로 다른 6개의 숫자가 뽑혔으면 while 문을 빠져나온다.
                   #6자리가 아니면 계속 pick_num을 뽑는다.

    key = '티켓%d' % (idx+1)  #딕셔너리에 넣을 key 와 value 정의
    val = sorted(list(lotto_num))
    print(' * {} : {} '.format(key,val))

    final_ticket[key] = val


print("-"*50)
print("생성한 로또번호는 최종적으로 dict형으로 저장")
print("final_ticket =", final_ticket)
