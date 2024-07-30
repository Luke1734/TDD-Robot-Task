import numpy as np
import numpy.typing as npt

class Robot():
    __position: npt.NDArray = np.array([0,0])
    __direction: npt.NDArray = np.array([0,0])

    __anticlockwiseRotation: npt.NDArray = np.array([[0,-1],[1,0]])
    __clockwiseRotation: npt.NDArray = np.array([[0,1],[-1,0]])
    
    _directionToMatrixMapping: dict = {"NORTH": np.array([0,1]), "SOUTH": np.array([0,-1]), "EAST": np.array([1,0]), "WEST": np.array([-1,0])}
    _matrixToDirectionMapping: dict = dict((v.tobytes(), k) for k, v in _directionToMatrixMapping.items())

    def __isValidPosition(self, x:int, y:int) -> bool:
        return x>=0 and x<=4 and y>=0 and y<=4 
    
    def place(self, x:int, y:int, direction:str):
        if not self.__isValidPosition(x,y) or direction not in Robot._directionToMatrixMapping.keys():
            return
        self.__position = np.array([x,y]).T
        self.__direction = Robot._directionToMatrixMapping[direction]
        
    def right(self):
        self.__direction = Robot.__clockwiseRotation.dot(self.__direction)
        
    def left(self):
        self.__direction = Robot.__anticlockwiseRotation.dot(self.__direction)

    def move(self):
        newPosition = self.__position + self.__direction
        if self.__isValidPosition(newPosition[0], newPosition[1]):
            self.__position = newPosition
        
    def report(self):
        if np.array_equal(self.__direction, np.array([0,0])):
            return
        direction = Robot._matrixToDirectionMapping[self.__direction.tobytes()]
        print(f"{self.__position[0]},{self.__position[1]},{direction}")