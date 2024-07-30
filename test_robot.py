from robot import Robot
from pytest import mark

# PLACE
###############################################################################

def test_placeAndReport(capfd):
    """
    Tests that a robot can be placed and a successful report is made
    """
    robot = Robot()
    robot.place(1,2,"NORTH")
    robot.report()
    out, _ = capfd.readouterr()
    assert out == "1,2,NORTH\n"
    
    
def test_invalidPlaceAndReport(capfd):
    """
    Tests that a robot with an invalid position is not placed
    """
    robot = Robot()
    robot.place(9,2,"NORTH")
    robot.report()
    out, _ = capfd.readouterr()
    assert out == ""
    
    
def test_invalidThenValidPlaceAndReport(capfd):
    """
    Tests that a robot with an invalid position is not placed but
    then any following commands are processed still
    """
    robot = Robot()
    robot.place(9,2,"NORTH")
    robot.report()
    robot.place(1,2,"NORTH")
    robot.report()
    out, _ = capfd.readouterr()
    assert out == "1,2,NORTH\n"
    

@mark.parametrize("direction", ["NORTH", "SOUTH", "EAST", "WEST"])
def test_eachDirectionPlaceAndReport(capfd, direction:str):
    """
    Tests that each direction option works
    """
    robot = Robot()
    robot.place(1,2,direction)
    robot.report()
    out, _ = capfd.readouterr()
    assert out == f"1,2,{direction}\n"
    
    
def test_invalidDirectionPlaceAndReport(capfd):
    """
    Tests that an invalid direction doesn't work
    """
    robot = Robot()
    robot.place(1,2,"northish")
    robot.report()
    out, _ = capfd.readouterr()
    assert out == ""
    
#Rotations Right and Left
###############################################################################
def test_clockwiseRotate(capfd):
    """
    Tests that an invalid direction doesn't work
    """
    robot = Robot()
    robot.place(1,2,"NORTH")
    robot.right()
    robot.report()
    out, _ = capfd.readouterr()
    assert out == "1,2,EAST\n"
    robot.right()
    robot.report()
    out, _ = capfd.readouterr()
    assert out == "1,2,SOUTH\n"
    robot.right()
    robot.report()
    out, _ = capfd.readouterr()
    assert out == "1,2,WEST\n"
    robot.right()
    robot.report()
    out, _ = capfd.readouterr()
    assert out == "1,2,NORTH\n"
    
    
def test_anticlockwiseRotate(capfd):
    """
    Tests that an invalid direction doesn't work
    """
    robot = Robot()
    robot.place(1,2,"NORTH")
    robot.left()
    robot.report()
    out, _ = capfd.readouterr()
    assert out == "1,2,WEST\n"
    robot.left()
    robot.report()
    out, _ = capfd.readouterr()
    assert out == "1,2,SOUTH\n"
    robot.left()
    robot.report()
    out, _ = capfd.readouterr()
    assert out == "1,2,EAST\n"
    robot.left()
    robot.report()
    out, _ = capfd.readouterr()
    assert out == "1,2,NORTH\n"
    

#Move
###############################################################################

def test_validMoveInAllDirections(capfd):
    """
    Tests that moving in all directiosn works by going round in a circle
    """
    robot = Robot()
    robot.place(1,2,"NORTH")
    robot.move()
    robot.report()
    out, _ = capfd.readouterr()
    assert out == "1,3,NORTH\n"
    robot.left()
    robot.move()
    robot.report()
    out, _ = capfd.readouterr()
    assert out == "0,3,WEST\n"
    robot.left()
    robot.move()
    robot.report()
    out, _ = capfd.readouterr()
    assert out == "0,2,SOUTH\n"
    robot.left()
    robot.move()
    robot.report()
    out, _ = capfd.readouterr()
    assert out == "1,2,EAST\n"
    

def test_invalidMoveInAllDirections(capfd):
    """
    Tests that moving in all directiosn works by going round in a circle
    """
    robot = Robot()
    for i in range(0,5):
        robot.place(i,0,"SOUTH")
        robot.move()
        out, _ = capfd.readouterr()
        assert out == f"{i},0,SOUTH\n"

        robot.place(4,i,"EAST")
        robot.move()
        out, _ = capfd.readouterr()
        assert out == f"4,{i},EAST\n"

        robot.place(i,4,"NORTH")
        robot.move()
        out, _ = capfd.readouterr()
        assert out == f"{i},4,NORTH\n"

        robot.place(0,i,"WEST")
        robot.move()
        out, _ = capfd.readouterr()
        assert out == f"0,{i},WEST\n"
    