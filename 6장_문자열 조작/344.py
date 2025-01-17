import collections
from typing import Deque
import re

class Solution:
    def reverseString(self, s: list[str]) -> None:
        s[:] = s[::-1] # 공간 복잡도 제한 있으면 [:] 사용
        # s.reverse()