class binarySearch(list):
    """Class to execute the binary search"""
    def __init__(self, list_max, step):
        """Initialize the variables"""
        self.list_max = list_max
        self.step = step
        #Finding which list to use
        if self.list_max in self.toTwenty():
            self.extend(self.toTwenty())
        elif self.list_max in self.toForty():
             self.extend(self.toForty())
        elif self.list_max in self.toOneThousand():
             self.extend(self.toOneThousand())

        self.length = len(self)
    
    def toTwenty(self):
        return range(self.step,(self.list_max * self.step)+1,self.step)
    def toForty(self):
        return range(self.step,(self.list_max * self.step)+1,self.step)
    def toOneThousand(self):
        return range(self.step,(self.list_max * self.step)+1,self.step)
    '''
    def toTwenty(self):
        return range(1,21)
    def toForty(self):
        return range(2, 41, 2)
    def toOneThousand(self):
        return range(10, 1001, 10)
    '''

    def search(self, num_to_find):
        bottom = 0
        top = self.length-1
        found = False
        index = 0
        counter = 0

        if num_to_find == self[bottom]:
            index = bottom
            found = True
        elif num_to_find == self[top]:
            index = top
            found = True
        elif num_to_find not in self:
            found = True
            index = -1

        while bottom <= top and not found:
            midpoint = (bottom + top)//2 #split the list into two half 
            # if number is equal to our middle term we return true
            if self[midpoint] == num_to_find: 
                found = True
                index = midpoint
            # else check if number is in lower or upper list and loop though again
            else:
                counter += 1
                if num_to_find < self[midpoint]:
                    top = midpoint-1
                else:
                    bottom = midpoint+1
        return {'count': counter, 'index': index}  



    