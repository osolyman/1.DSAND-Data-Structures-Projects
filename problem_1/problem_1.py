#Problem 1: LRU Cache:

# got the idea of using ordered dictionery from the following stack overflow post:
# https://stackoverflow.com/questions/4443920/python-building-an-lru-cache/8331631#8331631
from collections import OrderedDict

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initializing the class variables
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        # Checking if the entry is in the dictionery
        if key in self.cache:
            # if yes (cache hit), we pop that key and it's value and reinsert it at the end
            # to make sure this entry becomes the most recently used
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        else:
            # otherwise returning -1 (cache miss)
            return -1

    def set(self, key, value):
        # Checking if the entry is in the dictionery
        if key in self.cache:
            # if yes we move that entry to the end of the dict also
            # and after the if statement is done we update it's value with the entered value
            self.cache.pop(key)
        # if that entry is not in the dictionery
        # now checking the capacity
        # if it is at it's capacity
        elif len(self.cache) >= self.capacity:
            if self.cache: # if cache is not empty
                # then we remove the oldest item in the cache
                self.cache.popitem(last = False) # writing last = False ensures that the method removes the oldest(first) item 
        # now adding the new key and value or updating the existing key's value
        # depending on the which case that was
        self.cache[key] = value

our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values

## Test Case 1
empty_cache = LRU_Cache(0)
empty_cache.set(8, 8)
print(empty_cache.get(8)) # returns 8 because we added it in the last step
print(empty_cache.get(2)) # returns -1 because 2 doesn't exist in the cache

## Test Case 2
large_values = LRU_Cache(700)
for i in range(701):
    large_values.set(i, i)
print(large_values.get(658)) # returns 658
print(large_values.get(701)) # returns -1

## Test Case 3
our_cache = LRU_Cache(4)

our_cache.set(1, 1)
our_cache.set(2, 2)
#our_cache.set(0, 0)

print(our_cache.get(1)) # returns 1
print(our_cache.get(2)) # returns 2
print(our_cache.get(0)) # returns -1