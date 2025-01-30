#!/bin/bash
# Setup script for cline-llm-methodology

set -e  # Exit on error

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m'  # No Color

echo -e "${BLUE}Setting up cline-llm-methodology...${NC}"

# Check Python version
REQUIRED_PYTHON="3.11"
PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')

if [[ "$(printf '%s\n' "$REQUIRED_PYTHON" "$PYTHON_VERSION" | sort -V | head -n1)" != "$REQUIRED_PYTHON" ]]; then
    echo -e "${RED}Error: Python $REQUIRED_PYTHON or higher is required (found $PYTHON_VERSION)${NC}"
    exit 1
fi

# Check if Poetry is installed
if ! command -v poetry &> /dev/null; then
    echo -e "${BLUE}Installing Poetry...${NC}"
    curl -sSL https://install.python-poetry.org | python3 -
fi

# Configure Poetry
echo -e "${BLUE}Configuring Poetry...${NC}"
poetry config virtualenvs.create true
poetry config virtualenvs.in-project true

# Install dependencies
echo -e "${BLUE}Installing dependencies...${NC}"
poetry install

# Initialize git if not already initialized
if [ ! -d ".git" ]; then
    echo -e "${BLUE}Initializing git repository...${NC}"
    git init
fi

# Setup pre-commit hooks
echo -e "${BLUE}Setting up pre-commit hooks...${NC}"
poetry run pre-commit install

# Create necessary directories if they don't exist
echo -e "${BLUE}Creating directory structure...${NC}"
directories=(
    "docs/adr"
    "docs/methodology"
    "src/llm_setup"
    "src/templates"
    "tests/unit"
    "tests/integration"
    "examples/api_h2h"
)

for dir in "${directories[@]}"; do
    mkdir -p "$dir"
done

# Create .env file if it doesn't exist
if [ ! -f ".env" ]; then
    echo -e "${BLUE}Creating .env file...${NC}"
    cp .env.example .env 2>/dev/null || echo "# Environment variables" > .env
fi

# Run tests to verify setup
echo -e "${BLUE}Running tests...${NC}"
poetry run pytest

# Final checks
echo -e "${BLUE}Performing final checks...${NC}"

# Check if all required files exist
required_files=(
    "pyproject.toml"
    "README.md"
    "LICENSE"
    ".gitignore"
    ".pre-commit-config.yaml"
    "pytest.ini"
)

missing_files=()
for file in "${required_files[@]}"; do
    if [ ! -f "$file" ]; then
        missing_files+=("$file")
    fi
done

if [ ${#missing_files[@]} -ne 0 ]; then
    echo -e "${RED}Warning: The following files are missing:${NC}"
    printf '%s\n' "${missing_files[@]}"
else
    echo -e "${GREEN}All required files are present${NC}"
fi

# Check if documentation exists
if [ ! -f "docs/methodology/llm_methodology.md" ]; then
    echo -e "${RED}Warning: Core methodology documentation is missing${NC}"
fi

# Check git configuration
if ! git config user.name > /dev/null || ! git config user.email > /dev/null; then
    echo -e "${RED}Warning: Git user configuration is incomplete${NC}"
    echo "Please configure git user.name and user.email:"
    echo "git config user.name \"Your Name\""
    echo "git config user.email \"your.email@example.com\""
fi

# Setup complete
echo -e "${GREEN}Setup complete!${NC}"
echo -e "${BLUE}Next steps:${NC}"
echo "1. Review and update .env file with your settings"
echo "2. Review documentation in docs/methodology/"
echo "3. Run 'poetry shell' to activate the virtual environment"
echo "4. Start development!"

# Make the script executable
chmod +x scripts/*.sh

exit 0