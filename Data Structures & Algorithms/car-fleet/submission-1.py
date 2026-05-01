class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[pos, s] for pos, s in zip(position, speed)]
        stack = []
        cars.sort(reverse=True)
        for pos, s in cars:
            time = (target - pos) / s
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)