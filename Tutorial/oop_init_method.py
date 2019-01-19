class Employee:

'''
    __init__ method: initialize/constructor
    when we create a method within a class,
    we receive the instance as the first argument automatically.
    By convention, we should call the instance self
    *__init__ 메소드에 정의한 내용이 object/instance를 생성할 때 object/instance를 자동으로 받아서 메소드를 적용시킴
    *인스턴스 생성시에는 self는 자동으로 pass down되기때문에 이외의 arguments값만 입력하면 됨
'''
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):  #instance argument가 자동으로 pass되기때문에 self를 적어야함
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Corey', 'Schafer', 50000)
#eg. emp_1.first = 'Corey', emp_1.last = 'Schafer', emp_1.pay = 50000, etc
#self를 사용함으로써 위의 코드 등을 manually 입력하지 않아도 됨

print(emp_1.email)
print(emp_1.fullname())  # = Employee.fullname(emp_1)
#attribute나 return value가 아닌 method를 실행하기때문에 () 사용
#instance의 경우 self를 따로 적을 필요 없음 - 자동
