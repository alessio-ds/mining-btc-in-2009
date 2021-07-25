# Mining BTC in 2009
A Python program to mimick how much it take for your CPU to mine a Bitcoin block in 2009.

![](https://i.imgur.com/3RSA2cU.gif)
## Description
[As you might know, to mine BTC you will need to find a SHA256 hash **starting with 19 zeroes** to get 6.25BTC ($215k, July 2021)](https://www.blockchain.com/btc/block/0000000000000000000a21dd7eb71ed2f2c4a2818214357eb4948cb0ed317b19 "As you might know, to mine BTC you will need to find a SHA256 hash starting with 19 zeroes to get 6.25BTC ($215k, July 2021)")

[In 2009, **only 8 zeroes** were needed to mine a block and get 50BTC ($1.7m, July 2021)](https://www.blockchain.com/btc/block/000000005665d506f6c3ccb5fd98624f9816a8a169f1d2327d1d4d6d3262ad12)

**However, this doesn't mean it's easy**. 

This program is made to mimick how much it would take to mine a single block in 2009.

## How does it work?
To randomly generate SHA256 hashes, I decided to use this method:
1. Set a counter that starts from 0
2. I add this number to a random int going from 0 to 1 million
3. I take this sum and cipher it into an hex value
4. I finally encode this hex value into SHA256 using  **[hashlib](https://docs.python.org/3/library/hashlib.html "hashlib")**
5. If the hash doesn't have enough 0's, the counter will add 1 to itself and start all over again.
