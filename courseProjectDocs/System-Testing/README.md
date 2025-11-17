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

### TC-E2E-003
1. Ensure that this library is installed on your device:
```pip install pyinstrument```
2. Install all this in your enviroment (venv is recomended).
3. Make sure your pathing to ```test_script.py``` is correct
4. Run this command with the path from step three.
```python3 -m pyinstrument --renderer json "/mnt/c/.../pyinstrument/courseProjectDocs/System-Testing/Test-JSON-UI/test_script.py" > output.json```
