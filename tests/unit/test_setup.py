"""
Unit tests for LLM Methodology setup.
"""

import pytest
from pathlib import Path
import json
import yaml
from cline_llm_methodology.llm_setup.setup import ProjectConfig, LLMMethodologySetup

@pytest.fixture
def test_config():
    """Test project configuration."""
    return ProjectConfig(
        name="test-project",
        type="api",
        technologies=["python", "fastapi"],
        base_structure="standard",
        documentation_path=Path("test_output")
    )

@pytest.fixture
def setup_instance(test_config, tmp_path):
    """Test setup instance with temporary path."""
    test_config.documentation_path = tmp_path
    return LLMMethodologySetup(test_config)

def test_create_directory_structure(setup_instance):
    """Test directory structure creation."""
    setup_instance.create_directory_structure()
    
    # Check required directories
    required_dirs = [
        "docs/adr",
        "docs/methodology",
        "docs/analysis",
        "docs/guides",
        "src",
        "tests/unit",
        "tests/integration",
        "tools",
        "examples"
    ]
    
    for dir_path in required_dirs:
        assert (setup_instance.config.documentation_path / dir_path).exists()

def test_create_base_documentation(setup_instance):
    """Test base documentation creation."""
    setup_instance.create_directory_structure()
    setup_instance.create_base_documentation()
    
    # Check required documentation files
    required_docs = [
        "docs/methodology/README.md",
        "docs/methodology/llm_methodology.md",
        "docs/methodology/tools_integration.md",
        "docs/methodology/tavily_integration.md",
        "docs/methodology/project_initialization.md",
        "docs/methodology/resume_prompt.md"
    ]
    
    for doc_path in required_docs:
        assert (setup_instance.config.documentation_path / doc_path).exists()
        assert (setup_instance.config.documentation_path / doc_path).stat().st_size > 0

def test_setup_tools_configuration(setup_instance):
    """Test tools configuration setup."""
    setup_instance.setup_tools_configuration()
    
    config_path = setup_instance.config.documentation_path / "tools_config.json"
    assert config_path.exists()
    
    # Verify config content
    with config_path.open() as f:
        config = json.load(f)
        
    assert "browser_action" in config
    assert "tavily_ai" in config
    assert "mcp_tools" in config
    
    # Check specific settings
    assert config["browser_action"]["resolution"] == "900x600"
    assert config["tavily_ai"]["search_types"]["technical"]["include_code"] is True
    assert config["mcp_tools"]["enabled"] is True

def test_create_project_context(setup_instance):
    """Test project context creation."""
    setup_instance.create_project_context()
    
    context_path = setup_instance.config.documentation_path / "docs/methodology/context.yaml"
    assert context_path.exists()
    
    # Verify context content
    with context_path.open() as f:
        context = yaml.safe_load(f)
        
    assert context["project"]["name"] == setup_instance.config.name
    assert context["project"]["type"] == setup_instance.config.type
    assert context["project"]["technologies"] == setup_instance.config.technologies
    
    assert context["state"]["phase"] == "initialization"
    assert "metrics" in context

def test_setup_version_control(setup_instance):
    """Test version control setup."""
    setup_instance.setup_version_control()
    
    gitignore_path = setup_instance.config.documentation_path / ".gitignore"
    assert gitignore_path.exists()
    
    content = gitignore_path.read_text()
    assert "__pycache__" in content
    assert ".env" in content
    assert ".coverage" in content

def test_full_setup_process(setup_instance):
    """Test complete setup process."""
    setup_instance.run()
    
    # Verify all components
    assert (setup_instance.config.documentation_path / "docs").exists()
    assert (setup_instance.config.documentation_path / "src").exists()
    assert (setup_instance.config.documentation_path / "tests").exists()
    assert (setup_instance.config.documentation_path / "tools_config.json").exists()
    assert (setup_instance.config.documentation_path / ".gitignore").exists()
    
    # Check documentation
    methodology_path = setup_instance.config.documentation_path / "docs/methodology/llm_methodology.md"
    assert methodology_path.exists()
    content = methodology_path.read_text()
    assert "Core Principles" in content
    assert "Components" in content

def test_setup_with_invalid_config():
    """Test setup with invalid configuration."""
    with pytest.raises(ValueError):
        ProjectConfig(
            name="",  # Invalid empty name
            type="api",
            technologies=["python"],
            base_structure="standard",
            documentation_path=Path("test")
        )

def test_setup_with_existing_files(setup_instance):
    """Test setup with existing files."""
    # Create existing file
    docs_dir = setup_instance.config.documentation_path / "docs"
    docs_dir.mkdir(parents=True)
    test_file = docs_dir / "test.md"
    test_file.write_text("Test content")
    
    # Run setup - should not raise errors
    setup_instance.run()
    
    # Verify existing file was preserved
    assert test_file.exists()
    assert test_file.read_text() == "Test content"