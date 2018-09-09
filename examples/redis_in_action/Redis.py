import redis


class Redis:
    def __init__(self, host='localhost', port=6379, db=0):
        self.conn = redis.StrictRedis(
            host=host,
            port=port,
            db=db
        )


if __name__ == "__main__":
    redis_instance = Redis()
    redis_instance.conn.set('foo', 'bar')
    print(f"{redis_instance.conn.get('foo')}")