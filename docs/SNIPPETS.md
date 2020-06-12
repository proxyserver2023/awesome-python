## Snippets

- generate token

```python
import hashlib
from datetime import datetime

def generate_token():
    return hashlib.md5(
        datetime.now()
                .strftime('%Y-%m-%dT%H:%M:%S')
                .encode('utf-8')
    ).hexdigest()
```