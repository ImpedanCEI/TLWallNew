# PyTlWall Testing Documentation

**Comprehensive test suite documentation**

## Authors

- **Tatiana Rijoff** — tatiana.rijoff@gmail.com  
- **Carlo Zannini** — carlo.zannini@cern.ch  

---

[← Back to README](../README.md) | [API Documentation](API.md)

---

## Table of Contents

1. [Overview](#overview)
2. [Test Structure](#test-structure)
3. [Running Tests](#running-tests)
   - [Single Module Tests](#single-module-tests)
   - [Base Test Suite](#base-test-suite)
   - [Deep Test Suite](#deep-test-suite)
4. [Test Modules](#test-modules)
5. [Writing New Tests](#writing-new-tests)
6. [Test Configuration](#test-configuration)

---

## Overview

PyTlWall uses Python's `unittest` framework for automated testing. The test suite is organized in two levels:

| Test Level | Purpose | Speed | Validation |
|------------|---------|-------|------------|
| **Base Tests** | Unit tests for all modules | Fast (~seconds) | Automated pass/fail |
| **Deep Tests** | Comparison with Wake2D/IW2D references | Slow (~minutes) | Manual analysis required |

All test files are located in the `tests/` directory.

---

## Test Structure

```
tests/
├── README.md                  # Tests overview
├── run_tests_base.py          # Base test runner (fast unit tests)
├── run_tests_deep.py          # Deep test runner (reference comparison)
├── input/                     # Test input files (.cfg, .dat, .txt)
├── output/                    # Generated test outputs
├── logs/                      # Test execution logs
├── deep_test/                 # Deep test configurations
│   ├── newCV/                 # Test case with Wake2D references
│   │   ├── *.cfg              # Configuration files
│   │   ├── Wake2D/            # Wake2D reference data
│   │   └── OldTLWall/         # Old TLWall reference data
│   └── ...
│
├── test_beam.py               # Beam class tests
├── test_chamber.py            # Chamber class tests
├── test_layer.py              # Layer class tests
├── test_freq.py               # Frequencies class tests
├── test_tlwall.py             # TlWall (impedance calc) tests
├── test_cfg.py                # CfgIo class tests
├── test_cfgio_realistic.py    # CfgIo tests with real .cfg files
├── test_cfgio_special_cases.py # CfgIo edge cases
├── test_io_util.py            # I/O utilities tests
└── test_plot.py               # Plotting utilities tests
```

---

## Running Tests

### Single Module Tests

To run tests for a specific module:

```bash
# From project root directory
cd tests/

# Run a single test file
python test_beam.py

# Run with verbose output
python test_beam.py -v

# Run specific test class
python -m unittest test_beam.TestBeamInitialization

# Run specific test method
python -m unittest test_beam.TestBeamInitialization.test_default_initialization

# Run with unittest discover (from tests/ directory)
python -m unittest discover -s . -p "test_beam.py"
```

**Example output:**
```
test_default_initialization (test_beam.TestBeamInitialization) ... ok
test_init_with_gammarel (test_beam.TestBeamInitialization) ... ok
...
----------------------------------------------------------------------
Ran 25 tests in 0.234s

OK
```

---

### Base Test Suite

The `run_tests_base.py` script runs all unit tests with logging support.

#### Method 1: Direct Execution (Default Configuration)

```bash
# From project root
python tests/run_tests_base.py
```

Uses configuration from `TestConfig` class in the script:
- Discovers all `test*.py` files
- Logs to `tests/logs/tlwall_test_YYYYMMDD_HHMMSS.log`
- Verbosity level 2 (INFO)

#### Method 2: Command-Line Arguments

```bash
# Run all tests
python tests/run_tests_base.py

# Run specific modules
python tests/run_tests_base.py --modules test_beam.py test_layer.py

# Change verbosity (1=WARNING, 2=INFO, 3=DEBUG)
python tests/run_tests_base.py --verbosity 3

# Custom test directory
python tests/run_tests_base.py --test_dir ./my_tests/

# Custom log directory
python tests/run_tests_base.py --logdir ./my_logs/

# Custom log filename
python tests/run_tests_base.py --logfile my_test_run

# Custom pattern for test discovery
python tests/run_tests_base.py --pattern "test_cfg*.py"

# Combined options
python tests/run_tests_base.py \
    --modules test_beam.py test_chamber.py \
    --verbosity 3 \
    --logdir ./detailed_logs/
```

See [RUN_TESTS_BASE.md](RUN_TESTS_BASE.md) for complete documentation.

---

### Deep Test Suite

The `run_tests_deep.py` script generates output files for **manual analysis** comparing PyTlWall results with Wake2D and IW2D references.

> ⚠️ **Important**: Deep tests do NOT perform automatic pass/fail validation. Percentage differences can be misleading for very small values. Results require expert analysis.

#### Generated Outputs

For each test case, the script generates:
- **Text files**: `ZLong.txt`, `ZDip.txt`, `ZQuad.txt`
- **Excel comparisons**: `NewTLWallvsWake2D*.xlsx`
- **Plots**: `*.png` comparison plots
- **Logs**: Detailed execution logs

#### Running Deep Tests

```bash
# Run all deep tests
python tests/run_tests_deep.py

# Run specific subdirectories
python tests/run_tests_deep.py --subdirs newCV newPEC

# Use specific config file pattern
python tests/run_tests_deep.py --cfg-pattern "*Wake2D.cfg"

# Skip space charge calculations
python tests/run_tests_deep.py --no-space-charge

# Change verbosity
python tests/run_tests_deep.py --verbosity 3
```

#### Validation Notes

Based on IW2D comparisons:
- **Consistent with IW2D**: ZLong, ZTrans, ZLongTotal, ZDipX, ZDipY, ZQuadX, ZQuadY
- **May show discrepancies**: ZTransTotal, ZDipXTotal, ZDipYTotal, ZQuadXTotal, ZQuadYTotal

---

## Test Modules

Each test module covers a specific PyTlWall component:

| Module | Documentation | Tests |
|--------|---------------|-------|
| `test_beam.py` | [→ test_beam.md](testing/test_beam.md) | Relativistic kinematics |
| `test_chamber.py` | — | Chamber geometry, Yokoya factors |
| `test_layer.py` | [→ test_layer.md](testing/test_layer.md) | Material properties, skin depth |
| `test_freq.py` | [→ test_freq.md](testing/test_freq.md) | Frequency array generation |
| `test_tlwall.py` | [→ test_tlwall.md](testing/test_tlwall.md) | Core impedance calculations |
| `test_cfg.py` | [→ test_cfg.md](testing/test_cfg.md) | Configuration file I/O |
| `test_cfgio_realistic.py` | [→ test_cfgio_realistic.md](testing/test_cfgio_realistic.md) | Real .cfg file tests |
| `test_cfgio_special_cases.py` | [→ test_cfgio_special_cases.md](testing/test_cfgio_special_cases.md) | Edge cases (inf thickness) |
| `test_io_util.py` | [→ test_io_util.md](testing/test_io_util.md) | File I/O utilities |
| `test_plot.py` | [→ test_plot.md](testing/test_plot.md) | Plotting functions |

---

## Impedance Types Tested

The test suite validates all impedance types:

### Base Impedances (Wall Contribution)
- `ZLong` — Longitudinal impedance
- `ZTrans` — Transverse impedance
- `ZDipX`, `ZDipY` — Dipolar impedances
- `ZQuadX`, `ZQuadY` — Quadrupolar impedances

### Total Impedances (Wall + Space Charge)
- `ZLongTotal`, `ZTransTotal`
- `ZDipXTotal`, `ZDipYTotal`
- `ZQuadXTotal`, `ZQuadYTotal`

### Surface Impedances
- `ZLongSurf`, `ZTransSurf`

### Space Charge Impedances
- `ZLongDSC`, `ZLongISC` — Direct/Indirect longitudinal
- `ZTransDSC`, `ZTransISC` — Direct/Indirect transverse

---

## Writing New Tests

### Basic Test Structure

```python
"""
Unit tests for MyModule class.
"""

import unittest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pytlwall.mymodule import MyClass


class TestMyClassInitialization(unittest.TestCase):
    """Test MyClass initialization."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.instance = MyClass()
    
    def test_default_values(self):
        """Test that default values are correct."""
        self.assertEqual(self.instance.value, expected_value)
    
    def test_invalid_input_raises_error(self):
        """Test that invalid input raises appropriate error."""
        with self.assertRaises(ValueError):
            MyClass(invalid_param=-1)


if __name__ == '__main__':
    unittest.main(verbosity=2)
```

### Naming Conventions

- Test files: `test_<module_name>.py`
- Test classes: `Test<ClassName><Aspect>`
- Test methods: `test_<what_is_tested>`
- Use docstrings for all test methods

---

## Test Configuration

### Log Files

Logs are saved to `tests/logs/` with timestamps:
```
tests/logs/
├── tlwall_test_20251218_143025.log
├── deep_test_newCV_20251218_150312.log
└── ...
```

### Input Files

Test configuration files are in `tests/input/`:
```
tests/input/
├── one_layer.cfg
├── two_layers.cfg
├── test001.cfg
├── rectangular_chamber.cfg
├── freq_input.txt
└── ...
```

### Exit Codes

Both test runners return appropriate exit codes:
- `0`: All tests passed
- `1`: One or more tests failed

---

## See Also

- [README.md](../README.md) — Main project documentation
- [RUN_TESTS_BASE.md](RUN_TESTS_BASE.md) — Base test runner documentation
- [tests/README.md](../tests/README.md) — Tests directory overview

---

*Last updated: December 2025*
