# OUTAGE POSTMORTEM REPORT

### Summary

An outage occurred in our system as from **2305HRS EAT** to **0030HRS EAT** as aresult of a major influx of requests the server received, it was then duly concluded that this was an unforeseen case of scalability.
Users of our website experienced really slow loading times of webpages and finally default to an error pageage.
Complains obtained as a result of the slow loading times came from about a hundred individuals that total to about *65%* of our day to day users/visitors of the website.

### Timeline

* 2306HRS - A complain came in via email from an avid user of our web services

* 2309HRS - Investigation into what could have occurred is initiated with a select pool of probable mishaps owed to the description of the problem encountered as given by the user to avoid wandering needlessly.

* 2317HRS - This issue is escalated to the led DevOps Engineer on our team; He is brought onboard to help bring the system back to it's feet.

* 0029HRS - The issue causing the outage is fixed; The architecture of the webstack system is updated to ensure that dynamic scaling is properly implemented so that in scenarios where there is a hike in traffic, their is no throttle that would lead to an ultimate failure.

### Root Cause and Resolution Measures

**Suspected Cause**

The main cause for the outage that was experienced for close to an hour and a half was conclusively attributed to scalability issues, It was discovered that not enough measures had been put in place to cater for a surge in the number of requests our servers could get at particular instances.
It is worth noting that 6 hours before the complaint an online marketing/advertisement campaign had just been had been commenced and was ongoing. It is suspected that this could be the case and such a number had not been expected to make request or atleast overbear our systems hence cause a resource overload and finally cause the timely collapse.

**Resolution**

* Our lead DevOps engineer with assistance of the rest of the engineering department upgraded our webstack architecture system to include dynamic scaling abilities in that the system could intelligently distribute resources based on the patterns and number of requests in real -time to avoid another failure.

* We also optimized our system. Caching mechanisms, resource analyzation techniques and query optimizations were done to make the system more efficient.

### Corrective and Preventative measures

1. Obtain data based on history of the webstack operations and the monitoring tool to better create strategies to prevent a repeat disaster.

2. Ensuring that we implement auto-scaling systems that would easily allocate resources in realtime when needed.

3. Making sure that our monitoring tool works appropriately and if possible get an upgrade so that it is operating optimumly at all times.

4. Conduct mock tests on load management of our systems to see how best it can be tweaked to avoid errors that might come up.

5. Optimizing our systems to ensure thatit performs at peak; This will be done by conducting resource utilization analysis, doing query optimizations and also caching.
