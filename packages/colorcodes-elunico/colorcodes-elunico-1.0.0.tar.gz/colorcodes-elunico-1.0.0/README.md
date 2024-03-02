# Color Codes

`colorcodes.py` is a module that helps you print color formatted text.

You can do this in many ways

## Inserting colors into strings

You can use string formatting and the `ColorCode` objects to print colored text

```python
from colorcodes import blue
print("Hello, {}world".format(blue))
```

This is good for simple, permanent color changes.

You can also combine these with the `+` operator

```python
from colorcodes import blue, bold, uline
print("Hello, {}world".format(blue + bold + uline))
```


If you do not need to intermingle color and style then you can use individual `ColorCode`s `print()` method

```python
import colorcodes

colorcodes.magenta.print("This text is all magenta")
```

These can also be combined using the `+` operator

```python
import colorcodes

(colorcodes.magenta + colorcodes.bold).print("This text is all magenta")
```

Finally, you can use the `cfs` (short for Color Format String) wrapper class to print colored values with format specifiers

```python
      #normal  #red  #mag #black
print("Welcome {:+r} {:m}{:k}".format(cfs('to the'), cfs('Jungle'), cfs('!')))
```
