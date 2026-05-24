# 22 Hooks And Automations

## Purpose

Defines hook and automation policy for FinSignalHub.

## Owner

Engineering lead.

## When to update

Update when a hook, scheduled automation, CI automation, or review automation is added or changed.

## Required fields

- Automation name
- Trigger
- Scope
- Files affected
- Safety checks
- Owner
- Status

## Example format

`phase-check | PR | governance files | read-only checks | no secrets | engineering lead | planned`

## Current state

Stage 00 creates GitHub workflow placeholders for governance checks only. No recurring automation, production hook, external deployment hook, or runtime job is active.
