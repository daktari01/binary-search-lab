class BinarySearch(object):
    def __init__(self, list_size, list_step):
        self.list_step = list_step
        self.list_size = list_size
        
        # Creating our list that we are going to search through
        # Credits to JamesDindi
        # This block check number_list is within our scope
        # i.e, toTwenty is [1, 2, 3 . . . 20]
        if self.list_size in self.toTwenty():
            self.number_list = self.toTwenty()
        elif self.list_size in self.toForty():
            self.number_list = self.toForty()
        elif self.list_size in self.toOneThousand():
            self.number_list = self.toOneThousand()
        
        # self.number_list = list(range(self.list_step, (self.list_size * self.list_step) + 1))[::self.list_step]
        # creating a variable to get length of our list
        self.length = len(self.number_list)

    # we need this to pass ListComprehensionTest
    # look at this as a getter method.
    def __getitem__(self, index):
        return self.number_list[index] # equivalent to one_to_twenty[19]
    
    # methods to return list to search through
    def toTwenty(self):
        return list(range(1,21)) # returns [1, 2, 3 . . . 20]
    
    def toForty(self):
        return list(range(2,41))[::2] # returns [2, 4, 6 . . . 40]
    def toOneThousand(self):
        return list(range(10,1001))[::10] # returns [10, 20, 30 . . . 1000]

	# where the magic happens
	# binary search by iterative method
	# our test expects search to return a dictionary
	# this a standard method to do a binary search
    '''def search(self, number):
        firstIndex = 0
        lastIndex = len(self.number_list) - 1
        found = False
        count = 0
        index = -1 # if the number to find is out of scope the index should be -1

		# Checks if number is the first or last element in our list
		# sets the index to either lastIndex or Firstindex
		# also sets Found to True so that we don't run the while loop
		# credits to EricMiriti
        if number == self.number_list[firstIndex]:
            found = True
            index = firstIndex
        elif number == self.number_list[lastIndex]:
            found = True
            index = lastIndex

		# Iteration. Divide and conquer the list until we get what we want
        while not found and firstIndex <= lastIndex:
			# Count to get how many times we have loop to get out number
            count += 1

			# midpoint is the pivot/center of our list
			# '//' is called 'floor division'
			# instead of rounding up the result we round-down
			# i.e, if result is supposed to be 4.5, floor division will give us 4
            midpoint = (firstIndex + lastIndex) // 2

			# Checks if number in the center is what we are looking for
            if self.number_list[midpoint] == number:
                found = True # set value to true to stop our loop
                return { "count": count, 'index': midpoint }

			# otherwise we will split the list into two and set new values of
			# firstIndex and lastIndex
            elif self.number_list[midpoint] < number:
                firstIndex = midpoint + 1
            else:
                lastIndex = midpoint - 1
            return {"count": 0, "index": index}'''
    def search(self, num_to_find):
        search_dict = {}
        num_list = []
        '''if num_to_find in range(1, 21):
            num_list = toTwenty()
        elif num_to_find in range(2, 41, 2):
            num_list = toForty()
        elif num_to_find in range(10, 1001, 10):
            num_list = toOneThousand()
        else:
            print("The number you have entered is out of scope")
            '''
        #binary search engine    
        found = 0
        bottom = 0
        count = 0
        top = len(num_list) - 1
        while bottom <= top and not found:
            count += 1
            middle = (bottom + top) // 2
            if num_list[middle] == num_to_find:
                found = num_list.index(num_to_find)
                '''print("The number is on index %d" % found)
                print("It took %d hops to find it" %count)
                print("Length of the original array is %d" %len(num_list))'''
            elif num_list[middle] < num_to_find:
                bottom = middle + 1
            else:
                top = middle - 1
        search_dict = {'count': count, 'index': found} 
        return search_dict

#print(number1)

"""
For the condition 'firstIndex <= lastIndex' in line 60.
if we assume that the item we are looking for is not contained in the list
eventually we'll get to a point where the lastIndex is equal to the firstIndex,
meaning that, the midpoint is also equal to firstIndex and lastIndex
and since that last item is NOT the item we are looking for either
"""