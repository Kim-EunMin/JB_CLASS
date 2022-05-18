# data = '''                     #json 은 이처럼 다차원의 형태가 많다. 
# {
#     "name" : "홍길동",
#     "dog"  : {
#         "name" : "순둥이",
#         "toys" : [
#             {"name" : "뽀로로"},
#             {"name" : "토마스"}
#         ]
#     }
# }
# '''


# with open('data/person.json','w') as fp:      #json 을 읽기위해서 (임시로) json 파일 만들어두자
#   fp.write(data)                             #'w' -> write -> json을 생성한다는 뜻 
  

  
  
  
#json 읽어오기


import json

with open('./data/person.json') as data_file:
  person = json.load(data_file)            #  json 파일을 읽어서 person에 담았음
  
  

text = '{}의 개 {}의 장난감은 {}, {}입니다.'.format(
    person["name"],
    person["dog"]["name"],
    person["dog"]["toys"][0]["name"],      #리스트는 인덱스/  #딕셔너리는 키로 불러온다. 
    person["dog"]["toys"][1]["name"]
)
print(text)
