# hyphenfrac
Uses a hyphen-minus character to visualize a fraction.
## Usage
Displaying a fraction
```python
>>> import hyphenfrac, random
>>> hyphenfrac.display(random.randint(1, 100)/random.randint(1, 100))
20
-- + 1
49
>>>
```
You may also assign this value to a variable
```python
>>> import hyphenfrac
>>> foo = hyphenfrac.make_pretty(1, 10)
>>> print(foo)
1
--
10
>>>
```
