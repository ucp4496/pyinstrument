# System Testing Report for Pyinstrument
## Test Scope and Coverage
### TC-E2E-001
This system level test validate the main end to end workflow of the ```pyinstrument``` profiling tool.
- Execute a Python script through the Command Line Interface (CLI) using ```pyinstrument```
- Generate an HTML report showing function calls and execution times
- Display accurate program output and profiling summary

The test simulate real user interaction with public CLI interface, ensuring that core profiling functionality and output generation behave as expected

### TC-E2E-XXX
### TC-E2E-XXX

## Test Case Summary
### Test ID
TC-E2E-001
### Title
Profiling a simple Python script via CLI
### Pre conditions
Create a simple script with working Python code (test_script.py)
### Test steps
1. Open de terminal in courseProjectDocs/System-Testing/TC-E2E-001
2. Run ```pyinstrument test_script.py -o report.html```
3. Verify that report.html was generated
4. Open the report in the browser
### Expected results
- report.html is created in the current directory
- The HTML reports shows profiling data with function ranmes and execution times

### Test ID
TC-E2E-XXX
### Title
### Pre conditions
### Test steps
### Expected results

### Test ID
TC-E2E-003
### Title
End-to-End Validation of PyInstrument JSON UI Renderer
### Pre conditions
PyInstrument is installed and accessible through the CLI (either via WSL or Windows).
A valid Python script exists at the test path (e.g., test_script.py).
The tester has permission to execute commands and write output files.
The environment uses a supported Python version (3.8+).
### Test steps
In WSL, run the following command: ```python3 -m pyinstrument --renderer json "/mnt/c/Users/.../test_script.py" > output.json```

### Expected results
output.json is created and contains valid JSON.

## Execution and Results
- Initial attempt using ```-o report.html``` did not generate the file. I needed to do a ls -la to show the ```report.html``` file
- If the code takes to little time to execute it doesnt create the ```report.html```
- No functional defects were found after incrementing the time of execution of the script


- The JSON UI test command successfully executed using the PyInstrument CLI with no errors or warnings.
- The output file output.json was made without issues.
- Parsing the JSON shows that the file structure was valid and contained all required top-level fields: ```"root_frame"```,```"duration"```, ```"samples"```, and ```"frames"```

## Group Contributions
- Jose: Designed and executed the CLI end to end profiling test case (TC-E2E-001). Documented results, verified HTML output generation and identified the correct report generation method
- Ursula:
- Michael: Designed the JSON UI end-to-end system test, along with executing the test in the development environment.