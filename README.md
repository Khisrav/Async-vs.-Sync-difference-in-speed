
# Async vs. Sync - Difference in speed

I was bored then I decided to compare synchronous and asynchronous programming using Python and some libraries like ``asyncio`` and ``aiohttp``




## Deployment

To deploy this project you need Python installed with its package manager `pip`

#### Open command line in project folder and run following command:
```bash
  pip install -r requirements.txt
```

## Usage/Examples
#### Sample output for `sync_main.py`:
```bash
  Downloading pic 1
  Downloading pic 2
  ...
  Downloading pic 11
  Downloading pic 12
  Time: 5.90338134765625
```

#### Sample output for `async_main.py`:
```bash
  Downloading pic onepunch_man_202_7.jpg
  Downloading pic onepunch_man_202_4.jpg
  ...
  Downloading pic onepunch_man_202_5.jpg
  Downloading pic onepunch_man_202_9.jpg
  Time: 1.8927528858184814
```

## Difference
Synchronous | Asynchronous
-- | --
9,71s | 2,59s
9,17s | 2,54s
9,17s | 2,24s
8,25s | 2,06s
6,41s | 2,3s
6,00s | 4,4s
6,12s | 2,11s
*Avg: **7,83s*** | *Avg: **2,61s***

Difference will grow exponentially as amount of data grows

