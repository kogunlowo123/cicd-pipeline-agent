# CI/CD Pipeline Agent

[![CI](https://github.com/kogunlowo123/cicd-pipeline-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/cicd-pipeline-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: DevOps & Platform Engineering | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

CI/CD automation agent that generates pipeline configurations, diagnoses build failures, optimizes pipeline performance, manages deployment strategies (canary, blue-green, rolling), and provides natural language pipeline administration.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `generate_pipeline` | Generate CI/CD pipeline configuration from requirements |
| `diagnose_failure` | Analyze build/deploy failure logs and identify root cause |
| `optimize_pipeline` | Analyze pipeline for speed improvements (caching, parallelism) |
| `configure_deployment` | Configure deployment strategy (canary, blue-green, rolling) |
| `get_pipeline_metrics` | Get pipeline success rate, duration, and failure trends |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/pipeline/generate` | Generate pipeline config |
| `POST` | `/api/v1/pipeline/diagnose` | Diagnose pipeline failure |
| `POST` | `/api/v1/pipeline/optimize` | Optimize pipeline speed |
| `POST` | `/api/v1/pipeline/deploy` | Configure deployment strategy |
| `GET` | `/api/v1/pipeline/metrics` | Get pipeline metrics |

## Features

- Pipeline Generation
- Failure Diagnosis
- Performance Optimization
- Deployment Strategies
- Pipeline Monitoring

## Integrations

- Github Actions
- Gitlab Ci
- Jenkins
- Argocd
- Docker Registry

## Architecture

```
cicd-pipeline-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── cicd_pipeline_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**GitHub Actions + GitLab CI + Jenkins + ArgoCD**

---

Built as part of the Enterprise AI Agent Platform.
