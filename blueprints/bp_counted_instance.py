"""
This file implements a simple instance counter.
On construction, the instance counter is incremented.
On destruction, the instance counter is decremented.
"""


class BP_counted_instance:
    """
    Implementation of the instance_count blueprint.
    """
    # The instance counting variable
    _instance_count = 0
    
    @classmethod
    def has_instance(cls) -> bool:
        """
        Check whether an instance exists or not.
        @param: class: This class. 
        @return: bool: True, if an instance exists.
        """
        return cls._instance_count != 0
    
    @classmethod
    def get_instance_count(cls) -> int:
        """
        Get the number of instances.
        @param: class: The counted class
        @return: int: The number of instances
        """
        return cls._instance_count

    def __init__(self):
        """
        Constructor
        Increment the instance counter
        """
        self.__class__._instance_count += 1
        
    def __del__(self):
        """
        Destrucor:
        Decrement the instance counter
        """
        self.__class__._instance_count -= 1
