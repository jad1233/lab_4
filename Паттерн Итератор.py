# Iterator Pattern
class Iterator:
    def __init__(self, collection):
        self._collection = collection
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._collection):
            item = self._collection[self._index]
            self._index += 1
            return item
        raise StopIteration

class Collection:
    def __init__(self):
        self._items = []

    def add(self, item):
        self._items.append(item)

    def __iter__(self):
        return Iterator(self._items)

# Usage
collection = Collection()
collection.add(1)
collection.add(2)
collection.add(3)

for item in collection:
    print(item)
