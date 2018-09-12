# System Design

## Approach A Problem
### Outline - Use Cases, Constraints and Assumptions
1. Who is going to use it?
2. How are they going to use it?
3. How many users?
4. What does the system do?
5. What are the inputs and outputs?
6. How much data are expected to handle?
7. How many requests per second do we expect?
8. What is the expected Read to Write Ratio?

### High level Design
Draw it... Justify ideas

### Design core components
**Example**: Design an URL Shortening Service
1. Generating and storing a hash of the full URL
    1. MD5 and Base62
    2. Hash Collisions
    3. SQL or NoSQL
    4. Database Schema
2. Translating a hashed url to the full URL
    1. Database Lookup
3. API and object-oriented design

### Scaling The Design
1. Load Balancer
2. Horizontal Scaling
3. Caching
4. Database Sharding


### Example - Generate Image results Page of 30 Thumbnails
#### Design 1 - Serial
1. Read images serially. Do a disk seek. Read a 256K image and then go on to the next image.
2. **Performance**: `30 seeks * 10ms/seek + (30*256K)/(30MB/s)` = `560ms`

#### Design 2 - Parallel
1. Issue reads in parallel.
2. **Performance**: `10ms/seek + 256K read/30MB/s` = 18ms
3. There will be variance from the disk reads. so with system loss `30-60ms`.

#### Considerations
1. Does it make sense to cache single thumbnail images?
2. Should you cache a whole set of images in one entry?
3. Does it make sense to precompute the thumbnails?

To know if caching is a good design alternative, for example, you'll have to know how long it takes to write into your cache.

## Concepts for System Design Knowledge
1. **Concurrency**: Threads, Deadlock, starvation. Parallelize Algorithms? Consistency and Coherence.
2. **Networking**: IPC and TCP/IP? throughput vs. latency and when each is the relevant factor?
3. **Abstraction**: How an OS, file system and database work? Various Level of Caching in Modern OS?
4. **Real-World Performance**: speed of everything your computer can do, relative performance of RAM, disk, SSD and your Network.
5. **Estimation**: back-of-the-envelope calculation
6. **Availability and Reliability**: How things can fail in a distributed environment? How to design a system to cope with network failures? Do you understand `durability`.

## Practicing Steps for designing a system
1. Do mock design sessions
2. work on an actual system.
3. Do back-of-the-envelope calcualation and micro-benchmark them.
4. Dig into the performance characterstics of an open source system.
5. Learn how databases and OS work.

## Fallacies of the Distributed Systems
1. The network is reliable.
2. Latency is zero.
3. Bandwidth is infinite.
4. The network is secure.
5. Topology doesn't change.
6. There is one administrator.
7. Transport cost is zero.
8. The network is homogeneous.

