class BinarySearch(list):
    """Class """
    
    def toTwenty(self):
        """Function to list numbers from 1-20"""
        num_list = []
        for i in range(1, 21):
            num_list.append(i)
        return num_list


    def toForty(self):
        """Function to list numbers from 2-40 at intervals of 2"""
        num_list = []
        for i in range(2, 41, 2):
            num_list.append(i)
        return num_list 

    def toOneThousand(self):
        """Function to list numbers from 10-1000 at intervals of 10"""
        num_list = []
        for i in range(10, 1001, 10):
            num_list.append(i)
        return num_list


    def search(self, num_to_find):
        pass
    


    