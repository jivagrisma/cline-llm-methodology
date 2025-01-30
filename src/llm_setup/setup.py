"""
Core setup module for Cline LLM Methodology.
"""

from dataclasses import dataclass
from pathlib import Path
import shutil
import json
import yaml
from typing import Dict, List, Optional
import logging
import sys

@dataclass
class ProjectConfig:
    """Project configuration."""
    name: str
    type: str
    technologies: List[str]
    base_structure: str
    documentation_path: Path

class LLMMethodologySetup:
    """Implementation of the LLM methodology setup."""
    
    def __init__(self, config: ProjectConfig):
        """Initialize setup with project configuration.
        
        Args:
            config: Project configuration
        """
        self.config = config
        self.logger = self._setup_logging()
        
    def _setup_logging(self) -> logging.Logger:
        """Configure logging system."""
        logger = logging.getLogger("llm_setup")
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(
            logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        )
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        return logger
        
    def create_directory_structure(self) -> None:
        """Create base directory structure."""
        directories = [
            "docs/adr",              # Architecture Decision Records
            "docs/methodology",       # Methodology documentation
            "docs/analysis",         # Technical analysis
            "docs/guides",          # Technical guides
            "src",                  # Source code
            "tests/unit",           # Unit tests
            "tests/integration",    # Integration tests
            "tools",               # Tools and scripts
            "examples"             # Example projects
        ]
        
        for dir_path in directories:
            Path(self.config.documentation_path / dir_path).mkdir(
                parents=True, exist_ok=True
            )
            
    def create_base_documentation(self) -> None:
        """Create base documentation files."""
        docs = {
            "README.md": self._generate_readme(),
            "llm_methodology.md": self._generate_methodology_doc(),
            "tools_integration.md": self._generate_tools_doc(),
            "tavily_integration.md": self._generate_tavily_doc(),
            "project_initialization.md": self._generate_initialization_doc(),
            "resume_prompt.md": self._generate_resume_doc()
        }
        
        for filename, content in docs.items():
            path = self.config.documentation_path / "docs/methodology" / filename
            path.write_text(content)
            
    def setup_tools_configuration(self) -> None:
        """Configure project tools."""
        tools_config = {
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
                    },
                    "implementation": {
                        "depth": "detailed",
                        "include_examples": True
                    }
                }
            },
            "mcp_tools": {
                "enabled": True,
                "auto_discovery": True
            }
        }
        
        config_path = self.config.documentation_path / "tools_config.json"
        config_path.write_text(json.dumps(tools_config, indent=2))
        
    def create_project_context(self) -> None:
        """Create initial project context."""
        context = {
            "project": {
                "name": self.config.name,
                "type": self.config.type,
                "technologies": self.config.technologies
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
        
        context_path = self.config.documentation_path / "docs/methodology/context.yaml"
        context_path.write_text(yaml.dump(context, indent=2))
        
    def setup_version_control(self) -> None:
        """Configure version control."""
        gitignore = """
        __pycache__/
        *.py[cod]
        *$py.class
        .env
        .venv
        .coverage
        htmlcov/
        .pytest_cache/
        """
        
        gitignore_path = self.config.documentation_path / ".gitignore"
        gitignore_path.write_text(gitignore.strip())
        
    def run(self) -> None:
        """Execute complete setup process."""
        try:
            self.logger.info("Starting LLM methodology setup...")
            
            self.create_directory_structure()
            self.logger.info("Directory structure created")
            
            self.create_base_documentation()
            self.logger.info("Base documentation created")
            
            self.setup_tools_configuration()
            self.logger.info("Tools configured")
            
            self.create_project_context()
            self.logger.info("Project context created")
            
            self.setup_version_control()
            self.logger.info("Version control configured")
            
            self.logger.info("Setup completed successfully")
            
        except Exception as e:
            self.logger.error(f"Error during setup: {str(e)}")
            raise

    def _generate_readme(self) -> str:
        """Generate project README."""
        return f"""# {self.config.name}

Project using Cline LLM Methodology.

## Overview

- Type: {self.config.type}
- Technologies: {', '.join(self.config.technologies)}

## Documentation

See the `docs/` directory for complete documentation:

- [LLM Methodology](docs/methodology/llm_methodology.md)
- [Tools Integration](docs/methodology/tools_integration.md)
- [Project Initialization](docs/methodology/project_initialization.md)

## Development

### Setup

```bash
# Install dependencies
poetry install

# Setup environment
poetry shell

# Run tests
pytest
```

### Structure

```
{self.config.name}/
├── docs/           # Documentation
├── src/           # Source code
├── tests/         # Tests
└── tools/         # Tools and scripts
```
"""

    def _generate_methodology_doc(self) -> str:
        """Generate methodology documentation."""
        return """# LLM Methodology

Structured approach for developing projects with LLM in VSCode using Cline.

## Core Principles

1. Structured Documentation
2. Tool Integration
3. Context Management
4. Iterative Development

## Components

1. Documentation Structure
2. Tool Configuration
3. Project Templates
4. Development Workflow

See individual component documentation for details.
"""

    def _generate_tools_doc(self) -> str:
        """Generate tools documentation."""
        return """# Tools Integration

Configuration and usage of integrated tools.

## Available Tools

1. Browser Action
2. Tavily AI
3. MCP Tools

## Configuration

See `tools_config.json` for detailed configuration.
"""

    def _generate_tavily_doc(self) -> str:
        """Generate Tavily AI documentation."""
        return """# Tavily AI Integration

Integration with Tavily AI for technical search and research.

## Configuration

See `tools_config.json` for search type configurations.

## Usage

Examples of common search patterns and best practices.
"""

    def _generate_initialization_doc(self) -> str:
        """Generate initialization documentation."""
        return """# Project Initialization

Guide for initializing new projects using the methodology.

## Steps

1. Configuration
2. Directory Setup
3. Tool Integration
4. Documentation

## Templates

Available project templates and their usage.
"""

    def _generate_resume_doc(self) -> str:
        """Generate resume documentation."""
        return """# Work Resumption

Guide for resuming work on projects.

## Context Management

How to maintain and restore context when resuming work.

## Tools

Using tools effectively for work continuation.
"""