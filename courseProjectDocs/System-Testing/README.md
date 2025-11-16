## How to run these tests
### TC-E2E-001
Make sure you have this library installed:

```pip install pyinstrument```

Install all this in your enviroment (venv is recomended).
1. Position yourself in the follow route ```/courseProjectDocs/System-Testing/TC-E2E-001
2. Inside we would find the ```test_script.py``` with some working code for pyinstrument to analyze
3. Run the follow command this will generate a ```report.html``` file, in case this file doesn't appear run the following command ```ls -la``` or increase the execution time of the script

```
pyinstrument test_script.py -o report.html
```