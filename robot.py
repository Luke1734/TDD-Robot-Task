class Robot():
    __x: int = 0
    __y: int = 0
    __direction: str = ""
    
    def __place(self, x:int, y:int, direction:str):
        if x<0 or x>4 or y<0 or y>4 or direction not in ["NORTH", "SOUTH", "EAST", "WEST"]:
            return
        self.__x = x
        self.__y = y
        self.__direction = direction
        
    def __report(self):
        if self.__direction == "":
            return
        print(f"{self.__x},{self.__y},{self.__direction}")