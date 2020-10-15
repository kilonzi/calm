

class Robot:
    ''' Implement the EMP Mines on Grid avoiding Robot
    '''

    def __init__(self,condition):
        if isinstance(condition, int):
            self.condition = condition
        else:
            raise ValueError('Condition should be an Integer')
    
    def get_condition(self) => int:
        '''
        Condition given to the robot

        Args:
            self: Instance of class
        Returns:
            int: Return for the condition
        '''
        return self.condition

    def get_bound(self) => int:
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
    
    def sum_of_digits(self,n) => int:
        lst = self.split_digits(n)
        return sum(lst)

    def split_digits(self,n) => list:
        return [int(d) for d in str(n)]

    


