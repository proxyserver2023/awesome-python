*Task Queue*:
1. offload long tasks to background workers
2. pattern used by almost all big companies
3. PaaS support: Heroku, AppEngine
4. Major Implementation:
    1. Geraman (Perl)
    2. Reque (Ruby)
    3. Celery (Python)

![Celery Design](https://image.slidesharecdn.com/parispy2-pricingassistant-celerytorq-130723022845-phpapp02/95/why-and-how-pricing-assistant-migrated-from-celery-to-rq-parispy-2-5-1024.jpg?cb=1479238863)


### Install
`pip install Celery`

### Broker
celery needs someone to send and receive messages, aka message broker
1. RabbitMQ - `sudo apt-get install rabbitmq-server`
2. Redis - `redis-rq`

### Easy Start
```python
from celery import Celery
celery = Celery(
    'tasks',
    broker='amqp://guest@localhost//'
)

@celery.task
def add(x,y):
    return x + y

from tasks import add 
add.delay(4,4)

```

![celery-is-fast](https://image.slidesharecdn.com/parispy2-pricingassistant-celerytorq-130723022845-phpapp02/95/why-and-how-pricing-assistant-migrated-from-celery-to-rq-parispy-2-8-1024.jpg?cb=1479238863)

![redis-rq vs celery](https://image.slidesharecdn.com/parispy2-pricingassistant-celerytorq-130723022845-phpapp02/95/why-and-how-pricing-assistant-migrated-from-celery-to-rq-parispy-2-21-1024.jpg?cb=1479238863)
