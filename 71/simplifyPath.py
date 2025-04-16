class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        cur = ''

        for c in path:
            if c == '/':
                if cur == '..':
                    stack.pop()
                elif cur != '' and cur != '.':
                    stack.append(c)
                cur = ''
            else:
                cur += c

        return '/' + '/'.join(stack)