# Redis In Action

## Install redis and python

```bash
wget http://download.redis.io/redis-stable.tar.gz
tar xvzf redis-stable.tar.gz
cd redis-stable
make
sudo make install
```

Start Redis-Server
```bash
redis-server
```

Check if Redis is working
```bash
$ redis-cli ping
PONG
```

```bash
$ redis-cli
redis 127.0.0.1:6379> ping
PONG
redis 127.0.0.1:6379> set mykey somevalue
OK
redis 127.0.0.1:6379> get mykey 
"somevalue"
```

Install Redis client
```bash
pip install redis hiredis
```

### Components of Redis
1. `redis-server` is the Redis Server itself.
2. `redis-sentinel` is the Redis Sentinel executable (monitoring and failover).
3. `redis-cli` is the command line interface utility to talk with Redis.
4. `redis-benchmark` is used to check Redis performances.
5. `redis-check-aof` and redis-check-dump are useful in the rare event of corrupted data files.

## Data Structures
1. STRING - Binary safe strings
2. LIST - Collection of string elements sorted according to the orderof insertion. They are basically linked lists.
3. SET  - Unordered collection of unique strings
4. HASH - Unordered Hash table of keys=>values, keys and values are strings. similar to python/ruby.
5. ZSET - Sorted Sets.
    Every String element is associated to a floating number value, called score. The elements are always taken sorted by their score, so unlike Sets it is possible to retrieve a range of elements (for example you may ask: give me the top 10, or the bottom 10).
6. Bit arrays (or simply bitmaps): it is possible, using special commands, to handle String values like an array of bits: you can set and clear individual bits, count all the bits set to 1, find the first set or unset bit, and so forth.
7. HyperLogLogs: this is a probabilistic data structure which is used in order to estimate the cardinality of a set. Don't be scared, it is simpler than it seems... See later in the HyperLogLog section of this tutorial.
   
### Redis Keys
Redis keys are binary safe. MAX Size <= 512MB
```bash
key := strings | JPEG binary Data | ""
```

### Redis Values
value <= 512MB

### Redis Strings
```bash
> set mykey somevalue
OK
> get mykey
"somevalue"
```

```
> set mykey newval nx
(nil)
> set mykey newval xx
OK
```

```bash
> set counter 100
OK
> incr counter
(integer) 101
> incr counter
(integer) 102
> incrby counter 50
(integer) 152
```

The ability to set or retrieve the value of multiple keys in a single command is also useful for reduced latency. For this reason there are the MSET and MGET commands:
```bash
> mset a 10 b 20 c 30
OK
> mget a b c
1) "10"
2) "20"
3) "30"
```
When MGET is used, Redis returns an array of values.

**Altering and querying the key space**:
For example the EXISTS command returns 1 or 0 to signal if a given key exists or not in the database, while the DEL command deletes a key and associated value, whatever the value is.

```bash
> set mykey hello
OK
> exists mykey
(integer) 1
> del mykey
(integer) 1
> exists mykey
(integer) 0
```

```bash
> set mykey x
OK
> type mykey
string
> del mykey
(integer) 1
> type mykey
none
```

**Expiration**
```bash
> set key some-value
OK
> expire key 5
(integer) 1
> get key (immediately)
"some-value"
> get key (after some time)
(nil)
```

Create key and set expire time
```
> set key 100 ex 10
OK
> ttl key
(integer) 9
```

### Redis Lists
Redis lists are implemented via Linked Lists. This means that even if you have millions of elements inside a list, the operation of adding a new element in the head or in the tail of the list is performed in constant time. The speed of adding a new element with the LPUSH command to the head of a list with ten elements is the same as adding an element to the head of list with 10 million elements.

```bash
> rpush mylist A
(integer) 1
> rpush mylist B
(integer) 2
> lpush mylist first
(integer) 3
> lrange mylist 0 -1
1) "first"
2) "A"
3) "B"
```

```bash
> rpush mylist 1 2 3 4 5 "foo bar"
(integer) 9
> lrange mylist 0 -1
1) "first"
2) "A"
3) "B"
4) "1"
5) "2"
6) "3"
7) "4"
8) "5"
9) "foo bar"
```

```bash
> rpush mylist a b c
(integer) 3
> rpop mylist
"c"
> rpop mylist
"b"
> rpop mylist
"a"
```

```bash
> rpop mylist
(nil)

```

**Common use cases for lists**
1. latest updates posted by users into a social network
2. communication between processes, using a consumer-producer pattern where the producer pushes items into a list, and a consumer (usually a worker) consumes those items and executed actions. Redis has special list commands to make this use case both more reliabale and efficient.

Imagine your home page shows the latest photos published in a photo sharing social network and you want to speedup access.
1. Every time a user posts a new photo, we add its ID into a list with LPUSH.
2. When users visit the home page, we use LRANGE 0 9 in order to get the latest 10 posted items.

#### Capped List
Redis allows us to use lists as a capped collection, only remembering the latest N items and discarding all the oldest items using the LTRIM command

The LTRIM command is similar to LRANGE, but instead of displaying the specified range of elements it sets this range as the new list value. All the elements outside the given range are removed.

An example will make it more clear:
```bash
> rpush mylist 1 2 3 4 5
(integer) 5
> ltrim mylist 0 2
OK
> lrange mylist 0 -1
1) "1"
2) "2"
3) "3"

```
#### Blocking operations on lists

However it is possible that sometimes the list is empty and there is nothing to process, so RPOP just returns NULL. In this case a consumer is forced to wait some time and retry again with RPOP. This is called polling, and is not a good idea in this context because it has several drawbacks:

```bash
> brpop tasks 5
1) "tasks"
2) "do_something"

```
It means "wait for elements in the list tasks, but return if after 5 seconds no element is available."

### Redis Hash
```bash
> hmset user:1000 username antirez birthyear 1977 verified 1
OK
> hget user:1000 username
"antirez"
> hget user:1000 birthyear
"1977"
> hgetall user:1000
1) "username"
2) "antirez"
3) "birthyear"
4) "1977"
5) "verified"
6) "1"
```

### Redis Sets

```bash
> sadd myset 1 2 3
(integer) 3
> smembers myset
1. 3
2. 1
3. 2

> sismember myset 3
(integer) 1
> sismember myset 30
(integer) 0

> sadd news:1000:tags 1 2 5 77
(integer) 4
```
