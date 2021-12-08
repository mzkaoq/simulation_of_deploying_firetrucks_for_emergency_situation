


class Iterator:
    def __init__(self, list_of_trucks):
        self._list_of_trucks = list_of_trucks
        self._num = 0
        self._end = len(list_of_trucks)

    def __iter__(self):
        return self

    def __next__(self):
        if self._num > self._end:
            raise StopIteration
        else:
            self._num += 1
            return self._list_of_trucks[self._num - 1]