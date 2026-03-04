##class Solution:
##    def twoSum(self, nums, target):
##        for i in range(len(nums)):
##            for j in range(len(nums)):
##                if(nums[j]==target-nums[i]) and j!=i:
##                    return [i,j]
##
##print("Hello there")    
##number=[3,2,4]
##target=6
##sol= Solution()
##result = sol.twoSum(number,target)
##print(result)
##l1=[2,3,5,4]
##
##class Solution(object):
##    def addTwoNumbers(self,l1,l2):
##        length1= len(l1)
##        b=0
##        print("length of L1=",length1)
##        for i in range(len(l1)-1,-1,-1):
##            a=(10**(length1-1))*l1[i]
##            length1=length1-1
##            b=b+a
##        print(b)
##
##        c=0
##        length2= len(l2)
##        print("length of L1=",length2)
##        for i in range(len(l2)-1,-1,-1):
##            d=(10**(length2-1))*l2[i]
##            length2=length2-1
##            c=c+d
##        print(c)
##        Sum=b+c
##        print("Sum of lists ",b,"+",c,"=",Sum)
##        l3=[]
##        while (Sum%10!=0):
##            Sum2=Sum%10
##            Sum=Sum//10
##            l3.append(Sum2)
##        return l3    
##print(l3)
##sol= Solution()
##l1=[1,2,3]
##l2=[4,5,6]
##result = sol.addTwoNumbers(l1,l2)
##print(result)
