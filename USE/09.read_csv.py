#행이 몇개든 열이 몇개든 다 읽어오는 csv 함수


def read_csv(filename):
    fp = open(filename, 'r',encoding='utf-8')
    data = fp.read()  #전부
    fp.close()

    rows = data.split('\n')     # 한줄씩 끊어서 읽는다. -> 결과값: [1행, 2행, 3행...]

    
#step1) 컬럼으로 사용되는 것, 실제 내용  구분하기
    
  cols = rows[0].split(',')   # 첫번째줄은 컬럼이다. -> , 를 통해서 분리한다. -> [컬럼1내용,컬럼2내용..]
    
