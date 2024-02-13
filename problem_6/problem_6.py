class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    output = LinkedList() # creating empty linkedlist to be returned.
    visited = set() # creating empty set (only unique values)

    current_node = llist_1.head # pointer refering to the node where the head is refering to in llist_1
    while current_node: # iterating through the nodes in the first llist.
        if current_node.value not in visited: # if we did not see this value before.
            output.append(current_node.value) # then we add that value to the output linkedlist
            visited.add(current_node.value) # then we mark it as visited by adding it to the set
        current_node = current_node.next # moving to the next node
        
    # the same happens here for llist_2    
    current_node = llist_2.head
    while current_node:
        if current_node.value not in visited:
            output.append(current_node.value)
            visited.add(current_node.value)
        current_node = current_node.next
        
    return output

def intersection(llist_1, llist_2):
    output = LinkedList() # creating empty linkedlist to be returned.
    # the porpuse is to add every unique value in the passed llist_1 and llist_2
    # in sets to get jus the unique values and use the intersection method in sets
    set_1 = set() # creating empty set1 (only unique values)
    set_2 = set() # creating empty set2 (only unique values)

    current_node = llist_1.head # pointer refering to the node where the head is refering to in llist_1
    while current_node: # iterating through the nodes in the first llist.
        set_1.add(current_node.value) # adding the value of the node to set_1
        current_node = current_node.next # moving to the next node
    
    # the same happens here for llist_2 
    current_node = llist_2.head
    while current_node:
        set_2.add(current_node.value)
        current_node = current_node.next
    
    final_set = set_1.intersection(set_2) # creating a new set of the intersection of set_1 and set_2
    for element in final_set: # iterating through that final_set
        output.append(element) # adding every value from the intersection set to the created output likedlist

    return output

## Test Case 1
# expecting to get union and intersection LinkedLists
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

print()
print("Test Case 1:")
if element_1 or element_2:
    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)
    print ("Union:",union(linked_list_1,linked_list_2))
else:
    print ("both Linkedlists are empty. Union operation is not possible.")

if element_1 and element_2:
    if set(element_1).intersection(set(element_2)):
        for i in element_1:
            linked_list_1.append(i)

        for i in element_2:
            linked_list_2.append(i)
        
        print ("Intersection:",intersection(linked_list_1,linked_list_2))
    else:
        print ("No common data found for intersection.")
else:
    print ("At least one of both Linkedlists is empty. Intersection is not possible.")

## Test case 2
# expecting to get union LinkedList but no intersection
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

print()
print("Test Case 2:")
if element_1 or element_2:
    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)
    print ("Union:",union(linked_list_3,linked_list_4))
else:
    print ("both Linkedlists are empty. Union operation is not possible.")

if element_1 and element_2:
    if set(element_1).intersection(set(element_2)):
        for i in element_1:
            linked_list_3.append(i)

        for i in element_2:
            linked_list_4.append(i)
        
        print ("Intersection:",intersection(linked_list_3,linked_list_4))
    else:
        print ("No common data found for intersection.")
else:
    print ("At least one of both Linkedlists is empty. Intersection is not possible.")

## Test Case 3
# expecting to get neither union nor intersection LinkedLists 
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = []
element_2 = []

print()
print("Test Case 3:")
if element_1 or element_2:
    for i in element_1:
        linked_list_5.append(i)

    for i in element_2:
        linked_list_6.append(i)
    print ("Union:",union(linked_list_5,linked_list_6))
else:
    print ("both Linkedlists are empty. Union operation is not possible.")

if element_1 and element_2:
    if set(element_1).intersection(set(element_2)):
        for i in element_1:
            linked_list_5.append(i)

        for i in element_2:
            linked_list_6.append(i)
        
        print ("Intersection:",intersection(linked_list_5,linked_list_6))
    else:
        print ("No common data found for intersection.")
else:
    print ("At least one of both Linkedlists is empty. Intersection is not possible.")

## Test Case 4
# expecting to get union but no intersection LinkedList. 
linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_1 = []
element_2 = [1,7,8,9,11,21,1]

print()
print("Test Case 4:")
if element_1 or element_2:
    for i in element_1:
        linked_list_7.append(i)

    for i in element_2:
        linked_list_8.append(i)
    print ("Union:",union(linked_list_7,linked_list_8))
else:
    print ("both Linkedlists are empty. Union operation is not possible.")

if element_1 and element_2:
    if set(element_1).intersection(set(element_2)):
        for i in element_1:
            linked_list_7.append(i)

        for i in element_2:
            linked_list_8.append(i)
        
        print ("Intersection:",intersection(linked_list_7,linked_list_8))
    else:
        print ("No common data found for intersection.")
else:
    print ("At least one of both Linkedlists is empty. Intersection is not possible.")

## Test Case 5
# expecting to get union and intersection LinkedLists of 1. 
linked_list_9 = LinkedList()
linked_list_10 = LinkedList()

element_1 = [1]
element_2 = [1]

print()
print("Test Case 4:")
if element_1 or element_2:
    for i in element_1:
        linked_list_9.append(i)

    for i in element_2:
        linked_list_10.append(i)
    print ("Union:",union(linked_list_9,linked_list_10))
else:
    print ("both Linkedlists are empty. Union operation is not possible.")

if element_1 and element_2:
    if set(element_1).intersection(set(element_2)):
        for i in element_1:
            linked_list_9.append(i)

        for i in element_2:
            linked_list_10.append(i)
        
        print ("Intersection:",intersection(linked_list_9,linked_list_10))
    else:
        print ("No common data found for intersection.")
else:
    print ("At least one of both Linkedlists is empty. Intersection is not possible.")