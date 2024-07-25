class Robot():
    __x: int = 0
    __y: int = 0
    __direction: str = ""
    
    def __place(self, x:int, y:int, direction:str):
        self.__x = x
        self.__y = y
        self.__direction = direction
        
    def __report(self):
        print(f"{self.__x},{self.__y},{self.__direction}")