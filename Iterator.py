class TopTenIterator:
    def __init__(self):
        self.num = 1

    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration

    def __iter__(self):
        return self


class TopTen:
    def __init__(self):
        self._internal_iterator = TopTenIterator()  # for manual next()

    def __iter__(self):
        return TopTenIterator()  # fresh iterator for loops

    def __next__(self):
        return next(self._internal_iterator)  # manual next() tracks state
values = TopTen()

print(next(values))  # Output: 1
print(next(values))  # Output: 2

for i in values:
    print(i)         # Output: 1 to 10 (fresh start)
