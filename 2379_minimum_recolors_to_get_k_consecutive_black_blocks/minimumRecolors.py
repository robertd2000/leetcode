class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        black_count = 0
        n = len(blocks)
        min_changes = n

        for i in range(n):
            if i - k >= 0 and blocks[i - k] == 'B':
                black_count -= 1
            if blocks[i] == 'B':
                black_count += 1
            min_changes = min(min_changes, k - black_count)

        return min_changes