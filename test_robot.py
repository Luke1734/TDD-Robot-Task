from robot import Robot

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