import generators


#--- [ID Generator] ---
# - Class level id generation - #
# Uncomment the following section to run the class level identification example.

# The classes IDGenSampleC1 and IDGenSampleC2 define an ID generator on class level.
# On instantiation, a new identifier is generated (__init__). When the instance
# is deleted (__del__), the identifier is returned to the generator.
# Thus, each instance of these classes will have a unique identifier.
# However, some instances of IDGenSampleC1 may have the same identifier as some instance
# of IDGenSampleC2.

"""
class IDGenSampleC1:
    id_gen = generators.IDGenerator()

    def __init__(self) -> None:
        self._id = IDGenSampleC1.id_gen.get_id()

    def __del__(self) -> None:
        IDGenSampleC1.id_gen.add_id(self._id)

class IDGenSampleC2():
    id_gen = generators.IDGenerator()

    def __init__(self) -> None:
        self._id = IDGenSampleC2.id_gen.get_id()

    def __del__(self) -> None:
        IDGenSampleC2.id_gen.add_id(self._id)

# Uncomment to run class level sample
i_1, i_2, i_3 = IDGenSampleC1(), IDGenSampleC1(), IDGenSampleC2()
print(f"Instance 1 has class: {i_1.__class__} And ID: {i_1._id}")
print(f"Instance 2 has class: {i_2.__class__} And ID: {i_2._id}")
print(f"Instance 3 has class: {i_3.__class__} And ID: {i_3._id}")
"""

# - Global id generation - #
# Uncomment the following section to run the global level identification example.

# The 'GlobalIdentifiedObject' class holds an instance of the IDGenerator as a class variable.
# On instantiation, a new identifier is generated (__init__). When the instance
# is deleted (__del__), the identifier is returned to the generator.
#   
# The classes IDGenSampleC1 and IDGenSampleC2 inherit from 'IdentifiedObject.
# Thus, each instance of these classes will have a unique identifier on a class level.
# However, some instances of IDGenSampleC1 may have the same identifier as some instance
# of IDGenSampleC2.

"""
ID_GENERATOR = generators.IDGenerator()

class GlobalIdentifiedObject:
    def __init__(self) -> None:
        self._id = ID_GENERATOR.get_id()

    def __del__(self) -> None:
        ID_GENERATOR.add_id(self._id)


class GlobalIDGenSampleC1(GlobalIdentifiedObject):
    pass

class GlobalIDGenSampleC2(GlobalIdentifiedObject):
    pass

i_1, i_2, i_3 = GlobalIDGenSampleC1(), GlobalIDGenSampleC1(), GlobalIDGenSampleC2()
print(f"Instance 1 has class: {i_1.__class__} And ID: {i_1._id}")
print(f"Instance 2 has class: {i_2.__class__} And ID: {i_2._id}")
print(f"Instance 3 has class: {i_3.__class__} And ID: {i_3._id}")
"""