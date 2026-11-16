#!/bin/sh
# Part E: three linked worktrees, a deliberate merge conflict, resolution, graph.
# Run from the repo root:  sh scripts/simulate_worktrees.sh
set -e
git config user.name  >/dev/null 2>&1 || git config user.name  "Student"
git config user.email >/dev/null 2>&1 || git config user.email "student@example.com"
BASE=$(git rev-parse --abbrev-ref HEAD)
mkdir -p ../wt && echo "== create worktrees" 
git worktree add -b feature/skill-tests ../wt/skill-tests
git worktree add -b feature/mcp-server  ../wt/mcp-server
git worktree add -b bugfix/hook-path    ../wt/hook-path
echo "== worktree list"; git worktree list
echo "== same branch twice is refused (default safeguard)"
git worktree add ../wt/dup feature/skill-tests || true

echo "== a change in each worktree"
( cd ../wt/skill-tests && printf '## Skill tests\nTrigger tests: 6 prompts recorded.\n' > docs/SKILL_TESTS.md \
  && echo "Status: skill tests written" >> docs/STATUS.md && git add -A && git commit -qm "skill-tests: add test log and status" )
( cd ../wt/mcp-server  && echo "Status: mcp server done" >> docs/STATUS.md && git add -A && git commit -qm "mcp-server: update status" )
( cd ../wt/hook-path   && python3 -c 'from pathlib import Path; p=Path("plugins/campus-helpdesk/hooks/scripts/block_protected.py"); p.write_text(p.read_text().replace("PROTECTED_DIRS = {\"protected\"}", "PROTECTED_DIRS = {\"protected\", \"secrets\"}"))' \
  && git add -A && git commit -qm "hook-path: also protect secrets folder" )

echo "== merge skill-tests into $BASE, then mcp-server (conflict on docs/STATUS.md)"
git merge --no-ff -m "Merge feature/skill-tests" feature/skill-tests
git merge --no-ff -m "Merge feature/mcp-server" feature/mcp-server || true
echo "-- conflict state:"; git status --short; echo "-- conflict markers in docs/STATUS.md:"; tail -n 8 docs/STATUS.md
printf 'Status: skill tests written\nStatus: mcp server done\n' > docs/STATUS.md   # keep both lines
git add docs/STATUS.md && git commit -qm "Merge feature/mcp-server (resolved STATUS.md conflict)"
git merge --no-ff -m "Merge bugfix/hook-path" bugfix/hook-path
echo "== history graph"; git log --graph --oneline --decorate --all

echo "== cleanup"
git worktree remove ../wt/skill-tests; git worktree remove ../wt/mcp-server; git worktree remove ../wt/hook-path
git worktree list; git worktree prune -v
git branch -d feature/skill-tests feature/mcp-server bugfix/hook-path
