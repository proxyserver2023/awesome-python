# System Design

## Approach A Problem
### Outline
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

### Scaling
1. Load Balancer
2. Horizontal Scaling
3. Caching
4. Database Sharding

## Powers of Two Table

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

## Latency Numbers every programmers should Know
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

## Example - Generate Image results Page of 30 Thumbnails
### Design 1 - Serial
1. Read images serially. Do a disk seek. Read a 256K image and then go on to the next image.
2. **Performance**: `30 seeks * 10ms/seek + (30*256K)/(30MB/s)` = `560ms`

### Design 2 - Parallel
1. Issue reads in parallel.
2. **Performance**: `10ms/seek + 256K read/30MB/s` = 18ms
3. There will be variance from the disk reads. so with system loss `30-60ms`.

### Considerations
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

## Practicing Steps for desiging a system
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