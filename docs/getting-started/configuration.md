# Guía de Configuración

Esta guía detalla todas las opciones de configuración disponibles en la Metodología Cline LLM.

## Configuración del Proyecto

### Archivo .env

El archivo `.env` contiene la configuración principal del proyecto:

```ini
# Configuración Básica
DEBUG=false
LOG_LEVEL=INFO
LOG_FORMAT=json
PROJECT_NAME=mi-proyecto
PROJECT_VERSION=1.0.0

# Configuración de Herramientas
BROWSER_RESOLUTION=900x600
SCREENSHOTS_ENABLED=true
CONSOLE_LOGS_ENABLED=true

# Configuración de MCP
MCP_TOOLS_ENABLED=true
MCP_AUTO_DISCOVERY=true
```

### Configuración por Ambiente

Se pueden tener diferentes configuraciones por ambiente:

- `.env.base`: Configuración base compartida
- `.env.development`: Desarrollo local
- `.env.test`: Pruebas automatizadas
- `.env.production`: Producción

## Herramientas

### Browser Action

```ini
# Configuración del navegador
BROWSER_RESOLUTION=900x600
SCREENSHOTS_ENABLED=true
CONSOLE_LOGS_ENABLED=true
BROWSER_HEADLESS=false
BROWSER_TIMEOUT=30000
```

### Tavily AI

```ini
# Configuración de búsqueda
TAVILY_API_KEY=your-api-key-here
TAVILY_SEARCH_DEPTH=comprehensive
TAVILY_INCLUDE_CODE=true
TAVILY_MAX_RESULTS=10
```

### MCP Tools

```ini
# Configuración de MCP
MCP_TOOLS_ENABLED=true
MCP_AUTO_DISCOVERY=true
MCP_CONFIG_PATH=/path/to/config
MCP_ALLOW_EXTERNAL=false
```

## Documentación

### MkDocs

```yaml
# mkdocs.yml
site_name: Mi Proyecto
theme:
  name: material
  features:
    - navigation.tabs
    - search.suggest
```

### Generación de Documentación

```ini
# Configuración de documentación
DOCS_OUTPUT_DIR=site
DOCS_THEME=material
DOCS_STRICT=true
DOCS_VERBOSE=true
```

## Testing

### Pytest

```ini
# pytest.ini
[pytest]
testpaths = tests
python_files = test_*.py
addopts = -v --cov=src
```

### Cobertura

```ini
# Configuración de cobertura
COVERAGE_REPORT_DIR=coverage_html
COVERAGE_FAIL_UNDER=80
COVERAGE_INCLUDE=src/*
COVERAGE_EXCLUDE=tests/*
```

## CI/CD

### GitHub Actions

```yaml
# Configuración de CI
CI_PYTHON_VERSION=3.11
CI_COVERAGE_THRESHOLD=80
CI_LINT_ENABLED=true
CI_TEST_PARALLEL=true
```

### Pre-commit

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
```

## Seguridad

```ini
# Configuración de seguridad
VALIDATE_TOOL_INPUTS=true
ALLOW_EXTERNAL_TOOLS=false
MAX_FILE_SIZE_MB=10
SECURE_MODE=true
```

## Rendimiento

```ini
# Límites de recursos
MAX_MEMORY_MB=512
MAX_PROCESS_TIME_SEC=300
CACHE_TTL=3600
CACHE_DIR=.cache
```

## Personalización

### Templates

```ini
# Directorios de plantillas
TEMPLATES_DIR=src/templates
EXAMPLES_DIR=examples
MIGRATIONS_DIR=migrations
```

### Feature Flags

```ini
# Características experimentales
ENABLE_EXPERIMENTAL=false
STRICT_MODE=true
DEBUG_TOOLS=false
```

## Validación de Configuración

### Usando CLI

```bash
# Validar configuración
llm-setup validate

# Validar con detalles
llm-setup validate --verbose

# Validar ambiente específico
llm-setup validate --env production
```

### Programáticamente

```python
from cline_llm_methodology.config import validate_config

# Validar configuración
result = validate_config()
if not result.is_valid:
    print(f"Errores: {result.errors}")
```

## Resolución de Problemas

### Problemas Comunes

1. **Error: Variable de entorno no encontrada**
   ```bash
   # Verificar variables
   llm-setup config check
   
   # Generar .env faltante
   llm-setup config init
   ```

2. **Error: Configuración inválida**
   ```bash
   # Ver detalles del error
   llm-setup validate --verbose
   
   # Arreglar automáticamente
   llm-setup fix
   ```

3. **Error: Conflicto de configuración**
   ```bash
   # Ver conflictos
   llm-setup config diff
   
   # Resolver automáticamente
   llm-setup config resolve
   ```

## Mejores Prácticas

1. **Seguridad**
   - No versionar archivos .env
   - Usar variables de entorno en CI/CD
   - Validar inputs de herramientas

2. **Mantenimiento**
   - Documentar cambios de configuración
   - Mantener valores por defecto seguros
   - Revisar configuración periódicamente

3. **Desarrollo**
   - Usar diferentes configs por ambiente
   - Mantener documentación actualizada
   - Validar antes de desplegar