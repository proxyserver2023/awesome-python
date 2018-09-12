## Study
1. Blocking Functions i.e. `Lock.acquire()`

## Examples

```python
"""
Thread Local data
"""

import threading

mydata = threading.local()
mydata.x = 1

```