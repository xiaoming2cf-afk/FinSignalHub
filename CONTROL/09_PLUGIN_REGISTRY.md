# 09 Plugin Registry

## Purpose

Records the local FinSignalHub Codex plugin draft and external plugins used in the workflow.

## Owner

Plugin workflow lead.

## When to update

Update when plugin structure, local installation status, external plugin usage, or marketplace status changes.

## Required fields

- Plugin name
- Path or connector
- Status
- Intended workflow
- Stage usage
- Restrictions

## Example format

`finsignalhub-codex-plugin | local | draft | governance skills | not published`

## Current state

Local plugin: `finsignalhub-codex-plugin`.

Status: draft, local-only, not published.

Intended workflow: package FinSignalHub governance skills, review packet templates, phase acceptance templates, and later MCP-first operating guidance. Stage 00 does not define runtime MCP servers.

Requested external plugins for Stage 00 audit/protocol context: Chrome, Browser, GitHub, OpenAI Developers, Codex Security, Render. Render is not used for deployment in Stage 00 because no hosting deployment is in scope.
