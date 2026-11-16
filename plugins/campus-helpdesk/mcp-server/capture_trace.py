#!/usr/bin/env python3
"""Spawn server.py over stdio, send raw JSON-RPC, and save the real exchange.

Run:  python capture_trace.py  ->  writes ../../../docs/logs/jsonrpc_trace.jsonl
stdio framing = one JSON message per line (UTF-8, no embedded newlines).
Set MCP_PROTOCOL_VERSION to the revision your installed SDK supports
(default 2025-11-25). Revision 2026-07-28 removed the initialize handshake,
so on a newer SDK use the Inspector / SDK client instead and note it in your report.
"""
import json, os, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE.parents[2] / "docs" / "logs" / "jsonrpc_trace.jsonl"
PV = os.environ.get("MCP_PROTOCOL_VERSION", "2025-11-25")

MSGS = [
    {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {
        "protocolVersion": PV, "capabilities": {},
        "clientInfo": {"name": "trace-script", "version": "0.1"}}},
    {"jsonrpc": "2.0", "method": "notifications/initialized"},
    {"jsonrpc": "2.0", "id": 2, "method": "tools/list"},
    {"jsonrpc": "2.0", "id": 3, "method": "tools/call", "params": {
        "name": "get_timetable", "arguments": {"batch": "CSE-A-Y2", "day": "Mon"}}},
    {"jsonrpc": "2.0", "id": 4, "method": "tools/call", "params": {   # failure case
        "name": "get_fee_status", "arguments": {"student_id": "1002; DROP TABLE"}}},
    {"jsonrpc": "2.0", "id": 5, "method": "resources/read", "params": {"uri": "hostel://rules"}},
]

p = subprocess.Popen([sys.executable, str(HERE / "server.py")], stdin=subprocess.PIPE,
                     stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, cwd=HERE)
OUT.parent.mkdir(parents=True, exist_ok=True)
with OUT.open("w", encoding="utf-8") as log:
    for m in MSGS:
        p.stdin.write(json.dumps(m) + "\n"); p.stdin.flush()
        log.write(json.dumps({"dir": "client->server", "msg": m}) + "\n")
        if "id" in m:                       # requests get a response; notifications do not
            line = p.stdout.readline()
            log.write(json.dumps({"dir": "server->client", "msg": json.loads(line)}) + "\n")
            print(line.strip())
    p.stdin.close(); p.wait(timeout=5)
print("saved", OUT)
