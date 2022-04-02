# py38-swekil
Swekil - Simple webkit library for Python 3.8

## Example:
```py
import swekil
import os

index = os.path.abspath(os.path.join(os.path.dirname(__file__), "index.html"))
swekil.Window.openWindow(swekil.Window(), index, 600, 400, "My Window", [[]])
```

## The Goal: 
To make the creation of webkit windows easy and simple to do in Python. While
a replacement to ElectronJS, this was just a quick hobby project.

## Dependencies:
Install your distribution's PyQt5 library tools.