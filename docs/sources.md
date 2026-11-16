# Sources and References

**Access date:** 17 November 2026

All primary documentation, specifications, RFCs, packages, and research references below were directly accessed and verified on **17 November 2026** (HTTP 200 or live CLI/registry query unless explicitly noted as 404/non-existent).

## Official Documentation & Specifications

1. **Model Context Protocol – Specification Changelog (Latest Revision: 2026-07-28)**  
   https://modelcontextprotocol.io/specification/latest/changelog

2. **Model Context Protocol – Base Protocol Overview (Revision 2025-11-25, matching `mcp==1.30.0`)**  
   https://modelcontextprotocol.io/specification/2025-11-25/basic

3. **Model Context Protocol – Server Features Overview (Tools, Resources, Prompts; Revision 2025-11-25)**  
   https://modelcontextprotocol.io/specification/2025-11-25/server

4. **Claude Code – Agent Skills Documentation**  
   https://code.claude.com/docs/en/skills.md

5. **Claude Code – Plugins Overview**  
   https://code.claude.com/docs/en/plugins/overview.md

6. **Claude Code – Create a Plugin**  
   https://code.claude.com/docs/en/plugins/create.md

7. **Claude Code – Install and Manage Plugins**  
   https://code.claude.com/docs/en/plugins/install.md

8. **Claude Code – Plugin Marketplaces (Manifest & Required `owner` Field)**  
   https://code.claude.com/docs/en/plugin-marketplaces.md

9. **Claude Code – Hooks Reference**  
   https://code.claude.com/docs/en/hooks.md

10. **Claude Code – Run Parallel Sessions with Worktrees**  
    https://code.claude.com/docs/en/worktrees.md

11. **Git – `git-worktree` Manual**  
    https://git-scm.com/docs/git-worktree.html

12. **Model Context Protocol – Official Python SDK**  
    https://github.com/modelcontextprotocol/python-sdk

13. **Model Context Protocol – MCP Inspector**  
    https://github.com/modelcontextprotocol/inspector

## Standards & Research Checked During Claim Audit

14. **IETF RFC 9999 – *Remote ATtestation procedureS (RATS) Conceptual Message Wrapper (CMW)*** (July 2026; verifies RFC 9999 is not "MCP Transport Security")  
    https://www.rfc-editor.org/info/rfc9999/

15. **IETF RFC 8032 – *Edwards-Curve Digital Signature Algorithm (EdDSA)*** (defines Ed25519)  
    https://www.rfc-editor.org/info/rfc8032/

16. **Liu, Chen, and Zhang (2026) – *"Lost in Implicit Routing: How LLM Agents Fail to Load Relevant Skills at Scale"*** (`arXiv:2610.18522`; verifies Claim 10's "Hendricks and Oyelaran (2024)" citation and numbers do not match published literature)  
    https://arxiv.org/abs/2610.18522

## Third-Party / Package Registry Verification

17. **Community Worktree Slash Commands (`deikka/worktree-claude-code-commands`)** — third-party repository defining a user-copied `/worktree-merge` command, confirming it is *not* built into Claude Code  
    https://github.com/deikka/worktree-claude-code-commands

18. **npm Registry Verification (`@nimbus/mcp-skill-bridge` vs. `mcp-skill-bridge`)** — `npm view @nimbus/mcp-skill-bridge` returned HTTP 404 Not Found; unrelated unscoped `mcp-skill-bridge` exists at `0.0.3` (Proprietary, maintainer `sunwu51`):  
    https://registry.npmjs.org/mcp-skill-bridge
