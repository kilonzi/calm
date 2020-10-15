
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

def test_robot_returns_correct_condition():
    robot = Robot(23)
    expected = 23
    actual = robot.get_condition()
    assert expected == actual, "The robot returns correct condition"

def test_x_bound_returns_int():
    robot = Robot(20)
    actual = robot.get_bound()
    assert isinstance(actual,int), "Bound should be an int"

def test_x_bound_returns_zero():
    robot = Robot(0)
    actual = robot.get_bound()
    assert actual == 0 , "Bound should be a Zero"

def test_x_bound_return_one():
    robot = Robot(1)
    actual = robot.get_bound()
    assert actual == 1 , "Bound should be a One"

def test_x_bound_return_correctly():
    robot = Robot(10)
    expected = 28
    actual = robot.get_bound()
    assert actual == expected , "Bound should be a Twenty Eight"

