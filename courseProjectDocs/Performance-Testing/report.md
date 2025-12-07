# Performance Testing

## LOAD TEST
### Test Scope
Tested the /profile endpoint of a Flask app running pyinstrument profiler under moderate load. Simulated users requesting profiles. Tool used Locust 2.42.6

### Configuration
10 concurrent users, ramp up 2 users/second, 30 seconds duration. Constant load pattern

### Results
- 1195 requests completed (0% failures) 
- Throughput: 39.45 requests/second 
- Response time: median 13 ms 
- CPU usage: 60 - 80%

### Performance Findings
- pyinstrument handles 40 profiles/second with stable low latency
- No errors or throughput drops observed
- Latency stable under tested load

## STRESS TEST
### Test Scope
### Configuration
### Results
### Performance Findings

## SPIKE TEST
### Test Scope
### Configuration
### Results
### Performance Findings

## Group Contributions
- Jose: Did tool setup, perform load test and recollect the information from the results
- Ursula:
- Michael: