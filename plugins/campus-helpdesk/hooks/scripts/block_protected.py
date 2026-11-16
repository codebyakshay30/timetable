#!/usr/bin/env python3
"""PreToolUse hook: block Write/Edit into any 'protected' folder.

Claude Code sends the tool call as JSON on stdin. Exit code 2 = block the
call and show stderr to the agent. Exit 0 = allow.
"""
import json
import sys
from pathlib import PurePosixPath

PROTECTED_DIRS = {"protected"}          # folder names that must never be written to
PROTECTED_NAMES = {".env"}              # individual files that are also off-limits

try:
    data = json.load(sys.stdin)
except json.JSONDecodeError:
    print("Blocked: hook could not parse its input.", file=sys.stderr)
    sys.exit(2)                          # fail closed

raw = str(data.get("tool_input", {}).get("file_path", ""))
path = PurePosixPath(raw.replace("\\", "/"))   # normalise Windows separators

# '..' segments could hide a protected path, so reject them outright
if ".." in path.parts or PROTECTED_DIRS & set(path.parts) or path.name in PROTECTED_NAMES:
    print(f"Blocked: {raw} is inside a protected location.", file=sys.stderr)
    sys.exit(2)
sys.exit(0)
