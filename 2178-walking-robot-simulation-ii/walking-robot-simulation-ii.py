class Robot:

    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        self.x, self.y = 0, 0
        self.d = 0
        self.dirmap = {0:"East",1:"North",2:"West",3:"South"}
        self.perimeter = 2 * (self.w + self.h - 2)

    def step(self, num: int) -> None:
        if num == 0:
            return
            
        # Special handling when we are back at (0,0) facing East
        if self.x == 0 and self.y == 0 and self.d == 0:
            if num >= self.perimeter:
                num %= self.perimeter
                if num == 0:
                    self.d = 3  # After full cycles, direction becomes South
                    return

        # Reduce num using modulo (but carefully)
        if num >= self.perimeter:
            num %= self.perimeter

        while num > 0:
            dx, dy = self.dirs[self.d]
            nx, ny = self.x + dx, self.y + dy

            if nx < 0 or nx >= self.w or ny < 0 or ny >= self.h:
                self.d = (self.d + 1) % 4
            else:
                self.x, self.y = nx, ny
                num -= 1
    
    def getPos(self) -> List[int]:
        return [self.x,self.y]

    def getDir(self) -> str:
        return self.dirmap[self.d]


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()