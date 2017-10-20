def one_to_twenty():
    """Function to list numbers from 1-20"""
    num_list = []
    for i in range(1, 21):
        num_list.append(i)
    return num_list


def two_to_forty():
    """Function to list numbers from 2-40 at intervals of 2"""
    num_list = []
    for i in range(2, 41, 2):
        num_list.append(i)
    return num_list 

def ten_to_thousand():
    """Function to list numbers from 10-1000 at intervals of 10"""
    num_list = []
    for i in range(10, 1001, 10):
        num_list.append(i)
    return num_list


def search(num_to_find):
    num_list = []
    if num_to_find in range(1, 21):
        num_list = one_to_twenty()
    elif num_to_find in range(2, 41, 2):
        num_list = two_to_forty()
    elif num_to_find in range(10, 1001, 10):
        num_list = ten_to_thousand()
    else:
        print("The number you have entered is out of scope")
        
    #binary search engine    
    found = False
    bottom = 0
    top = len(num_list) - 1
    while bottom <= top and not found:
        middle = (bottom + top) // 2
        if num_list[middle] == num_to_find:
            found = True
        elif num_list[middle] < num_to_find:
            bottom = middle + 1
        else:
            top = middle - 1
    return found 

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
    
    