"""Test configuration for CI/CD Pipeline Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "cicd-pipeline-agent", "category": "DevOps & Platform Engineering"}
