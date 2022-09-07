

class IDDuplicationException(Exception):
    """
    This Exception is thrown, when an id is added to the generator
    that already exists in the ID queue.
    """

    def __init__(self, id, source):
        self.message = f"IDGenerator: ID duplication detected: Caused by {source}, ID: {id}"
        super().__init__(self.message)


class IDNotFoundException(Exception):
    """
    This Exception is thrown, when an id is removed from the generator queue,
    that has not been there in the first place.
    """
    def __init__(self, id, source):
        self.message = f"IDGenerator: ID not found: Caused by {source}, ID: {id}"
        super().__init__(self.message)


class IDGenerator:
    """
    The IDQueue class implements a 
    """

    def __init__(self, seed_size=2):
        super().__init__()

        self._id_queue = [i for i in range(seed_size)]
        self._size = seed_size

    def _find_successor_position(self, id):
        if self._id_queue[0] >= id:
            return self._id_queue[0]

        pos = 0
        step = int(self._size + 1 / 2)
        while not self._id_queue[pos] < id <= self._id_queue[pos+1]:
            step = int((step + 1) / 2)
            if self._id_queue[pos] < id:
                pos += step
            else:
                pos -= step
        return pos + 1

    def get_id(self):
        if self._id_queue[0] == self._id_queue[-1]:  # Check if there is only one element left
            self._id_queue.append(self._id_queue[-1] + 1)
        return self._id_queue.pop(0)

        

    def add_id(self, id):
        # If the id is larger then the maximal queued id, ad all id's up to the new one at the tail of the queue    
        if id > self._id_queue[-1]:
            self._size += id - self._id_queue[-1]
            self._id_queue.extend(range(self._id_queue[-1] + 1, id + 1))
            

        # Else, search the insertion point, s.t. queue[i] < id < queue[i+1] 
        else:
            insertion_point = self._find_successor_position(id)
            if self._id_queue[insertion_point] == id:
                raise IDDuplicationException(id, "add_id")
            else:
                self._id_queue.insert(insertion_point, id)
                self._size += 1

    def remove_id(self, id) -> None:
        """
        This method removes an id from the queue.
        @args id: The ID to remove
        """
        if id > self._id_queue[-1]:
            self.add_id(id)
            self._id_queue.pop(-1)
            self._size -= 1
        else:
            successor_position = self._find_successor_position(id)
            if self._id_queue[successor_position] != id:
                raise IDNotFoundException(id, "remove_id")
            else:
                self._id_queue.pop(successor_position)
