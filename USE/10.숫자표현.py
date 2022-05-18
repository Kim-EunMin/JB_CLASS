#1,234,523  콤마찍어서 표현하기

n = '{:,}'.format(1423623)
print(n)




def cs_num(num):
    n = '{:,}'.format(num)
    return n

  
  #이런식으로 함수화해서 common.py 라는 파일에 저장해서 모아두는 것도 실용적이다.
  
  #import kj 처럼 다른 ipynb 에서 사용할땐
  
  #from common import cs_num  (방법1)
  
  #import common
  #cs_num = common.cs_num     (방법2)
  
  #라고 호출한 다음에
  
  #cs_num(123456) 하면 된다.
  



