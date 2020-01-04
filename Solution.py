import os 
import sys 
import math


class Solution:

    def __init__(self):
        self.maxPalindrome = 1
        pass


    def driver(self, leftIndex:int, rightIndex:int, s:str):
        ##if the right index = the left index then 
        ##recursive call with left Index +1 and right Index = to len(s)-1
        if rightIndex == leftIndex:
            return self.driver(leftIndex+1, len(s)-1, s)
        

        ##if leftIndex is at the end of the string
        if leftIndex >= len(s):
            return self.maxPalindrome
        ##if you found a matching character at left and right index
        ##check the characters between the matching characters
        if s[leftIndex] == s[rightIndex]:
            tempStr = s[leftIndex:rightIndex+1]
            temp1 = leftIndex 
            temp2 = rightIndex 
            ##keeps track of the number of mathcing characters between the first match
            count = 0
            bound = int(len(tempStr)/2)
            for i in range (0, bound):
                if s[temp1] == s[temp2]:
                    count += 1 
                    temp1 += 1
                    temp2 -= 1
            
            ##if the entire substring between leftIndex and rightIndex is a palindrome
            if count == bound:
                count = len(tempStr)
                leftIndex = rightIndex
                rightIndex = len(s)-1
                if count > self.maxPalindrome:
                    self.maxPalindrome = count

                return self.driver(leftIndex, rightIndex, s)
            ##else if it was not a palindrome 
            else:
                return self.driver(leftIndex, rightIndex-1, s)
        
        else:
            return self.driver(leftIndex, rightIndex-1, s)