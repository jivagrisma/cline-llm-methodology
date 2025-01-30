"""
Command-line interface for Cline LLM Methodology setup.
"""

import click
from pathlib import Path
import json
from typing import Dict, Any

from .setup import ProjectConfig, LLMMethodologySetup

def load_config(config_file: Path) -> Dict[str, Any]:
    """Load configuration from JSON file."""
    try:
        with config_file.open() as f:
            return json.load(f)
    except Exception as e:
        raise click.ClickException(f"Error loading config file: {str(e)}")

def validate_config(config: Dict[str, Any]) -> None:
    """Validate configuration data."""
    required_fields = ["name", "type", "technologies", "base_structure"]
    missing = [field for field in required_fields if field not in config]
    
    if missing:
        raise click.ClickException(
            f"Missing required fields in config: {', '.join(missing)}"
        )
        
    if not isinstance(config["technologies"], list):
        raise click.ClickException(
            "Field 'technologies' must be a list"
        )

@click.group()
def cli():
    """Cline LLM Methodology setup tools."""
    pass

@cli.command()
@click.argument('config_file', type=click.Path(exists=True, path_type=Path))
@click.option(
    '--output',
    '-o',
    type=click.Path(path_type=Path),
    help='Output directory for project'
)
def setup(config_file: Path, output: Path | None):
    """Setup new project using Cline LLM Methodology.
    
    CONFIG_FILE should be a JSON file with project configuration:
    
    {
        "name": "project-name",
        "type": "api",
        "technologies": ["python", "fastapi"],
        "base_structure": "standard"
    }
    """
    try:
        # Load and validate config
        config = load_config(config_file)
        validate_config(config)
        
        # Use output dir if provided, otherwise use project name
        doc_path = output or Path(config["name"])
        
        # Create project config
        project_config = ProjectConfig(
            name=config["name"],
            type=config["type"],
            technologies=config["technologies"],
            base_structure=config["base_structure"],
            documentation_path=doc_path
        )
        
        # Run setup
        setup = LLMMethodologySetup(project_config)
        setup.run()
        
        click.echo(f"\nProject setup complete: {doc_path}")
        click.echo("\nNext steps:")
        click.echo("1. Review generated documentation in docs/")
        click.echo("2. Configure tools in tools_config.json")
        click.echo("3. Initialize version control")
        click.echo("4. Start development!")
        
    except Exception as e:
        raise click.ClickException(str(e))

@cli.command()
@click.argument('project_dir', type=click.Path(exists=True, path_type=Path))
def validate(project_dir: Path):
    """Validate existing project structure and configuration."""
    try:
        # Check directory structure
        required_dirs = [
            "docs/methodology",
            "docs/adr",
            "src",
            "tests",
            "tools"
        ]
        
        missing_dirs = []
        for dir_path in required_dirs:
            if not (project_dir / dir_path).exists():
                missing_dirs.append(dir_path)
                
        if missing_dirs:
            click.echo("❌ Missing required directories:")
            for dir_path in missing_dirs:
                click.echo(f"  - {dir_path}")
        else:
            click.echo("✅ Directory structure valid")
            
        # Check documentation
        required_docs = [
            "docs/methodology/llm_methodology.md",
            "docs/methodology/tools_integration.md",
            "docs/methodology/project_initialization.md"
        ]
        
        missing_docs = []
        for doc_path in required_docs:
            if not (project_dir / doc_path).exists():
                missing_docs.append(doc_path)
                
        if missing_docs:
            click.echo("\n❌ Missing required documentation:")
            for doc_path in missing_docs:
                click.echo(f"  - {doc_path}")
        else:
            click.echo("✅ Documentation valid")
            
        # Check configuration
        config_file = project_dir / "tools_config.json"
        if not config_file.exists():
            click.echo("\n❌ Missing tools_config.json")
        else:
            try:
                with config_file.open() as f:
                    json.load(f)
                click.echo("✅ Configuration valid")
            except json.JSONDecodeError:
                click.echo("\n❌ Invalid tools_config.json format")
                
    except Exception as e:
        raise click.ClickException(str(e))

@cli.command()
def init():
    """Initialize new project configuration."""
    try:
        config = {
            "name": click.prompt("Project name"),
            "type": click.prompt(
                "Project type",
                type=click.Choice(["api", "web", "cli", "library"])
            ),
            "technologies": click.prompt(
                "Technologies (comma-separated)",
                default="python"
            ).split(","),
            "base_structure": click.prompt(
                "Base structure",
                type=click.Choice(["standard", "minimal"]),
                default="standard"
            )
        }
        
        output_file = Path("project_config.json")
        with output_file.open("w") as f:
            json.dump(config, f, indent=2)
            
        click.echo(f"\nConfiguration saved to {output_file}")
        click.echo("\nNext step: Run setup with the config file:")
        click.echo(f"  llm-setup setup {output_file}")
        
    except Exception as e:
        raise click.ClickException(str(e))

def main():
    """Main entry point."""
    cli()