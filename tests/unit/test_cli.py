"""
Unit tests for CLI module.
"""

import pytest
from pathlib import Path
import json
from click.testing import CliRunner
from cline_llm_methodology.llm_setup.cli import cli, setup, validate, init

@pytest.fixture
def runner():
    """Test CLI runner."""
    return CliRunner()

@pytest.fixture
def test_config(tmp_path):
    """Test configuration file."""
    config = {
        "name": "test-project",
        "type": "api",
        "technologies": ["python", "fastapi"],
        "base_structure": "standard"
    }
    
    config_file = tmp_path / "config.json"
    config_file.write_text(json.dumps(config))
    return config_file

def test_setup_command(runner, test_config, tmp_path):
    """Test setup command."""
    result = runner.invoke(setup, [str(test_config), "-o", str(tmp_path)])
    assert result.exit_code == 0
    
    # Check output directory
    assert (tmp_path / "docs").exists()
    assert (tmp_path / "src").exists()
    assert (tmp_path / "tests").exists()
    
    # Check specific files
    assert (tmp_path / "tools_config.json").exists()
    assert (tmp_path / "docs/methodology/llm_methodology.md").exists()

def test_setup_with_invalid_config(runner, tmp_path):
    """Test setup with invalid configuration."""
    # Create invalid config
    config = {
        "name": "test-project",
        # Missing required fields
    }
    
    config_file = tmp_path / "invalid_config.json"
    config_file.write_text(json.dumps(config))
    
    result = runner.invoke(setup, [str(config_file)])
    assert result.exit_code != 0
    assert "Missing required fields" in result.output

def test_validate_command_valid_project(runner, tmp_path):
    """Test validate command with valid project."""
    # Create valid project structure
    (tmp_path / "docs/methodology").mkdir(parents=True)
    (tmp_path / "docs/adr").mkdir()
    (tmp_path / "src").mkdir()
    (tmp_path / "tests").mkdir()
    (tmp_path / "tools").mkdir()
    
    # Create required files
    (tmp_path / "docs/methodology/llm_methodology.md").touch()
    (tmp_path / "docs/methodology/tools_integration.md").touch()
    (tmp_path / "docs/methodology/project_initialization.md").touch()
    (tmp_path / "tools_config.json").write_text("{}")
    
    result = runner.invoke(validate, [str(tmp_path)])
    assert result.exit_code == 0
    assert "✅ Directory structure valid" in result.output
    assert "✅ Documentation valid" in result.output
    assert "✅ Configuration valid" in result.output

def test_validate_command_invalid_project(runner, tmp_path):
    """Test validate command with invalid project."""
    # Create incomplete project structure
    (tmp_path / "src").mkdir()
    
    result = runner.invoke(validate, [str(tmp_path)])
    assert result.exit_code == 0  # Command succeeds but reports issues
    assert "❌ Missing required directories" in result.output
    assert "❌ Missing required documentation" in result.output
    assert "❌ Missing tools_config.json" in result.output

def test_init_command(runner, tmp_path):
    """Test init command."""
    with runner.isolated_filesystem(temp_dir=tmp_path):
        # Simulate user input
        inputs = [
            "test-project",  # name
            "api",          # type
            "python,fastapi",  # technologies
            "standard",     # base_structure
            ""             # Enter to confirm
        ]
        
        result = runner.invoke(init, input="\n".join(inputs))
        assert result.exit_code == 0
        
        # Check generated config file
        config_file = Path("project_config.json")
        assert config_file.exists()
        
        config = json.loads(config_file.read_text())
        assert config["name"] == "test-project"
        assert config["type"] == "api"
        assert config["technologies"] == ["python", "fastapi"]
        assert config["base_structure"] == "standard"

def test_init_command_invalid_input(runner, tmp_path):
    """Test init command with invalid input."""
    with runner.isolated_filesystem(temp_dir=tmp_path):
        # Simulate invalid input
        inputs = [
            "",  # Empty name
            "invalid-type",  # Invalid type
            "python",
            "standard",
            ""
        ]
        
        result = runner.invoke(init, input="\n".join(inputs))
        assert result.exit_code != 0

def test_setup_command_file_not_found(runner):
    """Test setup command with non-existent config file."""
    result = runner.invoke(setup, ["nonexistent.json"])
    assert result.exit_code != 0
    assert "Error" in result.output

def test_validate_command_directory_not_found(runner):
    """Test validate command with non-existent directory."""
    result = runner.invoke(validate, ["nonexistent"])
    assert result.exit_code != 0
    assert "Error" in result.output

def test_setup_command_with_existing_output(runner, test_config, tmp_path):
    """Test setup command with existing output directory."""
    # Create existing file
    docs_dir = tmp_path / "docs"
    docs_dir.mkdir(parents=True)
    test_file = docs_dir / "existing.md"
    test_file.write_text("Existing content")
    
    result = runner.invoke(setup, [str(test_config), "-o", str(tmp_path)])
    assert result.exit_code == 0
    
    # Verify existing file was preserved
    assert test_file.exists()
    assert test_file.read_text() == "Existing content"

def test_cli_help(runner):
    """Test CLI help output."""
    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0
    assert "Cline LLM Methodology setup tools" in result.output
    
    # Test subcommands help
    for cmd in ["setup", "validate", "init"]:
        result = runner.invoke(cli, [cmd, "--help"])
        assert result.exit_code == 0
        assert cmd in result.output