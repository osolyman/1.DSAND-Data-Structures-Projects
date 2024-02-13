import os

def find_files(suffix, path):
    if not os.path.exists(path): # checking if the folder doesn't exist
        return [] # then we return empty list
    
    files_list = [] # otherwise creating an empty list to store the paths of all files with the entered suffix
    items = os.listdir(path) # passing a list of all files and subdirectories in the directory with the entered path to items.
    # iterating over each item.
    for item in items:
        item_path = os.path.join(path, item) # getting the full path of that item by adding the item to the main path
        
        if os.path.isfile(item_path) and item.endswith(suffix):
            # adding the item path to our list in case that this item is a file and
            # this file ends with the entered suffix
            files_list.append(item_path) 
        elif os.path.isdir(item_path):
            # if that item is a directory then we do a recursive call with the item_path
            # saving the list resulted from the recursive function into out files_list
            # the reason of using extend, that we save every element in the list individually
            # to the end of out files_list. and that is why we don't use append because it would
            # save the resulted list from the recursive function as a single element.
            files_list.extend(find_files(suffix, item_path))
    
    return files_list

#Test Case 1:
test_case_1 = find_files(".c", r"C:\Users\ohass\Desktop\Data_Structures_Projects\problem_2\testdir")
print("Test Case 1:", test_case_1) # result should be a list of all files that ends with '.c'

#Test Case 2:
test_case_2 = find_files(".c", r"C:\Users\ohass\Desktop\Data_Structures_Projects\problem_2\emptydir")
print("Test Case 2:", test_case_2) # result should be an empty list

#Test Case 3:
test_case_3 = find_files(".h", r"C:\Users\ohass\Desktop\Data_Structures_Projects\problem_2\testdir")
print("Test Case 3:", test_case_3) # result should be a list of all files that ends with '.h'