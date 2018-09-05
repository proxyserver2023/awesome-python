```python
import logging
from examples.logging import Logger
a = Logger(
    name="MY_LOGGER_NAME",
    level=logging.DEBUG
)
a.debug("THIS is the message to be logged.")
```