got the idea of using ordered dictionery from the following stack overflow post:
    https://stackoverflow.com/questions/4443920/python-building-an-lru-cache/8331631#8331631

Efficiency:
            this is a O(1) LRU Cache Implementation using OrderedDict.

Code Design:
            the usage of OrderedDict is because of the ability to maintain the order of insertion. In LRU Cache it is important to be able to track and manage the least recently used item, that's why the ordered dictionery
            is the best choice here.