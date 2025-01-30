"""
Shared test fixtures for Cline LLM Methodology.
"""

import pytest
from pathlib import Path
import json
import shutil
from typing import Dict, Any

from cline_llm_methodology.llm_setup.setup import ProjectConfig

@pytest.fixture
def test_config() -> ProjectConfig:
    """Base test configuration."""
    return ProjectConfig(
        name="test-project",
        type="api",
        technologies=["python", "fastapi"],
        base_structure="standard",
        documentation_path=Path("test_output")
    )

@pytest.fixture
def config_data() -> Dict[str, Any]:
    """Test configuration data."""
    return {
        "name": "test-project",
        "type": "api",
        "technologies": ["python", "fastapi"],
        "base_structure": "standard"
    }

@pytest.fixture
def config_file(tmp_path, config_data) -> Path:
    """Test configuration file."""
    config_file = tmp_path / "config.json"
    config_file.write_text(json.dumps(config_data))
    return config_file

@pytest.fixture
def project_dir(tmp_path) -> Path:
    """Test project directory with basic structure."""
    # Create directory structure
    dirs = [
        "docs/methodology",
        "docs/adr",
        "src",
        "tests/unit",
        "tests/integration",
        "tools"
    ]
    
    for dir_path in dirs:
        (tmp_path / dir_path).mkdir(parents=True)
        
    # Create basic files
    files = {
        "docs/methodology/llm_methodology.md": "# LLM Methodology\n\nTest content",
        "docs/methodology/tools_integration.md": "# Tools Integration\n\nTest content",
        "docs/methodology/project_initialization.md": "# Project Init\n\nTest content",
        "tools_config.json": "{}"
    }
    
    for file_path, content in files.items():
        (tmp_path / file_path).write_text(content)
        
    return tmp_path

@pytest.fixture
def empty_project_dir(tmp_path) -> Path:
    """Empty project directory."""
    return tmp_path

@pytest.fixture
def cleanup_test_output():
    """Cleanup test output after tests."""
    yield
    test_output = Path("test_output")
    if test_output.exists():
        shutil.rmtree(test_output)

@pytest.fixture
def mock_tools_config() -> Dict[str, Any]:
    """Mock tools configuration."""
    return {
        "browser_action": {
            "resolution": "900x600",
            "screenshots_enabled": True,
            "console_logs_enabled": True
        },
        "tavily_ai": {
            "search_types": {
                "technical": {
                    "depth": "comprehensive",
                    "include_code": True
                }
            }
        },
        "mcp_tools": {
            "enabled": True,
            "auto_discovery": True
        }
    }

@pytest.fixture
def mock_project_context() -> Dict[str, Any]:
    """Mock project context."""
    return {
        "project": {
            "name": "test-project",
            "type": "api",
            "technologies": ["python", "fastapi"]
        },
        "state": {
            "phase": "initialization",
            "progress": 0,
            "mode": "architect"
        },
        "metrics": {
            "documentation": 0,
            "implementation": 0,
            "testing": 0
        }
    }

@pytest.fixture
def mock_docs_content() -> Dict[str, str]:
    """Mock documentation content."""
    return {
        "README.md": "# Test Project\n\nTest content",
        "llm_methodology.md": "# LLM Methodology\n\nTest content",
        "tools_integration.md": "# Tools Integration\n\nTest content",
        "tavily_integration.md": "# Tavily Integration\n\nTest content",
        "project_initialization.md": "# Project Init\n\nTest content",
        "resume_prompt.md": "# Resume Work\n\nTest content"
    }

@pytest.fixture
def mock_gitignore() -> str:
    """Mock .gitignore content."""
    return """
    __pycache__/
    *.py[cod]
    *$py.class
    .env
    .venv
    .coverage
    htmlcov/
    .pytest_cache/
    """