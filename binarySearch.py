def toTwenty():
    """Function to list numbers from 1-20"""
    num_list = []
    for i in range(1, 21):
        num_list.append(i)
    return num_list


def toForty():
    """Function to list numbers from 2-40 at intervals of 2"""
    num_list = []
    for i in range(2, 41, 2):
        num_list.append(i)
    return num_list 

def toOneThousand():
    """Function to list numbers from 10-1000 at intervals of 10"""
    num_list = []
    for i in range(10, 1001, 10):
        num_list.append(i)
    return num_list


def search(num_to_find):
    search_dict = {}
    num_list = []
    if num_to_find in range(1, 21):
        num_list = toTwenty()
    elif num_to_find in range(2, 41, 2):
        num_list = toForty()
    elif num_to_find in range(10, 1001, 10):
        num_list = toOneThousand()
    else:
        print("The number you have entered is out of scope")
        
    #binary search engine    
    found = 0
    bottom = 0
    top = len(num_list) - 1
    while bottom <= top and not found:
        middle = (bottom + top) // 2
        if num_list[middle] == num_to_find:
            found = num_list.index(num_to_find)
            print("The number is on index %d" % found)
            print("It took %d hops to find it" %found)
            print("Length of the original array is %d" %len(num_list))
        elif num_list[middle] < num_to_find:
            bottom = middle + 1
        else:
            top = middle - 1
    search_dict = {'count': found, 'index': found} 
    return search_dict

'''def binarySearch():
    search(4)
    '''

if __name__ == "__main__":
    #num_list = one_to_twenty()
    num_to_find = int(input("Enter number to find:"))
    is_found = search(num_to_find)
    if is_found:
        print("Yeah! Number found")
    else:
        print("The number you entered does not belong to list")
    
    