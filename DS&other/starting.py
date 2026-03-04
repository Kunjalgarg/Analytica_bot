print("Hello Kunjal")
# print((15+30)/2)
# a=10
# b=20
# print("Sum =",(a+b))
# print("sub =",(a-b),"or",(b-a))
# print("multiply =",(a*b))
# print("floor division =",(a/b))
# print("modulous =",(a%b))
# name="Kunjal"
# print(name)
# a,b,c="pulses","rice","chapati"
# print("Hello"*10)
# name,age="Kunjal",17
# x="Hello Sharifs! "
# y="Kunjal talking"
# z= x+y
# print(z)
# str="Kaashi"
# print(str[3])
# str_2="Kaashi Singh"
# print(str_2[0:6])
# print(str_2)
 
# print(str_2[0:])
# list_names=["Kunjal","Priya","Nimit","Prince","Khushi"]
# print(list_names[1])
# list_names[1]="Paro"
# print(list_names)
# del(list_names[4])
# print(list_names)
# print(len(list_names))
# list_num=[8,2,9,5,6]
# print(max(list_num))
# print(min(list_num))
# merged_list = list_names + list_num
# print(merged_list)
# dict_1={'a':10,'b':20}
# print(dict_1['a'])
# del(dict_1['b'])
# print(dict_1)
def calculate_factorial(number):
    a=1
    while(number>1):
        a = number*a
        number = number-1
    print(a)
        
calculate_factorial(5)
