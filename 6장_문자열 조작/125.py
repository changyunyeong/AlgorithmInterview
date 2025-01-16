import collections
from typing import Deque
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        lst: Deque = collections.deque()
        
        for char in s:
            if char.isalnum():
                lst.append(char.lower())
        
        while len(lst) > 1:
            if lst.popleft() != lst.pop():
                return False
        
        return True
    
    def isPalindrome2(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s) # 정규식 (^: 부정)
        return s == s[::-1] # 문자열 뒤집기