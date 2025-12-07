## How to run these tests

Make sure you have this library installed:

```pip install locust```
```pip install flask```

Install all this in your enviroment (venv is recomended).
1. Position yourself in the Performance-Testing folder
2. Open two terminals and in one open the ```server.py``` and in the other run the following commands depending on the performance testing

- Load Test
```
locust -f locustfile.py --headless --users 10 --spawn-rate 2 --run-time 30s --host=http://localhost:5000 --html=load.html
``` 

- Stress Test
```
locust -f locustfile.py --headless --users 10 --spawn-rate 2 --run-time 30s --host=http://localhost:5000 --html=stress.html
``` 

- Spike Test
```
locust -f locustfile.py --headless --users 10 --spawn-rate 2 --run-time 30s --host=http://localhost:5000 --html=spike.html
``` 