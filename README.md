<h1> Snippet-Dump </h1>
<p>
This Repo contains a collection of cool algorithm and data structure implementations. 
</p>

<h2>Content:</h1> 

[Generators](#generators)
<ul>
<li>

[IDGenerator](#id-generator) 

</li>
</ul>

## Generators
This section contains documentation and examples for the generator snippets

### ID Generator
```diff
+ generators.IDGenerator
```

<p>
The ID generator class implements the genratation of minimal integer 
identifiers for not security relevant code.
</p>

#### Examples:
Example 1: Creating 'per class' instance identifiers.
```python
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
```

Example 2: Creating a global instance identifier.
```python
ID_GENERATOR = generators.IDGenerator()

class GlobalIdentifiedObject:
    def __init__(self) -> None:
        self._id = ID_GENERATOR.get_id()

    def __del__(self) -> None:
        ID_GENERATOR.add_id(self._id)


class GlobalIDGenSampleC1(GlobalIdentifiedObject):
    # DoStuff
```

