class Heap():
    def __init__(self):
        # The default Zero here is used for ease the shift method down there
        self.ourList = list([0])
        self.currentSize = int()
        # We will use this list for the question specifically
        self.qList = [0, 5, 9, 11, 14, 18, 19, 21, 33, 17, 27]

    # To make sure we are following the heap properities after adding the a number as the last element in the heap

    def ShiftUp(self, addedItemIndex):
        while addedItemIndex // 2 > 0:  # Here, having the zero is useful, so that when we divide the zero by 2 at the end we get zero and end the loop

            # if the added item is less than the parent (11//2 = 5 --> 18 | from the formulas 2i+1 and 2i+2 and
            # the decimals are left so that we don't bother ourselves with the one and the 2(lef or right))
            if self.qList[addedItemIndex] < self.qList[addedItemIndex // 2]:
                tmp = self.qList[addedItemIndex // 2]
                # Replace the parent with the child
                self.qList[addedItemIndex // 2] = self.qList[addedItemIndex]
                # Replace the child with the parent
                self.qList[addedItemIndex] = tmp
            # Continue the proces sfor the next parent (even if we don't need to replace because of the loop until we reach the zero)
            """
            We can put an if condition to stop it if the first replacment is not done, but no need to have errors for now
            """
            addedItemIndex = addedItemIndex // 2
        print(self.qList)

    # Just to add, Nothing to expalin HERE
    def AddToHeap(self, k):
        self.qList.append(k)
        self.current_size = len(self.qList)
        self.current_size = self.current_size - 1
        self.ShiftUp(self.current_size)
        print(self.qList)


Test = Heap()

# Test.ShiftUp(9)
Test.AddToHeap(12)
