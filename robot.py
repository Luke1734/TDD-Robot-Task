import numpy as np
import numpy.typing as npt

class Robot():
    __position: int = np.array([0,0])
    __direction: npt.NDArray = np.array([0,0])

    __anticlockwiseRotation: npt.NDArray = np.array([[0,-1],[1,0]])
    __clockwiseRotation: npt.NDArray = np.array([[0,1],[-1,0]])
    
    _directionToMatrixMapping: dict = {"NORTH": np.array([0,1]), "SOUTH": np.array([0,-1]), "EAST": np.array([1,0]), "WEST": np.array([-1,0])}
    _matrixToDirectionMapping: dict = dict((v.tobytes(), k) for k, v in _directionToMatrixMapping.items())

    
    def __place(self, x:int, y:int, direction:str):
        if x<0 or x>4 or y<0 or y>4 or direction not in Robot._directionToMatrixMapping.keys():
            return
        self.__position = np.array([x,y]).T
        self.__direction = Robot._directionToMatrixMapping[direction]
        
    def __right(self):
        self.__direction = Robot.__clockwiseRotation.dot(self.__direction)
        
    def __left(self):
        self.__direction = Robot.__anticlockwiseRotation.dot(self.__direction)
        
    def __report(self):
        if np.array_equal(self.__direction, np.array([0,0])):
            return
        direction = Robot._matrixToDirectionMapping[self.__direction.tobytes()]
        print(f"{self.__position[0]},{self.__position[1]},{direction}")