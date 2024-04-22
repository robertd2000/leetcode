class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends: 
            return -1
        def neighbors(code):
            for i in range(4):
                x = int(code[i])
                for diff in (-1, 1):
                    y = (x + diff + 10) % 10
                    yield code[:i] + str(y) + code[i + 1:]

        visited = set(deadends)
        
        q = deque([("0000", 0)])
        
        while q:
            code, count = q.popleft()

            if code == target:
                    return count
            for neighbor in neighbors(code):
                
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append((neighbor, count + 1))

        return -1