# RUN_TESTS_BASE.md

**Base Test Runner Documentation**

## Authors

- **Tatiana Rijoff** — tatiana.rijoff@gmail.com  
- **Carlo Zannini** — carlo.zannini@cern.ch  

---

## Overview

`run_tests_base.py` is the main test runner for PyTlWall unit tests. It discovers and executes test files, provides logging, and reports results.

**Location:** `tests/run_tests_base.py`

---

## Quick Start

```bash
# Run all tests with default settings
python tests/run_tests_base.py

# Run specific modules
python tests/run_tests_base.py --modules test_beam.py test_layer.py

# Verbose output
python tests/run_tests_base.py --verbosity 3
```

---

## Command-Line Arguments

| Argument | Description | Default |
|----------|-------------|---------|
| `--modules` | Specific test modules to run | All `test*.py` |
| `--test_dir` | Directory containing tests | `./tests/` |
| `--logdir` | Directory for log files | `./tests/logs/` |
| `--logfile` | Base name for log file | `tlwall_test` |
| `--pattern` | Pattern for test discovery | `test*.py` |
| `--verbosity` | Output verbosity (1-3) | `2` |

### Examples

```bash
# Run only beam and layer tests
python tests/run_tests_base.py --modules test_beam.py test_layer.py

# Maximum verbosity
python tests/run_tests_base.py --verbosity 3

# Custom log location
python tests/run_tests_base.py --logdir ./my_logs/ --logfile my_test_run

# Run tests matching pattern
python tests/run_tests_base.py --pattern "test_cfg*.py"

# Combined options
python tests/run_tests_base.py \
    --modules test_beam.py test_tlwall.py \
    --verbosity 3 \
    --logdir ./detailed_logs/
```

---

## Configuration Class

The `TestConfig` class in `run_tests_base.py` provides default settings:

```python
class TestConfig:
    """Configuration for test execution."""
    
    # Directory containing test files
    TEST_DIR: str = "./tests/"
    
    # Directory for log files
    LOG_DIR: str = "./tests/logs/"
    
    # Base name for log files (timestamp added automatically)
    LOG_BASENAME: str = "tlwall_test"
    
    # Pattern for test file discovery
    PATTERN: str = "test*.py"
    
    # Output verbosity: 1=WARNING, 2=INFO, 3=DEBUG
    VERBOSITY: int = 2
    
    # Specific modules to run (None = all matching pattern)
    SELECTED_MODULES: Optional[List[str]] = None
```

### Modifying Defaults

Edit `run_tests_base.py` to change defaults:

```python
class TestConfig:
    TEST_DIR: str = "./tests/"
    LOG_DIR: str = "./tests/logs/"
    LOG_BASENAME: str = "tlwall_test"
    PATTERN: str = "test*.py"
    VERBOSITY: int = 2
    
    # Run only specific modules by default
    SELECTED_MODULES = ["test_beam.py", "test_layer.py", "test_tlwall.py"]
```

---

## Programmatic Usage

Use the test runner from Python code:

```python
from tests.run_tests_base import run_selected_unittests_with_log, TestConfig

# Method 1: Use TestConfig defaults
success = run_selected_unittests_with_log(
    test_dir=TestConfig.TEST_DIR,
    logdir=TestConfig.LOG_DIR,
    logfile=TestConfig.LOG_BASENAME,
    pattern=TestConfig.PATTERN,
    verbosity=TestConfig.VERBOSITY,
    selected_modules=TestConfig.SELECTED_MODULES,
)

# Method 2: Custom parameters
success = run_selected_unittests_with_log(
    test_dir="./tests/",
    logdir="./custom_logs/",
    logfile="my_tests",
    pattern="test_cfg*.py",
    verbosity=3,
    selected_modules=["test_cfg.py", "test_cfgio_realistic.py"],
)

print(f"Tests {'passed' if success else 'failed'}")
```

---

## Log Files

### Log Location

