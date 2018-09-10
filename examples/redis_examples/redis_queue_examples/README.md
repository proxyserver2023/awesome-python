## Processing Jobs the wrong way(crontab)
1. It loads your database
2. Almost impossible to scale.
3. Painful errors recovery.
4. Waste of time between each schedule.

## What is a task queue?
Task queue allows clients of some service asynchronously send tasks to it. Usually service has many clients and probably many workers. In short whole workflow looks like this:

Client puts task into a queue
Workers in loop periodically check the queue for a new task, if task exists then worker executes it

**Additional Requirements**:
- Quality of service: One client should not block other client’s requests
- Batch processing: clients and workers should have possibility to put and get several tasks at once for better performance.
- Reliability: if worker fails during processing of a task after some time this task have to be handed by other or the same worker again.
- Dead letters: if some task causes worker fail after several attempts to handle it then it have to be put into dead letters storage.
- One task have to be processed only one time in case of success.

```python
import json
import datetime
import pytz
from random import randint
import logging
import time

main_prefix = "bqueues:"



```

## Appendix
1. [Building Scalable, Distributed Job Queues](https://www.slideshare.net/francescolaurita/italians-coderjune13redisqueue)
2. [Simple Messae Queue](https://medium.com/@weyoss/building-a-simple-message-queue-using-redis-server-and-node-js-964eda240a2a)