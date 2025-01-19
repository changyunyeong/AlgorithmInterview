class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
            .lower().split()
                 if word not in banned] # 단어가 아닌 모든 문자 치환

        counts = collections.Counter(words)
        return counts.most_common(1)[0][0] 
            # most_common(1) => [('cherry',4)] _리스트
            # most_common(1)[0] => ('cherry', 4) _ 튜플
            # most_common(1)[0][0] => cherry _ 튜플에서 첫번째 추출