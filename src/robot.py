

class Robot:
    ''' Implement the EMP Mines on Grid avoiding Robot
    '''

    def __init__(self,condition):
        if isinstance(condition, int):
            self.condition = condition
        else:
            raise ValueError('Condition should be an Integer')
    
    def get_condition(self) -> int:
        '''
        Condition given to the robot

        Args:
            self: Instance of class
        Returns:
            int: Return for the condition
        '''
        return self.condition

    def get_bound(self) -> int:
        x_bound = 0
        sum_bound_ints = 0
        if self.condition == 0:
            return 0
        elif self.condition == 1:
            return 1
        else:
            while sum_bound_ints<self.condition+1:
                 x_bound += 1
                 sum_bound_ints = self.sum_of_digits(x_bound)
        return x_bound-1
    
    def sum_of_digits(self,n) -> int:
        lst = self.split_digits(n)
        return sum(lst)

    def split_digits(self,n) -> list:
        return [int(d) for d in str(n)]

    def sum_positions(self,x_position, y_position):
        return self.sum_of_digits(x_position)+ self.sum_of_digits(y_position)

    def get_access_area(self):
        x_position = self.get_bound()
        area_count = 1
        while x_position >=0:
            y_position = 0
            while  self.sum_positions(x_position,y_position) < self.condition+1:
                    y_position += 1
                    area_count += 1
            x_position -= 1
        return area_count*4

    


