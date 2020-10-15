
import pytest
from src.robot import Robot
robot = Robot(10)


def test_robot_init_without_condition():
    with pytest.raises(TypeError) as exc_info:
        robot = Robot()
    assert "__init__() missing 1 required positional argument: 'condition'" in str(exc_info.value)
def test_robot_init_with_str_condition(): 
    with pytest.raises(ValueError) as exc_info:
        robot = Robot("qwertyu")
    assert "Condition should be an Integer" in str(exc_info.value)

def test_robot_int_proper():
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
    expected = 28
    actual = robot.get_bound()
    assert actual == expected , "Bound should be a Twenty Eight"

def test_split_digits_is_list():
     actual = robot.split_digits(1234)
     assert isinstance(actual,list), "Returned should be a list"

def test_split_digits_returned():
     actual = robot.split_digits(1234)
     expected = [1,2,3,4]
     assert actual == expected, "Returned should be [1,2,3,4]"

def test_sum_of_digits():
    actual = robot.sum_of_digits(1234)
    expected = 10
    assert actual==expected, "Should return Ten"

def test_sum_of_digits_return_on_zero():
    actual = robot.sum_of_digits(0)
    expected = 0
    assert actual==expected, "Should return Zero"

def test_sum_of_digits_return_on_one():
    actual = robot.sum_of_digits(10)
    expected = 1
    assert actual==expected, "Should return One"

def test_sum_of_digits_return_an_int():
    actual = robot.sum_of_digits(10)
    assert isinstance(actual,int), "Should return an Int"


