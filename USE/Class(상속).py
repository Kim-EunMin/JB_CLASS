#1. 부모클래스 : Animal
#2. Animal 의 자식클래스 : Carnivore, Harbivore  (2개 클래스는 Animal 의 내용을 받아서 사용할 수 있다.)


#부모클래스, Animal
class Animal:
    tribe = '동물'
    def __init__(self, name):
        self.name = name

    def getInfo(self):
        print('나는', self.tribe, self.name, '입니다.')

#자식클래스, Carnivore
class Carnivore(Animal):  # 1. 괄호 안에 상속받을 부모 클래스 이름을 써준다. (Carnivore은 Animal을 내용을 상속받아서 만들어진다)
    def __init__(self, name):
        self.name = name
        self.tribe = '육식동물'
    def favoriteFood(self):
        print('나는 고기를 좋아합니다.')


#자식클래스, Herbivore
class Herbivore(Animal):
    def __init__(self,name):
        self.name = name
        self.tribe = '초식동물'
    def favoriteFood(self):
        print("나는 풀을 좋아합니다.")


#자식클래스, miniAnimal
class miniAnimal(Animal):                 #Animal 부모클래스 안에 name 이란 거 있으니 그걸 사용하면 됨.
    def __init__(self, name):             #self.name = name 이라고 안써줘도 된다.
        Animal.__init__(self, name)       #--->다만, Animal클래스에서 만들어진 생성자를 호출해줘야한다.
        self.tribe = '작은동물'
    def favoriteFood(self):
        print("나는 다 좋아합니다.")




print('-' * 50, "\n[Carnivore 객체 생성]")
tiger = Carnivore('호랑이')
tiger.getInfo() #getInfo 가져와서 사용가능
tiger.favoriteFood()

print('-' * 50, "\n[Herbivore 객체 생성]")
rabit = Herbivore('토끼')
rabit.getInfo()
rabit.favoriteFood()



print('-' * 50, "\n[Mini 객체 생성]")
mini = miniAnimal('미니')
mini.getInfo()
mini.favoriteFood()




#---------------------------------------------예제2-----------------------------------------#
#일반유닛 (부모클래스)
class Unit:
    def __init__(self, name, hp):
        self.name = name   
        self.hp = hp
        

#공격유닛 (자식클래스)
class AttackUnit(Unit):                      # 1.괄호열고 괄호안에 상속받을 클래스명을 적어준다. -> 공격유닛은 일반유닛의 내용을 상속받아서 만들어진다.
    def __init__(self, name, hp, damage):
        Unit.__init__(self,name,hp)          #2. self.name, self.hp 는 지워도됨 -> 다만Unit 클래스에서 만들어진 생성자를 호출해줘야한다.
        self.damage = damage
    
    
    #함수하나 더 만든다.(AttackUnit에 포함된것)
    def attack(self,location):
        print('{0} : {1} 방향으로 적군을 공격합니다. [공격력  {2}]'.format(self.name,  
                                                                          location,  
                                                                          self.damage
                                                                     ))   
        
        
#일반유닛, 공격유닛은 name 과 hp 가 겹친다.
#이럴때 상속을 쓸 수 있다. 물려받는걸 의미함  (unit 의 class 내용을 상속받아서 attack 유닛을 만들 수 있다.)

#똑같이실행된다.
firebat1 = AttackUnit('파이어뱃',50,16)
firebat1.attack('5시')