Logs are saved to `tests/logs/` with automatic timestamps:

```
tests/logs/
├── tlwall_test_20251218_143025.log
├── tlwall_test_20251218_150312.log
└── ...
```

### Log Format

```
2025-12-18 14:30:25 - INFO - Starting test run
2025-12-18 14:30:25 - INFO - Test directory: ./tests/
2025-12-18 14:30:25 - INFO - Modules: test_beam.py, test_layer.py
2025-12-18 14:30:25 - INFO - Running: test_beam.TestBeamInitialization.test_default_initialization
2025-12-18 14:30:25 - INFO - PASS: test_default_initialization
...
2025-12-18 14:30:28 - INFO - Tests run: 125, Failures: 0, Errors: 0
2025-12-18 14:30:28 - INFO - Test run completed: PASSED
```

### Verbosity Levels

| Level | Description | Output |
|-------|-------------|--------|
| `1` | WARNING | Only failures and errors |
| `2` | INFO | Test names and results |
| `3` | DEBUG | Detailed execution trace |

---

## Test Discovery

The runner uses Python's `unittest` discovery mechanism:

1. Scans `test_dir` for files matching `pattern`
2. If `selected_modules` is set, filters to those modules
3. Loads test cases from each module
4. Executes tests and collects results

### Discovery Examples

```python
# Discover all test*.py files
pattern = "test*.py"

# Discover only cfg-related tests
pattern = "test_cfg*.py"

# Discover tests starting with specific prefix
pattern = "test_beam*.py"
```

---

## Exit Codes

| Code | Meaning |
|------|---------|
| `0` | All tests passed |
| `1` | One or more tests failed or errored |

### Using Exit Codes in Scripts

```bash
# Run tests and check result
python tests/run_tests_base.py
if [ $? -eq 0 ]; then
    echo "All tests passed!"
else
    echo "Some tests failed!"
    exit 1
fi
```

---

## Test Modules Reference

| Module | Tests | Description |
|--------|-------|-------------|
| `test_beam.py` | ~25 | Beam class and relativistic kinematics |
| `test_chamber.py` | ~20 | Chamber geometry and Yokoya factors |
| `test_layer.py` | ~40 | Layer material properties |
| `test_freq.py` | ~30 | Frequency array generation |
| `test_tlwall.py` | ~50 | Core impedance calculations |
| `test_cfg.py` | ~25 | Configuration file I/O |
| `test_cfgio_realistic.py` | ~20 | Real .cfg file tests |
| `test_cfgio_special_cases.py` | ~10 | Edge cases |
| `test_io_util.py` | ~30 | I/O utilities |
| `test_plot.py` | ~5 | Plotting functions |

---

## Troubleshooting

### Import Errors

If tests fail with import errors:

```bash
# Ensure pytlwall is installed
pip install -e .

# Or add to PYTHONPATH
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
```

### Permission Errors

If logs can't be written:

```bash
# Create log directory
mkdir -p tests/logs

# Check permissions
chmod 755 tests/logs
```

### Test Discovery Issues

If tests aren't found:

```bash
# Verify test files exist
ls tests/test*.py

# Check pattern matches
python -c "import glob; print(glob.glob('tests/test*.py'))"

# Run discovery manually
python -m unittest discover -s tests/ -p "test*.py" -v
```

---

## Integration with CI/CD

### GitHub Actions Example

```yaml
name: Tests
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - run: pip install -e .
      - run: python tests/run_tests_base.py
```

### GitLab CI Example

```yaml
test:
  stage: test
  script:
    - pip install -e .
    - python tests/run_tests_base.py
  artifacts:
    paths:
      - tests/logs/
    when: always
```

---

## See Also

- [README.md](../tests/README.md) — Tests overview
- [TESTING.md](TESTING.md) — Full testing documentation
- [run_tests_deep.py](../tests/run_tests_deep.py) — Deep test runner

---

*Last updated: December 2025*
