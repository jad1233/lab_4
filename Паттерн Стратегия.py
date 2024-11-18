# Strategy Pattern
class SortStrategy:
    def sort(self, data):
        pass

class BubbleSort(SortStrategy):
    def sort(self, data):
        print("Sorting using Bubble Sort")
        return sorted(data)

class QuickSort(SortStrategy):
    def sort(self, data):
        print("Sorting using Quick Sort")
        return sorted(data, reverse=True)

class Context:
    def __init__(self, strategy: SortStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: SortStrategy):
        self._strategy = strategy

    def execute_strategy(self, data):
        return self._strategy.sort(data)

# Usage
data = [5, 3, 8, 6]
context = Context(BubbleSort())
print(context.execute_strategy(data))  # Bubble Sort

context.set_strategy(QuickSort())
print(context.execute_strategy(data))  # Quick Sort
