class Solution:
    def reverseWords(self, s: str) -> str:
        stack = []

        for i in s.split(" ")[::-1]:
            stack.append(i)

        return " ".join(filter(lambda x: (x != ""), stack)).strip()