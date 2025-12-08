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
The goal of this stress test was to evaluate the upper performance limits of the /profile endpoint, which executes a pyinstrument profiling routine inside a Flask server.
This test aims to push the system toward its breaking point by steadily increasing concurrency until the server approaches saturation.

### Configuration
- Tool: Locust 2.42.6
- Users: 50 concurrent simulated users
- Spawn rate: 5 users/second
- Duration: 60 seconds
- Endpoint tested: GET /profile
- Server: Flask running on port 5050 (note: my port 5000 was in use so I switched to 5050)
- Traffic pattern: Rapid ramp-up to high sustained load

### Results
- Total requests: 12,872
- Failures: 0% (no failed or rejected requests)
- Throughput: ~232 requests/second sustained
- Median response time: 15 ms
- Max response time: ~37 ms
- 95th percentile: ~18 ms
- 99th percentile: ~21 ms
- No latency spikes or degradation detected
- Overall, the system maintained stable response times despite high request volume.

### Performance Findings
- The Flask + pyinstrument endpoint demonstrated strong resilience under heavy stress, successfully serving ~230–240 requests per second.
- Zero errors occurred, indicating high stability even when pushed near saturation.
- Latency remained flat and predictable, with median times consistently around 15 ms.
- No resource starvation or slowdowns were observed, suggesting that the workload inside heavy_profile() is CPU-light enough to scale efficiently under concurrency.
- The system comfortably handled all traffic and showed no signs of degradation, implying significant performance headroom for this type of profiling workload.
- Overall, the stress test confirms that the /profile endpoint is robust, stable, and capable of handling substantially higher request volumes than those tested in the load scenario.


## SPIKE TEST
### Test Scope
- Performed a spike test on the /profile endpoint of a Flask application to try to emulate an abrupt surge of traffic. Traffic was generated using Locust 2.42.6.

### Configuration
- Sudden ramp to  around 30 users, 
- Duration was 17 seconds
- Spike load delivered instantly

### Results
- 3,762 total requests ( 0% failures )
- Peak throughput: ~222 RPS
- Average response time: 16.29 ms
- Median (50th percentile): 14 ms
- 95th percentile: ~24–25 ms
- Max latency: 1,465 ms (small outlier typical during spike tests)

### Performance Findings
- System handled the sudden spike without errors or drops in throughput.
- No degradation or instability observed during or after the spike.
- Response times remained stable at 14–16 ms even under peak load.

## Group Contributions
- Jose: Did tool setup, perform load test and recollect the information from the results
- Ursula: Did stress test and report
- Michael: Conducted the Spike Test and reported the data from the results

## Resources
ChatGPT was used for help with phrasing the report and interpreting results.
