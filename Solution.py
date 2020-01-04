import os 
import sys 


class Solution:

    def __init__(self):
        self.maxPalindrome = 1
        pass


    def driver(self, leftIndex:int, rightIndex:int, s:str):
        print(leftIndex, rightIndex)

        ##if the right index = the left index then 
        ##recursive call with left Index +1 and right Index = to len(s)-1
        if rightIndex == leftIndex:
            self.driver(leftIndex+1, len(s)-1, str)
        

        ##if leftIndex is at the end of the string
        if leftIndex >= len(s):
            return self.maxPalindrome
        ##if you found a matching character at left and right index
        ##check the characters between the matching characters
        if s[leftIndex] == s[rightIndex]:
            temp1 = leftIndex 
            temp2 = rightIndex 
            ##keeps track of the number of mathcing characters between the first match
            count = 0
            for i in range((temp2-temp1)/2):
                if s[temp1] == s[temp2]:
                    count += 1 
                    temp1 += 1
                    temp2 -= 1
            
            ##if the entire substring between leftIndex and rightIndex is a palindrome
            if count == (temp2 - temp1)/2:
                count = 2*count
                leftIndex = rightIndex
                rightIndex = len(s)-1
                if count > self.maxPalindrome:
                    self.maxPalindrome = count

                self.driver(leftIndex, rightIndex, s)
            ##else if it was not a palindrome 
            else:
                self.driver(leftIndex, rightIndex-1, s)