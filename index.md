# Welcome to Py38-Swekil
Py38-Swekil is the Python version of the Swekil libraries.

The project is maintained by Kai Lyons.

## How it works
### Opening a Window
```py
import swekil
import os
index = os.path.abspath(os.path.join(os.path.dirname(__file__), "index.html"))
swekil.Window.openWindow(swekil.Window(), index, 600, 400, "My Window", [[]])
```

### The module system
Modules are a method of taking a class of functions and allowing to be used with the client-side JavaScript.
```py
import swekil
import os
from PyQt5.QtCore import *

class MyModule(QObject):
    def __init__(self, parent=None):
        super(MyModile, self).__init__(parent)
    @pyqtSlot(str)
    def myFunction(self, name):
        print("Hello,", name, "!")

module = MyModule()
mymodule = ['mod', module]

index = os.path.abspath(os.path.join(os.path.dirname(__file__), "index.html"))
swekil.Window.openWindow(swekil.Window(), index, 600, 400, "My Window", [mymodule])
```

In your JavaScript file, or `<script>` tag in your index file:
```js
function myFunction(name){
     mod.myFunction(name)
}
```

And can be called from your HTML
```html
<button onclick="myFunction('kai');">Print my name</button>
```
