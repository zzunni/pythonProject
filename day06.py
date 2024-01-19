class FlyingMixin:
    def fly(self):
        return f"{self.name}이(가) 하늘을 훨훨 날아갑니다~"

class SwimmingMixin:
    def swim(self):
        return f"{self.name}이(가) 수영을 합니다."
class Poketmon:
    def __init__(self, name):   #생성자(객체가 생성될 때 딱 한번 실행)
        self.name = name

class Charizard(Poketmon,FlyingMixin):
    pass

class Gyarados(Poketmon,SwimmingMixin):
    pass

g1 = Gyarados("갸라도스")
c1 = Charizard("리쟈몽")
print(c1.fly())
print(g1.swim())