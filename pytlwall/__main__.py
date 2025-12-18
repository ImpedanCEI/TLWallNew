#!/usr/bin/env python3
"""
Package entry point for pytlwall.

This enables running pytlwall as a module:
    python -m pytlwall --gui       # Launch GUI
    python -m pytlwall -a file.cfg # Batch mode with config file
    python -m pytlwall -i          # Interactive mode
    python -m pytlwall --help      # Show help

The GUI lives in a separate package (pytlwall_gui) and is imported only when
requested to keep console usage lightweight.

Authors: Tatiana Rijoff, Carlo Zannini
Date: December 2025
"""

from __future__ import annotations

import argparse
import sys
from typing import Sequence, Optional


def _check_gui_dependencies() -> bool:
    """Check if GUI dependencies (PyQt5) are available."""
    try:
        import PyQt5
        return True
    except ImportError:
        return False


def _run_gui() -> int:
    """
    Launch the GUI application.
    
    Returns:
        Exit code (0 for success, 1 for error)
    """
    if not _check_gui_dependencies():
        print("Error: GUI dependencies not installed.")
        print("Please install with: pip install pytlwall[gui]")
        print("Or: pip install PyQt5")
        return 1
    
    try:
        from pytlwall_gui.main import main as gui_main
        gui_main()
        return 0
    except ImportError as e:
        print(f"Error: Could not import GUI module: {e}")
        print("Make sure pytlwall_gui package is installed.")
        return 1
    except Exception as e:
        print(f"Error launching GUI: {e}")
        return 1


def _run_console(argv: Sequence[str]) -> int:
    """
    Run the console/CLI workflow (batch or interactive).
    
    Args:
        argv: Command-line arguments
        
    Returns:
        Exit code
    """
    try:
        from pytlwall.run_pytlwall import main as console_main
        return int(console_main(list(argv)))
    except ImportError as e:
        print(f"Error: Could not import console module: {e}")
        return 1
    except Exception as e:
        print(f"Error in console mode: {e}")
        return 1


def _show_version() -> None:
    """Display version information."""
    try:
        from pytlwall._version import __version__
    except ImportError:
        __version__ = "1.0.0"
    
    print(f"pytlwall version {__version__}")
    print("Transmission line impedance calculation engine")
    print("Authors: Tatiana Rijoff, Carlo Zannini")
    print("Original MATLAB implementation: Carlo Zannini, CERN")
    print("Python development: Tatiana Rijoff")


def main(argv: Optional[Sequence[str]] = None) -> int:
    """
    Main entry point for pytlwall.

    Parameters
    ----------
    argv : Sequence[str] | None
        Command-line arguments excluding the program name.
        If None, defaults to sys.argv[1:].

    Returns
    -------
    int
        Process exit code (0 for success, non-zero for error).
        
    Examples
    --------
    >>> main(['--gui'])  # Launch GUI
    >>> main(['-a', 'config.cfg'])  # Batch mode
    >>> main(['-i'])  # Interactive mode
    """
    if argv is None:
        argv = sys.argv[1:]

    parser = argparse.ArgumentParser(
        prog="pytlwall",
        description="Transmission line impedance calculation engine",
        epilog="For GUI mode, use --gui. For batch mode, use -a <config.cfg>",
    )
    
    parser.add_argument(
        "--gui",
        action="store_true",
        help="Launch the graphical user interface",
    )
    
    parser.add_argument(
        "--version", "-V",
        action="store_true",
        help="Show version information and exit",
    )

    # Parse known args, pass rest to console runner
    args, rest = parser.parse_known_args(list(argv))

    if args.version:
        _show_version()
        return 0

    if args.gui:
        return _run_gui()

    # Default to console mode with remaining arguments
    return _run_console(rest)


if __name__ == "__main__":
    raise SystemExit(main())
