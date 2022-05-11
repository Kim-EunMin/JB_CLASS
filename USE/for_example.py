import turtle as t

color = ['red','green','blue','yellow','purple','cyan','magenta','violet']
size  = 5   # 나아가는 길이
n     = 1   # 펜싸이즈
angle = 45  # 각도



# for i in range(5):
#     for j in range(8):            #color 하나하나 불러오기 위해서 8을 사용함  (아래방법이 더 효율적)
#         t.pensize(n)
#         t.color(color[j])
#         t.forward(size)
#         t.left(angle)
#         size += 5
#     n += 5


for i in range(45):
    t.pensize(n)
    t.color(color[i%8])             # 나머지를 사용하면 중첩for문 사용하지 않아도 된다.
    t.forward(size)
    t.left(angle)
    size += 5
    n += 1

t.done()

