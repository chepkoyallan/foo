"""The List Abstract Data type"""


class CustomizedPythonList:
    def __init__(self, size=1):
        self.items = [None] * size
        self.number_of_items = 0

    def append(self, item):
        if self.number_of_items == len(self.items):
            # increase the size of the list by allocating a new list and copy all elements
            # to the new list
            new_list = [None] * self.number_of_items * 2
            for k in range(len(self.items)):
                new_list[k] = self.items[k]
            self.items = new_list

        self.items[self.number_of_items] = item
        self.number_of_items += 1
