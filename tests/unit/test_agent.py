"""CI/CD Pipeline Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_generate_pipeline():
    """Test Generate CI/CD pipeline configuration from requirements."""
    tools = AgentTools()
    result = await tools.generate_pipeline(platform="test", stages="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_diagnose_failure():
    """Test Analyze build/deploy failure logs and identify root cause."""
    tools = AgentTools()
    result = await tools.diagnose_failure(pipeline_id="test", run_id="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_optimize_pipeline():
    """Test Analyze pipeline for speed improvements (caching, parallelism)."""
    tools = AgentTools()
    result = await tools.optimize_pipeline(pipeline_config="test", current_duration_minutes=1)
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_configure_deployment():
    """Test Configure deployment strategy (canary, blue-green, rolling)."""
    tools = AgentTools()
    result = await tools.configure_deployment(strategy="test", target="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.cicd_pipeline_agent_agent import CicdPipelineAgentAgent
    agent = CicdPipelineAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
