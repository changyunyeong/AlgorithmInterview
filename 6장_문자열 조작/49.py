# 그룹 애너그램
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list) # 디폴트 생성

        for word in strs:
            anagrams[''.join(sorted(word))].append(word) # 정렬된 리스트 문자열로 join
        return list(anagrams.values())