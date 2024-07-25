from robot import Robot
from pytest import mark

# PLACE
###############################################################################

def test_placeAndReport(capfd):
    """
    Tests that a robot can be placed and a successful report is made
    """
    robot = Robot()
    robot._Robot__place(1,2,"NORTH")
    robot._Robot__report()
    out, _ = capfd.readouterr()
    assert out == "1,2,NORTH\n"
    
    
def test_invalidPlaceAndReport(capfd):
    """
    Tests that a robot with an invalid position is not placed
    """
    robot = Robot()
    robot._Robot__place(9,2,"NORTH")
    robot._Robot__report()
    out, _ = capfd.readouterr()
    assert out == ""
    
    
def test_invalidThenValidPlaceAndReport(capfd):
    """
    Tests that a robot with an invalid position is not placed but
    then any following commands are processed still
    """
    robot = Robot()
    robot._Robot__place(9,2,"NORTH")
    robot._Robot__report()
    robot._Robot__place(1,2,"NORTH")
    robot._Robot__report()
    out, _ = capfd.readouterr()
    assert out == "1,2,NORTH\n"
    
@mark.parametrize("direction", ["NORTH", "SOUTH", "EAST", "WEST"])
def test_eachDirectionPlaceAndReport(capfd, direction:str):
    """
    Tests that each direction option works
    """
    robot = Robot()
    robot._Robot__place(1,2,direction)
    robot._Robot__report()
    out, _ = capfd.readouterr()
    assert out == f"1,2,{direction}\n"
    
    
def test_invalidDirectionPlaceAndReport(capfd):
    """
    Tests that an invalid direction doesn't work
    """
    robot = Robot()
    robot._Robot__place(1,2,"northish")
    robot._Robot__report()
    out, _ = capfd.readouterr()
    assert out == ""
    
#Rotations Right and Left
###############################################################################
def test_clockwiseRotate(capfd):
    """
    Tests that an invalid direction doesn't work
    """
    robot = Robot()
    robot._Robot__place(1,2,"NORTH")
    robot._Robot__right()
    robot._Robot__report()
    out, _ = capfd.readouterr()
    assert out == "1,2,EAST\n"
    robot._Robot__right()
    robot._Robot__report()
    out, _ = capfd.readouterr()
    assert out == "1,2,SOUTH\n"
    robot._Robot__right()
    robot._Robot__report()
    out, _ = capfd.readouterr()
    assert out == "1,2,WEST\n"
    robot._Robot__right()
    robot._Robot__report()
    out, _ = capfd.readouterr()
    assert out == "1,2,NORTH\n"
    
    
def test_anticlockwiseRotate(capfd):
    """
    Tests that an invalid direction doesn't work
    """
    robot = Robot()
    robot._Robot__place(1,2,"NORTH")
    robot._Robot__left()
    robot._Robot__report()
    out, _ = capfd.readouterr()
    assert out == "1,2,WEST\n"
    robot._Robot__left()
    robot._Robot__report()
    out, _ = capfd.readouterr()
    assert out == "1,2,SOUTH\n"
    robot._Robot__left()
    robot._Robot__report()
    out, _ = capfd.readouterr()
    assert out == "1,2,EAST\n"
    robot._Robot__left()
    robot._Robot__report()
    out, _ = capfd.readouterr()
    assert out == "1,2,NORTH\n"
    