## Domain Name System
![DNS](https://camo.githubusercontent.com/fae27d1291ed38dd120595d692eacd2505cd3a9c/687474703a2f2f692e696d6775722e636f6d2f494f794c6a34692e6a7067)

## Content Delivery Network
![CDN](https://camo.githubusercontent.com/853a8603651149c686bf3c504769fc594ff08849/687474703a2f2f692e696d6775722e636f6d2f683954417547492e6a7067)
1. Push CDNs
2. Pull CDNs

## Load Balancer
![Load Balancer Elephant](https://varchitectthoughts.files.wordpress.com/2016/07/gop_balancing_act23.jpg)

![Load Balancer](https://camo.githubusercontent.com/21caea3d7f67f451630012f657ae59a56709365c/687474703a2f2f692e696d6775722e636f6d2f6838316e39694b2e706e67)

Load Balancers are effective at:
1. Preventing requests from going to unhealthy servers.
2. Preventing overloading resources.
3. Helping eliminate single points of failure.

Can be implemented with Hardware[Expensive] or with software such as HAProxy.

Additional Benefits:
1. **SSL Termination**: Decrypt incoming requests and encrypt server responses so backend servers do not have to perform these potentially expensive operations.
    1. Removes the need to install X.509 certificates on each server.
2. **Session Persistence**: Issue cookies and route a specific client's requests to same instance if the web apps do not keep track of sessions.

**Multiple Load Balancers**: Active-passive, active-active

### Horizontal Scaling
**Disadvantages**:
1. Sessions can be stored in a centralized data store such as database(SQL, NoSQL) or a persistent cache(Redis, Memcached)
2. **Downstream** servers such as caches and databases need to handle more simultaneous connections as upstream servers scale out

## Reverse Proxy (Web Server)
![Reverse Proxy](https://camo.githubusercontent.com/e88216d0999853426f72b28e41223f43977d22b7/687474703a2f2f692e696d6775722e636f6d2f6e3431417a66662e706e67)

**Benefits**:
1. Hide information about backend servers, blacklist IPs, limit number of connections per client
2. Clients only see the reverse proxy's IP, allowing you to scale servers or change their configuration
3. Decrypt incoming requests and encrypt server responses so backend servers do not have to perform these potentially expensive operations
    1. Removes the need to install X.509 certificates on each server
4. **Compress** Server Responses
5. Return the response for cached requests
6. Serve static content directly
    - HTML/CSS/JS
    - Photos
    - Videos
    - etc.

### Load Balancers Vs Reverse Proxy
1. Use Load Balance to balance requests between multiple servers
2. Use Reverse Proxy to Abstract the Implementation from Definition. It works like the public face of the website.

## Database
![Scaling up to your first 10 million users](https://camo.githubusercontent.com/15a7553727e6da98d0de5e9ca3792f6d2b5e92d4/687474703a2f2f692e696d6775722e636f6d2f586b6d3543587a2e706e67)

ACID - Atomicity, Consistency, Isolation, Durability.

### Master-Slave Replication
The master serves reads and writes, replicating writes to one or more slaves, which serve only reads. Slaves can also replicate to additional slaves in a tree-like fashion. If the master goes offline, the system can continue to operate in read-only mode until a slave is promoted to a master or a new master is provisioned.

![Master Slave Database](https://camo.githubusercontent.com/6a097809b9690236258747d969b1d3e0d93bb8ca/687474703a2f2f692e696d6775722e636f6d2f4339696f47746e2e706e67)
![Master Slave Database](https://camo.githubusercontent.com/6a097809b9690236258747d969b1d3e0d93bb8ca/687474703a2f2f692e696d6775722e636f6d2f4339696f47746e2e706e67)

### Master-Master Replication
![Master Master Replication](https://camo.githubusercontent.com/5862604b102ee97d85f86f89edda44bde85a5b7f/687474703a2f2f692e696d6775722e636f6d2f6b7241484c47672e706e67)

**Disadvantages**:
1. You'll need a load balancer or you'll need to make changes to your application logic to determine where to write.
2. Most master-master systems are either loosely consistent (violating ACID) or have increased write latency due to synchronization.
3. Conflict resolution comes more into play as more write nodes are added and as latency increases.

**Disadvantages**: Replication
1. There is a potential for loss of data if the master fails before any newly written data can be replicated to other nodes.
2. Writes are replayed to the read replicas. If there are a lot of writes, the read replicas can get bogged down with replaying writes and can't do as many reads.
3. The more read slaves, the more you have to replicate, which leads to greater replication lag.
4. On some systems, writing to the master can spawn multiple threads to write in parallel, whereas read replicas only support writing sequentially with a single thread.
5. Replication adds more hardware and additional complexity.

### Federation
// TODO
### Sharding
### Denormalization
### SQL Tuning

## Caching
### Memcached
1. very fast
2. simple
3. key-value (string->binary)
4. Clients for most languages
5. distributed
6. not replicated - so 1/N chance for local access in cluster.

## Scalability
![Managing Overload](https://upload.wikimedia.org/wikipedia/en/3/31/Don%27t-overload-your-trailer.jpg)

**General Recommendations**:
1. Immutability as the default
2. Referential Transparency (FP)
3. Laziness
4. Think about your data.
    1. Different data need different gurantees.
    
**Scalability Tradeoffs**:
![There is no free lunch](http://eddecosta.com/wp-content/uploads/2012/06/no-free-lunch.jpg)

**Tradeoffs**
1. Performance vs Scalability
2. Latency vs Throughput
3. Avaialability vs Consistency

### Performancs vs Scalability
1. If you have a performance problem, **your system is slow for a single user**.
2. If you have a scalability problem, **your system is fast for a single user but slow under heavy load**.

### Latency vs throughput
1. **Latency**: time/(per operation).
2. **Throughput**: (No of operations)/(per unit time).

**Maximum Throughput** with **Acceptable Latency**.

### Availability vs Consistency
**Brewer's CAP Theorem**:
![CAP Theorem](https://i.imgur.com/JcTQBmP.png)
![Centralized System](https://i.imgur.com/NB9IcWr.png)
![Distributed System](https://i.imgur.com/kK0dKH3.png)

**Availability Patterns**:
1. Fail-Over
2. Replication
    1. Master-Slave
    2. Tree Replication
    3. Master-Master
    4. Buddy Replication
    ![Buddy Replication](https://image.slidesharecdn.com/scalabilitypatterns20100510-100512004526-phpapp02/95/scalability-availability-stability-patterns-48-638.jpg?cb=1369533910)
    ![Buddy Replication](http://www.mastertheboss.com/images/stories/jboss/4026_07_15.png)
    
    
**Scalability Patterns**: State
1. Partitioning
2. HTTP Caching
    Reverse Proxy
    1. Varnish
    2. Squid
    3. rack-cache
    4. Pound
    5. Nginx
    6. Apache mod_proxy
    7. Traffic server
    
    Generate Static Content
    Precompute content
    1. Homegrown + cron or Quartz
    2. Spring Batch
    3. Gearman
    4. Hadoop
    5. Google Data Protocol
    6. Amazon Elastic MapReduce
3. RDBMS Sharding
4. NoSQL - Not only SQL
    1. Key-value databases
    2. Column Databases
    3. Document Databases
    4. Graph Databases
    5. Data Structure Databases.
5. Distributed Caching
6. Data Grids
7. Concurrency

**When is a RDBMS not good enough?**
Scaling reads to a RDBMS is hard.
Scaling writes to a RDBMS is impossible.

**Who's ACID?**
1. Relational DB (MySQL, Oracle, Postgres)
2. Object DBs (Gemstone, db40)
3. Clustering Products(Coherence, Teracotta)
4. Most Caching Products(ehcache)

**Who's BASE?**
Distributed databases
1. Cassandra
2. Riak
3. Voldemort
4. Dynomite
5. SimpleDB

**NoSQL in the wild**
1. Google: Bigtable
2. Amazon: Dynamo
3. Amazon: SimpleDB
4. Yahoo: HBase
5. Facebook: Cassandra
6. LinkedIn: Voldemort

**Types of NoSQL Stores**
1. Key-value (voldemort, dynomite)
2. Column (Cassandra, Vertica, Sybase IQ)
3. Document (MongoDB, CouchDB)
4. Graph (Neo4j AllegroGraph)
5. Datastructure (Redis, Hazelcast)

**Distributed Caching**
1. write-through
    ![write-through](https://i.imgur.com/His4l5H.png)
2. write-behind
    ![write-behind](https://i.imgur.com/6LRpVAi.png)
3. eviction policies
    1. TTL
    2. Bounded FIFO
    3. Boudned LIFO
    4. Explicit Cache Invalidation
4. replication
5. peer-to-peer(P2P)

### Concurrency
1. Shared-state concurrency
2. Message-passing concurrency
3. Dataflow concurrency
4. software transactional memory

### Clones
- every server contains exactly the same codebase and does not store any user related data, like sessions or profile pictures, on local disc or memory.
- Sessions need to be stored in a centralized data store which is accessible to all your application servers. It can be external database or external persistent cache like Redis.
- performance(external_persistent_cache) > performance(external_database)
- data store does not reside on the application servers.

### Database
1. Path #1: Scaling Database (i.e. MySQL) `master-slave replication` read from slaves and write into master. and upgrade your master by adding RAM, RAM and more RAM. Sharding, denormalization and SQL tuning.

2. Path #2:
    1. Denormalize from the beginning and include no more Joins in any DB Query. You can stay with mysql and use it like a NoSQL DB. or you can switch to a better and easier to scale NoSQL DB like MongoDB or CouchDB. 
    2. Joins will now need to be done in your application code. 
    3. Although you introduce NoSQL, it will be slower unless you use cache.

### Cache
Cache means `memory based caching`, never `file-based-caching`. it makes auto-scaling and cloning your servers just a pain.

2 Patterns of caching your data. An old one and a new one.
1. Cached Databasae Queries
    1. Whenever you do a query to your database, you store the result dataset in cache
    2. A `hashed version` of your query is the cache key.
    3. The main issue is expiration.
2. Cached Objects
    1. asynchronous processing possible! just imagine an army of worker servers who assemble your objects for you! The Application just consumes the latest cached object and nearly never touches the database anymore.
    
    Some ideas of objects to cache.
    1. user sessions
    2. fully rendered blog articles.
    3. user<->friend relationsips.
    4. activity streams.
    
    Redis is best for extra database-features like persistence and built-in data structures, like sets and lists.
    
    if you just need to cache. take Memcached, because it scales like a charm.

### Asynchronism
1. **Async #1**:
    "bake the breads at night and sell them in the morning".
    Doing time consuming work in advance and serving the finished work with a low request time.
    1. Very often this paradigm is used to turn dynamic content into static content.  Pages of a website, maybe built with a massive framework or CMS, are pre-rendered and locally stored as static HTML files on every change.
    2. Often these computing tasks are done on a regular basis, maybe by a script which is called every hour by a cronjob. This pre-computing of overall general data can extremely improve websites and web apps and makes them very scalable and performant.
    
    3. Just imagine the scalability of your website if the script would upload these pre-rendered HTML pages to AWS S3 or Cloudfront or another Content Delivery Network! Your website would be super responsive and could handle millions of visitors per hour!
2. **Asyn #2**:
    sometimes customers has special requests like a birthday cake with “Happy Birthday, Steve!” on it. The bakery can not foresee these kind of customer wishes, so it must start the task when the customer is in the bakery and tell him to come back at the next day.
    
    Workflow:
    1. User comes to website ->
    2. Starts very computing intensive task which would take several minutes to finish. ->
    3. so the frontend sends a job onto a job queue ->
    4. and immediately signals back to the user: your job is in work and please continue to browse.
    5. The job queue is constantly checked by a bunch of workers for new jobs
    6.  If there is a new job then the worker does the job and after some minutes sends a signal that the job was done.
    7. The frontend, which constantly checks for new “job is done” - signals, sees that the job was done and informs the user about it.
   
   If you do something time-consuming, try to do it always asynchronously. 
   

## Appendix
### Powers of Two Table

```
Power           Exact   Value           Approx Value        Bytes
-----------------------------------------------------------------
7               128                                  
8               256
10              1024                    1K                  1KB
16              65,536                                      64KB
20              1,048,576               1M                  1MB
30              1,073,741,824           1B                  1GB
32              4,294,967,296                               4GB
40              1,099,511,627,776       1T                  1TB
```

### Latency Numbers every programmers should Know
```
Latency Comparison Numbers
----------------------------
L1 Cache Reference                                  0.5ns
Branch Mispredict                                   5.0ns               10      * L1 Cache
L2 Cache Reference                                  7.0ns               14      * L1 Cache
Mutex Lock/Unlock                                 100.0ns               200     * L1 Cache
Main Memory Reference                             100.0ns               200     * L1 Cache, 20  * L2 Cache
Compress 1KB Bytes with Zippy                  10,000.0ns               
Send 1KB [~10K bits] Over 1Gbps Network        10,000.0ns
Read 4KB [~40K bits] randomly from SSD        150,000.0ns               ~1GB/sec SSD    
Read 1MB sequentially from Memory             250,000.0ns          
Round trip within same datacenter             500,000.0ns
Read 1MB sequentially from SSD*             1,000,000.0ns >>   1ms   ~1GB/sec SSD, 4X Memory
Disk Seek                                  10,000,000.0ns >>  10ms
Read 1MB sequentially from 1Gbps           10,000,000.0ns >>  10ms      40X Memory, 10X SSD
Read 1MB sequentially from disk            30,000,000.0ns >>  30ms     120X Memory, 30X SSD
Send packet CA->Netherlands->CA           150,000,000.0ns >> 150ms
```

```
System Call Overhead                          400ns
Context Switch between process              3,000ns
fork() (statically-linked binary)          70,000ns
fork() (dynamically-linked binary)        160,000ns
```
Handy Metrics based on numbers above:
1. Read sequentially from disk at 30MB/s
2. Read sequentially from 1Gbps Ethernet at 100MB/s
3. Read sequentially from Main Memory at 4GB/s
4. 6-7 world-wide round trips per second
5. 2000 round trips per second within a data-center

Some things to notice:
1. datacenters are far away so it takes a long time to send anything between them.
2. Memory is fast and disks are slow.
3. By using a cheap compression algorithm a lot (by a factor of 2) of network bandwidth can be saved.
4. Writes are 40 times more expensive than reads.
5. Global shared data is expensive. This is a fundamental limitation of distributed systems. The lock contention in shared heavily written objects kills performance as transactions become serialized and slow.
6. Architect for scaling writes.
7. Optimize for low write contention.
8. Optimize wide. Make writes as parallel as you can.

**Writes are Expensive**
1. Datastore is transactional: writes require disk access
2. Disk access means disk seeks
3. Rule of thumb: 10ms for a disk seek
4. Simple math: 1s / 10ms = 100 seeks/sec maximum
5. Depends on:
    * The size and shape of your data
    * Doing work in batches (batch puts and gets)

**Reads Are Cheap!**
1. Reads do not need to be transactional, just consistent
2. Data is read from disk once, then it's easily cached
3. All subsequent reads come straight from memory
4. Rule of thumb: 250usec for 1MB of data from memory
5. Simple math: 1s / 250usec = 4GB/sec maximum
    * For a 1MB entity, that's 4000 fetches/sec

**Visualizations**:
![Latency Numbers Every Programmer Should Know](https://camo.githubusercontent.com/77f72259e1eb58596b564d1ad823af1853bc60a3/687474703a2f2f692e696d6775722e636f6d2f6b307431652e706e67)

### Requests wrt Time Table

1. 86400 seconds per day ~ 87K
2. 86400 * 7 seconds per week ~ .6M
3. 86400 * 30 seconds per month ~ 2.5M+

1 Requests per second      => 2.5M Requests per month
40 Requests per second [R] => 2.5*40 = 100M Requests per month
400 Requests per second [W]=> 1000M or 1B requests per month.

## Topics I Need to clear
1. Cryptography
2. Database
3. Remote Procedure Calls
4. Service Analytics - MapReduce
