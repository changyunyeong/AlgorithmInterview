class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # idx [0]은 항상 문자이므로 [1]이 숫자인지 문자인지 구별 (문자 > 숫자)
        letters, digits = [], []

        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        letters.sort(key = lambda x: (x.split()[1:], x.split()[0])) # 동일할 경우 식별자 지정해 정렬 
        return letters + digits 