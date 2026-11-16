# Campus Helpdesk Plugin

Bundle for the Nimbus Labs Campus Helpdesk Agent (mock data only):

- **Skill (`timetable-helper`)**: Looks up class timetables from `skills/timetable-helper/data/timetable.csv` with progressive disclosure and anti-fabrication rules.
- **Slash command (`/campus-helpdesk:timetable-today <batch> <day>`)**: User-invoked timetable lookup (`disable-model-invocation: true`).
- **Hook (`PreToolUse`)**: Blocks `Write` and `Edit` calls targeting `protected/` directories, `.env`, or `..` path traversal segments.
- **MCP Server (`campus-data`)**: Stdio FastMCP server (`mcp-server/server.py`, launched via `mcp-server/run_server.py`) exposing `get_timetable`, `get_fee_status`, and `hostel://rules`.

## Installation

```text
/plugin marketplace add codebyakshay30/timetable
/plugin install campus-helpdesk@nimbus-campus-marketplace
```

Or in one step on Claude Code 2.1.275+:

```text
/plugin install campus-helpdesk --marketplace codebyakshay30/timetable
```

## Setup

Create the virtual environment and install dependencies inside `mcp-server/`:

```bash
cd plugins/campus-helpdesk/mcp-server
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m unittest discover -s tests -v
```
