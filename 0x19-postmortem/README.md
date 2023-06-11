# OUTAGE POSTMORTEM REPORT

### Summary
An outage occurred in our system as from **2305HRS EAT** to **0030HRS EAT** as aresult of a major influx of requests the server received, it was then duly concluded that this was an unforeseen case of scalability.
Users of our website experienced really slow loading times of webpages and finally default to an error pageage.
Complains obtained as a result of the slow loading times came from about a hundred individuals that total to about *65%* of our day to day users/visitors of the website.

### Timeline
* 2306HRS - A complain came in via email from an avid user of our web services

* 2309HRS - Investigation into what could have occurred is initiated with a select pool of probable mishaps owed to the description of the problem encountered as given by the user to avoid wandering needlessly.

* 2317HRS - This issue is escalatedand other engineers are brought onboard to bring the system back to it's feet.

* 0029HRS - The issue causing the outage is fixed; The architecture of the webstack system is updated to ensure that dynamic scaling is properly implemented so that in scenarios where ther is a hike in traffic, their is no throttle that would lead to an ultimate failure.


