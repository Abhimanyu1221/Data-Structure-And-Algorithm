class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last_occurrence = {char: i for i, char in enumerate(s)}
        
        stack = []
        visited = set()
        
        for i, char in enumerate(s):
            if char in visited:
                continue
                
            while stack and stack[-1] > char and last_occurrence[stack[-1]] > i:
                removed_char = stack.pop()
                visited.remove(removed_char)
                
            stack.append(char)
            visited.add(char)
            
        return "".join(stack)
