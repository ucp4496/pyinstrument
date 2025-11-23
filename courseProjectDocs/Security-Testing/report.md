## Test Scope and Coverage
We performed a static security analysis on the Python source files inside the `pyinstrument/` directory using the Bandit security scanner. The scan targeted Python-specific vulnerabilities such as unsafe use of `assert` (which is removed in optimized bytecode and can hide logic) and the use of `exec` (which can introduce arbitrary code execution risks). All core modules—including the CLI entry point, frame processing logic, renderers, context manager, and vendor utilities—were included in the scan.

---

## Vulnerability Summary

| Title | Type | Severity | Recommended Fix |
|-------|------|----------|------------------|
| Use of `assert` in production code (`__main__.py`) | Insecure Debug Code / Reliability Issue | Low | Replace `assert` with explicit runtime checks (e.g., raise an appropriate exception) so logic is preserved in optimized mode. |
| Use of `exec` to run dynamic code (`__main__.py`) | Arbitrary Code Execution | Medium | Replace `exec` with safer alternatives such as `runpy.run_path`, `importlib`, or controlled subprocess execution. |
| Use of `assert` statement (B101: `assert_used`) | Security / Code Quality | Low | Replace `assert` with an explicit condition and exception handling. |
| Use of `exec` detectec (B102: `exec_used`) | Security | Medium | Avoid using `exec`; use safer alternatives like `ast.literal_eval` or predefined function calls to prevent arbitrary code execution. |

---

## Execution and Results
We ran the security test using Bandit with the command `bandit -r pyinstrument/`. The scan completed without errors, skipped files, or interruptions. Bandit reported **19 issues in total**, with **17 low-severity `assert`-related findings** and **2 medium-severity findings related to the use of `exec`**. No unexpected behavior occurred during the scan, and the tool produced consistent results across all tested files.

## Group contributions
- Ursula: Did tool setup, did vulnerabilities 1 and 2 in the summary table
- Jose: Did vulnerabilities 3 and 4 in the summary table 

## Resources used
Used ChatGPT for help phrasing and formatting readme