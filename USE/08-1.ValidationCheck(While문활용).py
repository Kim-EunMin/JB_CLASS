from random import randint
proj_name = '##### 로또번호 생성기 #####'
print(proj_name)



#VALIDATION CHECK (숫자인지 check, 1과 5사이의 숫자인지 check 할것)

while True: 
    ticket_cnt = input('발급할 로또번호 티켓 갯수를 입력하세요.[1~5] =>')
    ticket_cnt = ticket_cnt.strip()  #공백제거

    is_valid = bool()  #True인지 False 인지 판별을 해서 아래쪽에 break 인지 아닌지 판단 (check 역할을 해줌)

    if len(ticket_cnt) == 1:  #글자수 확인
        if ticket_cnt in list('0123456789'):  #['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            ticket_cnt = int(ticket_cnt)
            if 1<= ticket_cnt <=5:
                is_valid = True
            else:
                is_valid = False
        else:
            is_valid = False
    else:
         is_valid = False

    # 위의 if 문을 통해서 is_valid 값을 정의했다.

    if is_valid:
        break  #is_valid 가 true 이면 while 문을 끝낸다.
    else:
        warn_msg = "한번에 발급할 수 있는 티켓은 최소 1개에서 최대 5개 입니다. "
        warn_msg += "다시 입력해주세요." #글자결합
        print(warn_msg)  #false 이면 경고메세지를 보내면서 while 문이 계속 돌아간다.


order_msg = '%d개의 로또번호 티켓을 주문하셨습니다.' % ticket_cnt
print(order_msg)
print("-"*50)

