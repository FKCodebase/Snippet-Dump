"""
@Author: Fabian Kolesch

This file implements a simple integer ID generator.

DO NOT USE FOR SECURITY RELEVANT CODE.

class IDDuplicationException(Exeception):
    This exception is thrown, when an ID 
    that already exists is added to the id queue.

class IDNotFoundException(Exception):
    This exception is thrown, when an ID
    that does not exist is removed from the id queue.

class IDGenerator:
    This class implements the ID generation.

    def get_id() -> int:
        This method returns a new ID

    def add_id() -> None: (Throws IDDuplicationException)
        This method adds an ID to the genertor queue.

    def remove_id() -> None: (Throws IDNotFoundException)
        This method removes an ID from the generator queue.
"""

import re


class IDDuplicationException(Exception):
    """
    This Exception is thrown, when an id is added to the generator
    that already exists in the ID queue.
    """

    def __init__(self, id, source, max, queue):
        self.message = f"\nIDGenerator: ID duplication detected: Caused by {source}, ID: {id}, MAX: {max} \nQUEUE:\n{queue}"
        super().__init__(self.message)


class IDNotFoundException(Exception):
    """
    This Exception is thrown, when an id is removed from the generator queue,
    that has not been there in the first place.
    """
    def __init__(self, id, source, max, queue):
        self.message = f"\nIDGenerator: ID not found: Caused by {source}, ID: {id}, MAX: {max} \nQUEUE:\n{queue}"
        super().__init__(self.message)

class IDGenerator:
    """
    The IDQueue class implements a simple generator for Unique integer identifiers.
    """

    def __init__(self, seed_size=2):
        """
        Constructor:

        @param: (int) seed_size: The initial number of IDs.
        """

        super().__init__()
        self._id_queue = [i for i in range(seed_size)] # Create the queue with #seed_size IDs
        self._max_element = seed_size - 1 # The maximal queued element
        self._queue_size = seed_size

        self._growth_policy = self.growth_double
        

    def _find_successor_position(self, id) -> int:
        """
        This method uses a binary search like algorithm to
        find the element right of the target id in the queue.

        @param: (int) id: The id to find the successor of.
        @return: (int) position of the right neighbour of the id. 
        """
        pos = int(self._queue_size / 2)
        i = 1
        while not self._id_queue[pos] < id <= self._id_queue[pos+1]: # Neightbour condition
            i += 1
            step = max([int((self._queue_size) / 2**i), 1])  # Update step width
            if self._id_queue[pos] < id:    # Go right if the current element is to small
                pos += step
            else:
                pos -= step # Go left if the current element is to large
        return pos + 1  # Return the right neighbour position

    def get_id(self) -> int:
        """
        This method hands out a new ID.
        
        @return: (int) The new id.
        """

        if self._id_queue[0] == self._id_queue[-1]:  # Check if there is only one element left
            self._grow_to(self._growth_policy()) # Extend the range of IDs

        id =  self._id_queue.pop(0) # Return the first element in the queue
        self._queue_size -= 1
        return id

    def add_id(self, id) -> None:
        """
        This method adds an ID to the queue.

        @param: (int) id: The ID to add to the queue.
        """

        # If the id is larger then the maximal id, ad all id's up to the new one at the tail of the queue    
        if id > self._max_element:
            self._grow_to(id)

        elif id > self._id_queue[-1]:
            self._id_queue.append(id)
            self._queue_size += 1

        elif id < self._id_queue[0]:
            self._id_queue.insert(0, id)
            self._queue_size += 1

        # Else, search the insertion point, s.t. queue[i] < id < queue[i+1] 
        else:
            insertion_point = self._find_successor_position(id) # Find the next right element

            if self._id_queue[insertion_point] == id: # Check if the element is already in the queue (Error)
                raise IDDuplicationException(id, "add_id", self._max_element, self._id_queue)

            else: # Add the element to the queue
                self._id_queue.insert(insertion_point, id)
                self._queue_size += 1

    def remove_id(self, id) -> None:
        """
        This method removes an id from the queue.

        @param id: The ID to remove.
        @return: None.
        """

        if id < self._id_queue[0]: # If the ID is smaller than the smallest one, throw exception 
            raise IDNotFoundException(id, "remove_id", self._max_element, self._id_queue)

        elif id > self._max_element: # If the ID is larger then the largest current one, extend the queue up to (ID + 1)
            self._grow_to(id) # Grow to the new id
            self._id_queue.pop(-1) # Remove the target ID 
            self._queue_size -= 1 # Update the queue size
 
        elif id == self._id_queue[0]: # If the ID is the smallest one in the queue, remove from front
            self._id_queue.pop(0) # Remove the id
            self._queue_size -= 1  # Update the queue size
        
        elif id == self._id_queue[-1]: # If the ID is the largest one in the queue, remove from end
            self._id_queue.pop(-1)
            self._queue_size -= 1

        else: # If the ID is somewhere in the queue, search it
            successor_position = self._find_successor_position(id) # Find the right neighbour (left < ID <= right) of the target ID
            if self._id_queue[successor_position] != id:    # If the position is invalid, throw exception
                raise IDNotFoundException(id, "remove_id", self._max_element, self._id_queue) 
            else:
                self._id_queue.pop(successor_position)  # Remove the ID
                self._queue_size -= 1 # Decrease the queue size

        if self._queue_size == 0: # If the queue is empty after removal, grow the queue
            self._grow_to(self._growth_policy())

    # Linear growth policy
    def growth_linear(self) -> int:
        return self._max_element + 100

    # Double growth policy
    def growth_double(self) -> int:
        return self._max_element * 2
    
    # Squared growth policy
    def growth_square(self) -> int:
        return self._max_element**2
    
    def _grow_to(self, new_max) -> None:
        """
        This method doubles the range of possible IDs
        """
        new_elements = list(range(self._max_element + 1, new_max + 1)) # The list of new elements
        self._id_queue.extend(new_elements) # Extend the ID queue by the new elements
        self._queue_size += new_max - self._max_element # Ad the new elements to the size
        self._max_element = new_max # Set the new maximum