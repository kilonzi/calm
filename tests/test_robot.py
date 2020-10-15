
import pytest
from src.robot import Robot

def test_robot_init_without_condition():
    with pytest.raises(TypeError) as exc_info:
        robot = Robot()
    assert "__init__() missing 1 required positional argument: 'condition'" in str(exc_info.value)
def test_robot_init_with_str_condition(): 
    with pytest.raises(ValueError) as exc_info:
        robot = Robot("qwertyu")
    assert "Condition should be an Integer" in str(exc_info.value)

def test_robot_int_proper():
    robot = Robot(10)
    print(robot.condition)
    assert int(robot.condition) == 10, "The condition should be 10"