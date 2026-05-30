# BTP Usage Agent

A Joule AI agent that helps BTP administrators query and analyze daily subaccount usage for SAP HANA Cloud, AI Core, Cloud Foundry Runtime, and Integration Suite via the SAP UAS Reporting API

## Overview

Uses A2A Protocol, LangGraph, LiteLLM, and SAP Cloud SDK.

## Structure

- `app/main.py` - A2A server entry
- `app/agent_executor.py` - Request handling
- `app/agent.py` - Agent logic

## Local Development Setup

Copy `.env.example` to `.env` and fill in your credentials — **never commit `.env` to Git**:

```bash
cp .env.example .env
# Edit .env with your actual BTP and AI Core service key values
```

## Credentials / Security Notes

- **`.env` is listed in `.gitignore` and `.dockerignore`** — it must never be committed to Git or baked into a Docker image.
- For production deployments on BTP, inject credentials via **BTP environment bindings** or **Kubernetes Secrets**.  The app reads all credentials from environment variables at startup (`os.environ`).
- Rotate service keys immediately if they are ever accidentally exposed.
