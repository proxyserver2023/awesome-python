Use Cases

1. User makes a read or write request
    1. Service does processing, stores user data, then returns the results
2. Service needs to evolve from serving a small amount of users to millions of users
    1. Discuss general scaling patterns as we evolve an architecture to handle a large number of users and requests
3. Service has high availability


State assumptions
Traffic is not evenly distributed
Need for relational data
Scale from 1 user to tens of millions of users
Denote increase of users as:
Users+
Users++
Users+++
...
10 million users
1 billion writes per month
100 billion reads per month
100:1 read to write ratio
1 KB content per write
