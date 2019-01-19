class FirstClass:   #클래스 객체 정의
    def setdata(self, value):   #클래스 메서드 정의
        self.data = value   #self는 인스턴스
    def display(self):
        print(self.data)    #self.data: 인스턴스마다 존재함

class SecondClass(FirstClass):  #setdata를 상속
    def display(self):  #display 메서드를 변경
        print('Current value = "%s"' % self.data)

class  ThirdClass(SecondClass): #SecondClass로부터 상속
    def __init__(self, value):  #ThirdClass(value) 호출 시
        self.data = value
    def __add__(self, other):   #self + other 호출 시
        return ThirdClass(self.data + other)
    def __str__(self):  #print(self)나 str() 호출 시
        return '[ThirdClass: %s]' % self.data
    def mul(self, other):   #내부의 값을 변경하는 명명된 메서드
        self.data *= other
