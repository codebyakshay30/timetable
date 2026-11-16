#!/usr/bin/env python3
"""Launch server.py using the local .venv Python if present, else sys.executable."""
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
for candidate in (
    HERE / ".venv" / "bin" / "python",
    HERE / ".venv" / "Scripts" / "python.exe",
):
    if candidate.is_file():
        py = str(candidate)
        break
else:
    py = sys.executable

os.execv(py, [py, str(HERE / "server.py"), *sys.argv[1:]])
