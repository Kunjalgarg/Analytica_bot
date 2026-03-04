##class Solution():
##    def isPalindrome(self, x):
##        c=x
##        reverse=0
##        while (x > 0):
##            digit = x % 10  
##            reverse = reverse * 10 + digit  
##            x = x // 10  
##        return reverse==c
##sol=Solution()
##result=sol.isPalindrome(1001)
##print(result)


##class Solution:
##    def plusOne(self, digits):
##        length1= len(digits)
##        b=0
##        for i in range(len(digits)):
##            a=(10**(length1-1))*digits[i]
##            length1=length1-1
##            b=b+a
##        print("original number=",b)
##        b+=1
##        print("number after addition=",b)
##        l_new=[]
##        while (b!=0):
##            b2=b%10
##            b=b//10
##            l_new.insert(0,b2)
##        print("new list=",l_new)
##        return l_new
##sol=Solution()
##result=sol.plusOne([1,2,3])
##print("final list=",result)


a="Honesty is the best policy"
a=a.replace(" ","")
print(a)
    


#
