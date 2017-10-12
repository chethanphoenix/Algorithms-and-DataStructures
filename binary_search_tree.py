#!/usr/bin/python

class TreeNode():
    def __init__(self):
        self.root = None
        self.left = None
        self.right = None
        self.height = None
        self.balance_factor = None

    def insert(self, value):
        l_h = 0
        r_h = 0
        if self.root == None:
            self.root = value
            self.height = 0
            self.balance_factor = 0
        else:
            if value < self.root:
                if self.left == None:
                    self.left = TreeNode()
                self.left.insert(value)
            else:
                if self.right == None:
                    self.right = TreeNode()
                self.right.insert(value)

            if self.left is not None:
                l_h = self.left.height + 1

            if self.right is not None:
                r_h = self.right.height + 1

            h = max(l_h, r_h)
            self.balance_factor = l_h - r_h
            self.height = h

    def does_node_exists(self, ele):
        lReturn = False
        if ele == self.root:
            lReturn = True
        elif ele < self.root:
            lReturn = self.left.does_node_exists(ele)
        else:
            lReturn = self.right.does_node_exists(ele)

        return lReturn

    def get_height_of(self, ele):
        lReturn = None
        if ele == self.root:
            lReturn = self.height
        elif ele < self.root:
            lReturn = self.left.get_height_of(ele)
        else:
            lReturn = self.right.get_height_of(ele)
        return lReturn

    def get_balance_factor_of(self, ele):
        lReturn = None
        if ele == self.root:
            lReturn = self.balance_factor
        elif ele < self.root:
            lReturn = self.left.get_balance_factor_of(ele)
        else:
            lReturn = self.right.get_balance_factor_of(ele)
        return lReturn

if __name__ == "__main__":
    # array = map(int, raw_input("Enter an array: ").split())
    array = [5, 23, 8, 1, 3, 7, 9, 2]
    tree = TreeNode()
    for ele in array:
        tree.insert(ele)

    i = 0
    # while i < 100:
        # n = int(raw_input("get height of: "))
    print tree.get_balance_factor_of(23), 23
    print tree.get_balance_factor_of(8), 8
    print tree.get_balance_factor_of(1), 1
    print tree.get_balance_factor_of(3), 3
    print tree.get_balance_factor_of(9), 9
    print tree.get_balance_factor_of(2), 2
    print tree.get_balance_factor_of(5), 5
    print tree.get_balance_factor_of(7), 7
    print ""
    print tree.get_height_of(23), 23
    print tree.get_height_of(8), 8
    print tree.get_height_of(1), 1
    print tree.get_height_of(3), 3
    print tree.get_height_of(9), 9
    print tree.get_height_of(2), 2
    print tree.get_height_of(5), 5
    print tree.get_height_of(7), 7

