# PyTlWall Tests

**Test suite for the PyTlWall transmission-line wall impedance calculator**

## Authors

- **Tatiana Rijoff** — tatiana.rijoff@gmail.com  
- **Carlo Zannini** — carlo.zannini@cern.ch  

---

## Quick Start

```bash
# Run all unit tests
python tests/run_tests_base.py

# Run specific test module
python tests/test_beam.py -v

# Run deep comparison tests (generates output for manual analysis)
python tests/run_tests_deep.py
```

---

## Test Structure

```
tests/
├── README.md                  # This file
├── run_tests_base.py          # Base test runner (fast unit tests)
├── run_tests_deep.py          # Deep test runner (reference comparison)
│
├── input/                     # Test input files (.cfg, .dat, .txt)
├── output/                    # Generated test outputs
├── logs/                      # Test execution logs
├── deep_test/                 # Deep test configurations and references
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

## Test Levels

| Level | Script | Purpose | Speed |
|-------|--------|---------|-------|
| **Unit Tests** | `run_tests_base.py` | Automated pass/fail validation | Fast (~seconds) |
| **Deep Tests** | `run_tests_deep.py` | Comparison with Wake2D/IW2D references | Slow (~minutes) |

### Unit Tests

Unit tests verify individual components work correctly:

```bash
# Run all unit tests with logging
python tests/run_tests_base.py

# Run specific modules
python tests/run_tests_base.py --modules test_beam.py test_layer.py

# Verbose output
python tests/run_tests_base.py --verbosity 3
```

### Deep Tests

Deep tests compare PyTlWall output against reference solvers (Wake2D, IW2D):

```bash
# Run all deep tests
python tests/run_tests_deep.py

# Run specific test cases
python tests/run_tests_deep.py --subdirs newCV

# Compare with specific reference
python tests/run_tests_deep.py --cfg-pattern "*Wake2D.cfg"
```

> **Note:** Deep tests generate output files for manual analysis. Percentage differences can be misleading for very small values.

---

## Test Modules

| Module | Description | Documentation |
|--------|-------------|---------------|
| `test_beam.py` | Relativistic beam kinematics | [test_beam.md](doc/testing/test_beam.md) |
| `test_chamber.py` | Chamber geometry and Yokoya factors | — |
| `test_layer.py` | Material properties and surface impedance | [test_layer.md](doc/testing/test_layer.md) |
| `test_freq.py` | Frequency array generation | [test_freq.md](doc/testing/test_freq.md) |
| `test_tlwall.py` | Core impedance calculations | [test_tlwall.md](doc/testing/test_tlwall.md) |
| `test_cfg.py` | Configuration file I/O | [test_cfg.md](doc/testing/test_cfg.md) |
| `test_cfgio_realistic.py` | Real .cfg file tests | [test_cfgio_realistic.md](doc/testing/test_cfgio_realistic.md) |
| `test_cfgio_special_cases.py` | Edge cases (inf thickness, etc.) | [test_cfgio_special_cases.md](doc/testing/test_cfgio_special_cases.md) |
| `test_io_util.py` | File I/O utilities | [test_io_util.md](doc/testing/test_io_util.md) |
| `test_plot.py` | Plotting functions | [test_plot.md](doc/testing/test_plot.md) |

---

## Running Individual Tests

```bash
# Run single test file
python tests/test_beam.py -v

# Run specific test class
python -m unittest tests.test_beam.TestBeamInitialization

# Run specific test method
python -m unittest tests.test_beam.TestBeamInitialization.test_default_initialization

# Discover and run tests matching pattern
python -m unittest discover -s tests/ -p "test_cfg*.py"
```

---

## Test Configuration Files

Test input files are in `tests/input/`:

| File | Description |
|------|-------------|
| `one_layer.cfg` | Single layer elliptical chamber |
| `two_layers.cfg` | Multi-layer structure |
| `rectangular_chamber.cfg` | Rectangular chamber |
| `test_round.cfg` | Circular chamber with `:` delimiter |
| `test001.cfg` | Basic test configuration |

---

## Output and Logs

- **Logs:** `tests/logs/tlwall_test_YYYYMMDD_HHMMSS.log`
- **Unit test output:** `tests/output/`
- **Deep test output:** `tests/deep_test/<case>/output/`

---

## Exit Codes

| Code | Meaning |
|------|---------|
| `0` | All tests passed |
| `1` | One or more tests failed |

---

## See Also

- [TESTING.md](../doc/TESTING.md) — Full testing documentation
- [RUN_TESTS_BASE.md](../doc/RUN_TESTS_BASE.md) — Base test runner documentation
- [README.md](../README.md) — Main project documentation

---

*Last updated: December 2025*
