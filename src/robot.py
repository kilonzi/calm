class Robot:
    ''' Implement the EMP Mines on Grid avoiding Robot
    '''

    def __init__(self,condition) ->int:
        if isinstance(condition, int):
            self.condition = condition
        else:
            raise ValueError('Condition should be an Integer')
    
    def get_condition(self) -> int:
        '''
        Returns the condition given during initilisation

        Args: 
            self: An instance of the class

        Returns:
            int: An integer with the condition/danger areas
        '''
        return self.condition

    def get_bound(self) -> int:
        '''
        Returns the upper bound beyond which the robot cannot travel to 

        Args: 
            self: An instance of the class

        Returns:
            int: An integer with the x integer bound
        '''
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
        '''
        Returns the sum of all the 

        Args: 
            self: An instance of the class

        Returns:
            int: An integer with the condition/danger areas
        '''
        lst = self.split_digits(n)
        return sum(lst)

    def split_digits(self,n) -> list:
        '''
        Returns the list of individual digits of the positions

        Args: 
            self: An instance of the class
            position: The position integer
        Returns:
            list: The list all the digits in the position.]
        '''
        return [int(d) for d in str(n)]

    def sum_positions(self,x_position, y_position):
        '''
        Returns the sum of individual x and y positions

        Args: 
            self: An instance of the class
            x_position = x position/coordinates
            y_position = y position/coordinates
        Returns:
            int: The sum of all the digits in the position.
        '''
        return self.sum_of_digits(x_position)+ self.sum_of_digits(y_position)

    def get_access_area(self):
        '''
        Returns the access area of a robot given a condition

        Args: 
            self: An instance of the class

        Returns:
            int: An integer defining the total area robot can access
        '''
        y = self.get_bound()
        x = 0
        k = self.get_bound()
        area = 0
        for y in range(self.get_bound()+1):
            for x in range(k,-1,-1):
                if self.sum_positions(x,y)<=self.condition:
                    area += 1
            k -= 1
        return ((area-(y+1))*4)+1