class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

    def __str__(self):
        return "Value: %d - Weight: %d" % (self.value, self.weight)

    def __repr__(self):
        return self.__str__()

items = [Item(4, 12),
         Item(2, 2),
         Item(2, 1),
         Item(1, 1),
         Item(10, 4),
        ]
c = 0


def ks(items, weight):
    mem = [[0 for j in xrange(weight + 1)]
           for i in xrange(len(items) + 1)]

    grab = [[0 for j in xrange(weight + 1)]
            for i in xrange(len(items) + 1)]

    for i, item in enumerate(items, start=1):
        for j in xrange(1, weight + 1):
            if item.weight <= j:
                if item.value + mem[i][j - item.weight] >= mem[i - 1][j]:
                    mem[i][j] = item.value + mem[i][j - item.weight]
                    grab[i][j] = 1
                else:
                    mem[i][j] = mem[i - 1][j]
            else:
                mem[i][j] = mem[i - 1][j]

    itemList = []
    n = len(items)
    while n > 0 and weight >= 0:
        if grab[n][weight]:
            itemList.append(items[n - 1])
            weight -= items[n - 1].weight
        n -= 1
    return itemList


print ks(items, 15)