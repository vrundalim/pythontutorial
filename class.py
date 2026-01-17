class orgnization:
        def info(self):
          print("company's salary cateria")
class Assistant(orgnization):
    def ass(self,salary):
        bouns = 105*salary/100
        print("Asistant bonus is",bouns)
class Emp(orgnization):
    def emp(self,salary):
        bouns = 104*salary/100
        print("Employee bonus is",bouns)
class Man(orgnization):
    def manager(self,salary):
        bouns = 106*salary/100
        print("Manager bonus is",bouns)

a  = Assistant()
e  = Emp()
m = Man()
a.ass(10000)
e.emp(25000)
m.manager(45000)