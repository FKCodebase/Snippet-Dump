"""
@Author: Fabian Kolesch

UT FOR: id_generator.py

def stability(trials) -> bool:
    This test executes a fixed number 
    of valid random operations on
    the IDGenerator.
""" 
from generators.id_generator import IDGenerator
import sys
import random

SEED_SIZE = 2    # Initial size of the ID queue

def stability(trials) -> bool:
    """
    This method emulates #trials operations on the ID queue
    and checks the stability. The test checks whether the 
    the queued elements are monotonly increasing and
    each id is handed out exactly once.

    @param: (int) trials: The number of emulated operations
    """
    print("RUNNING TEST: ut_id_generator.stability, (Emulating %i ops)" %trials)

    id_gen = IDGenerator() # The tested instance
    active_ids = [] # Collection of currently used IDs

    def _test_monotony():
        """
        This method test if the elements in the queue are monotonly increasing
        """
        for i in range(len(id_gen._id_queue) - 1):
            assert id_gen._id_queue[i] < id_gen._id_queue[i + 1]

    def _test_get():
        """
        This method executes a "get_id" opetaration on the test instance
        and checks whether the id is currently used or not.
        """
        id = id_gen.get_id() # Get an ID from the IDGenerator
        assert id not in active_ids
        active_ids.append(id) # Add the id to the active ones
        _test_monotony()
        return True

    def _test_add():
        """
        This method exectues an "add_id" operation, adding a used or new ID to the the test instance and
        making it available (again).
        """
        if not active_ids: # If the is no active id to be used, use a new large one. (This is safe, because the id can not be in the queue)
            test_id = random.choice(list(range(id_gen._max_element + 1, id_gen._max_element + 100)))
        else:
            test_id = random.choice(active_ids)  # Choose an active id to add if possible
            active_ids.remove(test_id) # Remove it from the used ids

        id_gen.add_id(test_id) # Execute the "add_id" operation
        _test_monotony() # The monotone growth of queued elements
        return True


    def _test_remove():
        """
        This method executes a "remove_id" operation, removing a free ID from the test instance and
        adding it to the active IDs.
        """
        if not active_ids: # If there is no active if, select a large one (can not be in the queue)
            test_id = random.choice(list(range(id_gen._max_element + 1, id_gen._max_element + 101)))

        else: # If there are acitve IDs
            candidates = [i for i in range(max(active_ids)) if i not in active_ids] # Generate a list of all free IDs
            if not candidates:
                test_id = random.choice(list(range(id_gen._max_element + 1, id_gen._max_element + 100))) # If there are no free IDs, generate a new large one (can not be in the queue)
            else: 
                test_id = random.choice(candidates) # If there are free IDs, choose one

        id_gen.remove_id(test_id) # Execute the "remove_id" operation
        active_ids.append(test_id) # Add the removed ID to the active IDs
        _test_monotony() # The monotone growth of queued elements
        return True

    # Driver code
    operations = [_test_get, _test_add, _test_remove] # The list of emulated operations
    executed = 0 # Counter for executed ops

    while executed < trials: # Operation execution loop
        operation = random.choice(operations) # Choose an operation
        executed += operation() #  Execute
        
        if executed % (int(trials / 1000)) == 0: # Show progress
            sys.stdout.write("\r %s" % str(executed / int(trials / 100)) + "%")
            sys.stdout.flush()
