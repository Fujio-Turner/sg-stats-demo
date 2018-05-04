# sg-stats-demo

This script pulls stats from SG Admin port localhost:4985/_expvar,in real time, and puts them into a basic graph in the browser.

#http://localhost:8000

<img src="img/sg-stats-demo1.png" width="75%">

**HOW TO USE**

-Just run the pythen script and tell it where the sync_gateway_error.log is
```
#/path/to/ ./sg-stats-demo.py
```

**Stats/Data**
Currently the browser only shows data for:

Revision Cache Misses vs Revision Cache Hits - Total number of times a revision-cache lookup failed vs Total number of times a revision-cache lookup succeeded (as a percentage).

Active _changes Feeds - Current number of active _changes feeds.

Max Pending - Total max number of sequences waiting on a missing earlier sequence number

Out Of Order - Total number of out-of-order sequences posted

View Queries - Total number of view queries to channels view 


**_expvar**

Here is a link about whats in the _expvar https://developer.couchbase.com/documentation/mobile/2.0/references/sync-gateway/admin-rest-api/index.html#/server/get__expvar


**Compatibility**

Works with SG 2.x and lower.


**REQUIREMENTS**

PYTHON 2.7+

Web Browser
