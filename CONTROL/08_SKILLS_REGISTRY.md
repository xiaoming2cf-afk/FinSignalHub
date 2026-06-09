# 08 Skills Registry

## Purpose

Registers local FinSignalHub skills and when they must be used.

## Owner

Engineering lead.

## When to update

Update when a skill is added, removed, renamed, or assigned to a stage gate.

## Required fields

- Skill name
- Path
- Purpose
- Required stages
- Failure condition

## Example format

`finsignal-product-governor | .agents/skills/finsignal-product-governor/SKILL.md | required on product drift`

## Current state

Required Stage 00 skills: finsignal-product-governor, phase-gate-auditor, gpt-pro-review-preparer, browser-gpt-pro-reviewer, github-stage-deployer, codex-log-keeper, mcp-tool-builder, connector-builder, evidence-graph-architect, repro-pack-builder, ai-capability-radar, subagent-coordinator, github-review-resolver, acceptance-evidence-collector, stage-next-goal-synthesizer.

Skills are governance artifacts in Stage 00. They do not implement runtime product behavior.

Stage 05 added `computer-use-gpt-pro-reviewer` at `.agents/skills/computer-use-gpt-pro-reviewer/SKILL.md` as a governance-only recovery skill for GPT Pro reviews. It does not make Computer Use available by itself. It must be used only after Chrome/background browser routes fail and only when the current Codex tool surface exposes a callable Computer Use capability.
