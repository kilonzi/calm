



class Robot:
    def __init__(self,condition):
        if isinstance(condition, int):
            self.condition = condition
        else:
            raise ValueError('Condition should be an Integer')
    
    def get_condition(self):
        return self.condition


robot = Robot(10)
print(robot.condition)