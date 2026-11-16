#!/usr/bin/env python3
"""Campus Helpdesk MCP server (stdio). MOCK DATA ONLY.

Built with the official MCP Python SDK (package `mcp`, FastMCP helper).
IMPORTANT: stdout is the JSON-RPC channel on stdio. Never print() to stdout;
log to stderr only.
"""
import sys
from mcp.server.fastmcp import FastMCP
import campus_data

mcp = FastMCP("campus-data")


@mcp.tool()
def get_timetable(batch: str, day: str) -> str:
    """Return the classes for ONE batch on ONE weekday from the campus timetable.

    Args:
        batch: Exact batch id such as 'CSE-A-Y2', 'CSE-B-Y2' or 'ECE-A-Y2'.
        day: Weekday as 'Mon', 'Tue', 'Wed', 'Thu', 'Fri' or 'Sat'.
    Returns one line per class (time | course | room | faculty), or
    'No classes found' when the batch has none that day. Read-only. Never
    returns data for other batches. Invalid batch or day raises an error.
    """
    rows = campus_data.timetable_for(batch, day)
    if not rows:
        return "No classes found"
    return "\n".join(f'{r["start"]}-{r["end"]} | {r["course_code"]} {r["course_name"]} | '
                     f'{r["room"]} | {r["faculty"]}' for r in sorted(rows, key=lambda r: r["start"]))


@mcp.tool()
def get_fee_status(student_id: str) -> dict:
    """Return the fee status of ONE student by id (mock data only).

    Args:
        student_id: Id in the form 'S' followed by 4 digits, e.g. 'S1002'.
    Returns total, paid, balance, due_date and status (PAID or PENDING).
    Read-only: this tool cannot change, waive or record payments.
    """
    return campus_data.fee_status(student_id)


@mcp.resource("hostel://rules", mime_type="text/markdown")
def hostel_rules_doc() -> str:
    """The hostel rules document (mock)."""
    return campus_data.hostel_rules()


if __name__ == "__main__":
    print("campus-data MCP server starting on stdio", file=sys.stderr)
    mcp.run(transport="stdio")
