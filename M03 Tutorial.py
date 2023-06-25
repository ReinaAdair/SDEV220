# Module 03 Tutorial - Functional vs OOP Programming
# SDEV 220 - Thomas Gordon
# 06/24/2023

class Solution:
    def sort012(self,arr,n):
        arr.sort()
	
    def binarysearch(self, arr, n, k):
        count = 0
        for i in arr:
            if i == k:
                return count
            else:
                count += 1
        if k not in arr:
            count = -1
            return count