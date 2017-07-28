import random
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data_dict = {}
        self.data_list = []
        self.length = 0
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.data_dict and self.data_dict[val] >= 0:
            return False
        if self.length == len(self.data_list):
            self.data_list.append(val)
        else:
            self.data_list[self.length] = val
        self.data_dict[val] = self.length
        self.length += 1
        return True

        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.data_dict or self.length <= 0 or self.data_dict[val] < 0:
            return False
        index = self.data_dict[val]
        self.data_list[index] = self.data_list[self.length-1]
        self.length -= 1
        self.data_dict[self.data_list[index]] = index
        self.data_dict[val] = -1
        return True

        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        if self.length <= 0:
            return -1
        index = random.randint(0,self.length-1)
        return self.data_list[index]
        


a = RandomizedSet()
print a.data_dict,a.data_list,a.length
a.insert(0)
print a.data_dict,a.data_list,a.length
a.remove(0)
print a.data_dict,a.data_list,a.length
a.insert(-1)
print a.data_dict,a.data_list,a.length
a.remove(0)
print a.data_dict,a.data_list,a.length