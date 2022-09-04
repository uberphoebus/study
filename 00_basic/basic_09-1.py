
class Unit:
    
    def __init__(self, name, hp): # 생성자
        self.name = name
        self.hp = hp
        print(f'{name} 유닛 생성')
        print(f'체력 {hp}')
        print('-' * 20)

# 메소드
class AttackUnit(Unit): # 상속
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp) # 상속
        self.damage = damage
    
    def attack(self, loc):
        print(f'{self.name} : {loc} 방향 공격. 공격력 {self.damage}')
    
    def damaged(self, damage):
        print(f'{self.name} : {damage} 데미지 입음')
        self.hp -= damage
        print(f'{self.name} : 현재 체력 {self.hp}')
        if self.hp <= 0:
            print(f'{self.name} 파괴')
            print('-' * 20)

class Flyable:
    def __init__(self, speed):
        self.speed = speed
    
    def fly(self, name, loc):
        print(f'{name} : {loc} 방향으로 비행. 속도 {self.speed}')

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, speed)

# 인스턴스
marine1 = AttackUnit('마린', 40, 5)
marine2 = AttackUnit('마린', 40, 5)
tank = AttackUnit('탱크', 150, 35)

wraith1 = AttackUnit('레이스', 80, 5)
print(f'유닛이름 : {wraith1.name}, 공격력 : {wraith1.damage}')

# 멤버 변수
wraith2 = AttackUnit('레이스2', 80, 5)
wraith2.clocking = True # 외부에서 변수를 추가로 할당

if wraith2.clocking == True:
    print(f'{wraith2.name} 클로킹')

firebat1 = AttackUnit('파이어뱃', 50, 16)
firebat1.attack('5시')

firebat1.damaged(25)
firebat1.damaged(25)

# 다중 상속
valk = FlyableAttackUnit('발키리', 200, 6, 5)
valk.fly(valk.name, '3시')

# 메소드 오버라이딩