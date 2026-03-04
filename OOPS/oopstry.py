class length:
    def __init__(d,f=0,inch=0):
        d.feet = f
        d.inch = inch
        print('---')

        
    def display(self):
        return f"{self.feet}'{self.inch}"


length1=length(12)
print(length1.feet, length1.inch)
print(length1.display())

length2=length(3,4)
print(length2.feet, length2.inch)
print(length2.display())

x=5
class scope:
    def scope():
        global x
        x=6
        y=10
        return('inside a function', x)



print("outside a function", x)
