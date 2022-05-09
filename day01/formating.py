name = '홍길동'
age  = 10
hobby = 'guiter'


print('{}님, {}살입니다'.format(name,age))
print('%s님, %s살입니다'%(name, age))

print('%d살'%(age))       #d로 하면 숫자형타입을 넣어야한다.


-------------------------------------------------------------------------

coffee1_name = '카페라떼'
coffee2_name = '아메리카노'
coffee3_name = '마끼야또'

coffee1_val = 4500
coffee2_val = 4000
coffee3_val = 5000
coffee_val = coffee1_val + coffee2_val + coffee3_val

print('손님, \n%s, %s, %s를 주문하셨습니다.' % (coffee1_name, coffee2_name, coffee3_name))
print('손님, \n %d 총 가격 입니다'%(coffee_val))

