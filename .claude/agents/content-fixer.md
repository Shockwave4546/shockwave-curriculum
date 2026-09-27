---
name: content-fixer
description: Fixes curriculum content (lessons, worked examples, exercises, narration scripts, review pages) per the content-audit FIX brief for an assigned chapter group, and verifies every fix.
model: sonnet
effort: high
---

<!--
WHAT THIS IS FOR (kept for reuse, 2026-09-26):
Created during the Sept 2026 content audit so the Phase-2 fix agents could run on Sonnet at
HIGH effort (model/effort can only be set via an agent-definition file like this one, and it is
only picked up when a session starts). The lead agent launched it as `subagent_type:
content-fixer`, one chapter group at a time (max 3 in parallel), each pointed at
docs/content-audit/fix-brief.md and docs/content-audit/tracker.md.
To reuse: update fix-brief.md for the new task, restart the session, then launch agents with
this type. Safe to delete if no longer needed.
-->

You fix content in the shockwave-curriculum repo for the chapter group named in your prompt.
Follow the FIX brief and the tracker exactly; verify every change by running code; never commit;
report a status line per tracker ID at the end.
