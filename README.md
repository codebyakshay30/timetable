
# Campus Helpdesk Agent Toolchain
## Assignment 8 – AI Tools and Prompt Engineering

**Student:** Akshay Sharma  
**Cohort:** Jeff Bezos  
**Roll Number:** 150096725107  
**Programme:** B.Tech Computer Science and Engineering

This project demonstrates four components of an AI-agent toolchain:

1. Agent Skills – reusable instructions for timetable queries.
2. Plugins – packaging Skills, commands, hooks and MCP configuration.
3. Model Context Protocol (MCP) – connecting an agent to mock campus data.
4. Git Worktrees – supporting parallel development.

All student records and campus information in this project are mock data. No real student information, credentials or payment records are used.

---

## Project Structure

```text
timetable/
│
├── .claude-plugin/
│   └── marketplace.json
│
├── docs/
│   ├── Assignment8_Report.pdf
│   ├── STATUS.md
│   ├── sources.md
│   ├── prompt_log.md
│   ├── logs/
│   └── screenshots/
│
├── plugins/
│   └── campus-helpdesk/
│       ├── .claude-plugin/
│       │   └── plugin.json
│       ├── README.md
│       ├── hooks/
│       │   ├── hooks.json
│       │   └── scripts/
│       │       └── block_protected.py
│       ├── skills/
│       │   ├── timetable-helper/
│       │   └── timetable-today/
│       ├── mcp-server/
│       │   ├── server.py
│       │   ├── run_server.py
│       │   ├── campus_data.py
│       │   ├── capture_trace.py
│       │   ├── requirements.txt
│       │   ├── data/
│       │   └── tests/
│       ├── protected/
│       └── .mcp.json
│
├── LICENSE
└── scripts/
    └── simulate_worktrees.sh
```

## Requirements

- Python 3.10 or later
- Git
- Node.js and npm (for MCP Inspector)
- Claude Code (for plugin installation and testing)

## Running the MCP Server

Open the terminal from the project directory:

```bash
cd plugins/campus-helpdesk/mcp-server
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it on macOS/Linux:

```bash
source .venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the unit tests:

```bash
python -m unittest discover -s tests -v
```

Start the MCP Inspector (using `.venv` directly or via `run_server.py`):

```bash
npx -y @modelcontextprotocol/inspector python3 run_server.py
```

Or capture the raw JSON-RPC stdio exchange to `docs/logs/jsonrpc_trace.jsonl`:

```bash
.venv/bin/python capture_trace.py
```

Use the Inspector to connect to the server and test its tools and resource.

The server provides:

| Name | Purpose |
|---|---|
| get_timetable | Retrieves a batch's timetable for a weekday |
| get_fee_status | Retrieves mock fee information for a student ID |
| hostel://rules | Provides the mock hostel rules document |

## Plugin Installation

From the Claude Code terminal, add the marketplace repository:

```text
/plugin marketplace add codebyakshay30/timetable
```

Install the plugin:

```text
/plugin install campus-helpdesk@nimbus-campus-marketplace
```

Reload plugins:

```text
/reload-plugins
```

Test the timetable command:

```text
/campus-helpdesk:timetable-today CSE-A-Y2 Mon
```

Verify the MCP connection:

```text
/mcp
```

To uninstall:

```text
/plugin uninstall campus-helpdesk@nimbus-campus-marketplace
```

For local development, the plugin can also be tested using:

```bash
claude --plugin-dir ./plugins/campus-helpdesk
```

Plugin validation:

```bash
claude plugin validate ./plugins/campus-helpdesk
```

Run these commands in the actual environment and record the results before claiming successful installation.

## Git Worktrees

The project includes a script to demonstrate parallel development:

```bash
sh scripts/simulate_worktrees.sh
```

It demonstrates three workstreams:

- feature/skill-tests
- feature/mcp-server
- bugfix/hook-path

The exercise includes worktree creation, a deliberate merge conflict, conflict resolution and a Git history graph.

Run it only from a clean repository after making the initial commit.

## Testing and Evidence

Recorded execution evidence is stored under `docs/`:

- Skill trigger & description-variant logs: `docs/logs/part_b_skill_tests.log`
- Plugin validation, lifecycle & hook logs: `docs/logs/part_c_plugin_lifecycle.log`, `docs/logs/part_c_hooks.log`
- Package verification & Inspector CLI logs: `docs/logs/part_d_npm_check.log`, `docs/logs/part_d_inspector_cli.log`
- Raw JSON-RPC stdio trace: `docs/logs/jsonrpc_trace.jsonl`
- MCP Inspector screenshots: `docs/screenshots/`
- Git worktree simulation log: `docs/logs/part_e_worktrees.log`

## Security

The project uses mock data only.

The protected-folder hook blocks write and edit operations targeting protected locations. The MCP server provides read-only tools and validates input before returning data.

Third-party plugins and MCP servers should always be reviewed before installation.

## Author

**Akshay Sharma**  
B.Tech Computer Science and Engineering  
ITM Skills University  
Cohort: Jeff Bezos
