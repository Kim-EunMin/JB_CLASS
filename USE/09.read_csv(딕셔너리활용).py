#행이 몇개든 열이 몇개든 다 읽어오는 csv 함수


def read_csv(filename):
    fp = open(filename, 'r',encoding='utf-8')
    data = fp.read()  #전부
    fp.close()

    rows = data.split('\n')     # 한줄씩 끊어서 읽는다. -> 결과값: [1행, 2행, 3행...]

    
#step1) 컬럼으로 사용되는 것, 실제 내용  구분하기
  
    cols = rows[0].split(',')   # 첫번째줄은 컬럼이다. -> , 를 통해서 분리한다. -> 결과값: [컬럼1내용,컬럼2내용..]
    contents = rows[1:]         # 컬럼을 제외하고 그 이외의 값들 ( 실제 내용이다 )  -> 결과값 : [2행, 3행, 4행...]
  

    final = []
    
    
    for row in contents:          #한줄한줄씩 읽는다.
        fields = row.split(',')   #, 를 기준으로 리스트에 넣어줌 
        
        if len(cols) != len(fields):      #csv사이에 공백인줄이 있더라도 ->  실행될 수 있게 (skip 하게 끔 해준다)
            continue                      # 왜냐면 len(cols) 는 항상 컬럼갯수인데, 공백인줄은 len(fields) 값이 0 이기 때문
            
       
    
        record = {}
       
        for idx in range(len(cols)):       #컬럼갯수
            key   = cols[idx].strip()
            value = fields[idx].strip()
            #print(key,value)
            record[key] = value             #빈딕셔너리에 내용 삽입
            
        final.append(record)
    
    return final            
    

    
filename ="./data/company.csv"
students = read_csv(filename)
for student in students:
    print(student)

    
