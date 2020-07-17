class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.oldest = 0
        # By initializing the array here, we never hit the doubling cost for
        # inserting to a list later, ensuring append is O(1)
        self.storage = [None] * self.capacity

    def append(self, item):
        # save the item to the storage array
        self.storage[self.oldest] = item
        # increment the oldest counter, wrap to 0 if needed
        self.oldest += 1
        if self.oldest == self.capacity:
            self.oldest = 0

    def get(self):
        # return all non-None entries as described in README.md
        return [x for x in self.storage if x is not None]
