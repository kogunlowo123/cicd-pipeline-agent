# CI/CD Pipeline Agent Architecture

CI/CD automation agent that generates pipeline configurations, diagnoses build failures, optimizes pipeline performance, manages deployment strategies (canary, blue-green, rolling), and provides natural language pipeline administration.

## Domain Tools

- **generate_pipeline**: Generate CI/CD pipeline configuration from requirements
- **diagnose_failure**: Analyze build/deploy failure logs and identify root cause
- **optimize_pipeline**: Analyze pipeline for speed improvements (caching, parallelism)
- **configure_deployment**: Configure deployment strategy (canary, blue-green, rolling)
- **get_pipeline_metrics**: Get pipeline success rate, duration, and failure trends