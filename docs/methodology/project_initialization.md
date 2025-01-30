# Inicialización de Proyectos

Esta guía detalla el proceso de inicialización de proyectos usando la Metodología Cline LLM.

## Estructura Base

```
proyecto/
├── docs/               # Documentación
│   ├── adr/           # Architecture Decision Records
│   ├── methodology/   # Documentación de metodología
│   ├── analysis/      # Análisis técnicos
│   └── guides/        # Guías técnicas
├── src/               # Código fuente
├── tests/             # Pruebas
│   ├── unit/         # Pruebas unitarias
│   └── integration/  # Pruebas de integración
└── tools/            # Herramientas y scripts
```

## Proceso de Inicialización

### 1. Crear Proyecto

```bash
# Usando CLI
llm-setup init

# Seguir asistente interactivo
Project name: mi-proyecto
Project type: [api/web/cli/library]
Technologies: python,fastapi
Base structure: [standard/minimal]
```

### 2. Configuración Base

```bash
# Copiar configuración de ejemplo
cp .env.example .env

# Editar configuración
DEBUG=false
LOG_LEVEL=INFO
PROJECT_NAME=mi-proyecto
```

### 3. Estructura de Documentación

#### Architecture Decision Records (ADRs)

```markdown
# docs/adr/001-initial-setup.md

# 1. Configuración Inicial

Fecha: 2025-01-30

## Estado

Aceptado

## Contexto

Necesitamos establecer la estructura base del proyecto.

## Decisión

Usar la estructura estándar de la Metodología Cline LLM.

## Consecuencias

- Estructura consistente
- Fácil mantenimiento
- Documentación clara
```

#### Documentación de Metodología

```markdown
# docs/methodology/overview.md

# Visión General

Este proyecto sigue la Metodología Cline LLM para:
- Desarrollo guiado por contexto
- Integración de herramientas
- Documentación continua
```

## Configuración de Herramientas

### 1. Browser Action

```json
// tools_config.json
{
  "browser_action": {
    "resolution": "900x600",
    "screenshots_enabled": true
  }
}
```

### 2. Tavily AI

```json
{
  "tavily_ai": {
    "search_types": {
      "technical": {
        "depth": "comprehensive"
      }
    }
  }
}
```

### 3. MCP Tools

```json
{
  "mcp_tools": {
    "enabled": true,
    "auto_discovery": true
  }
}
```

## Configuración de Desarrollo

### 1. Pre-commit Hooks

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
```

### 2. Pytest

```ini
# pytest.ini
[pytest]
testpaths = tests
python_files = test_*.py
addopts = -v --cov=src
```

### 3. VSCode

```json
// .vscode/settings.json
{
  "python.testing.pytestEnabled": true,
  "python.linting.enabled": true
}
```

## Integración Continua

### GitHub Actions

```yaml
# .github/workflows/ci.yml
name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Test
        run: pytest
```

## Validación

### 1. Estructura

```bash
# Verificar estructura
llm-setup validate

# Verificar documentación
llm-setup validate --docs
```

### 2. Configuración

```bash
# Verificar configuración
llm-setup config check

# Verificar herramientas
llm-setup tools check
```

## Mejores Prácticas

### 1. Documentación

- Mantener ADRs actualizados
- Documentar decisiones importantes
- Incluir ejemplos prácticos

### 2. Código

- Seguir estándares de código
- Escribir pruebas unitarias
- Mantener cobertura alta

### 3. Herramientas

- Configurar pre-commit hooks
- Usar validación automática
- Mantener dependencias actualizadas

## Solución de Problemas

### 1. Problemas Comunes

```bash
# Error: Estructura inválida
llm-setup fix structure

# Error: Configuración inválida
llm-setup fix config

# Error: Herramientas no disponibles
llm-setup tools install
```

### 2. Verificación

```bash
# Verificar estado
llm-setup status

# Verificar herramientas
llm-setup tools status

# Verificar documentación
llm-setup docs status
```

## Siguientes Pasos

1. Revisar [Metodología LLM](llm_methodology.md)
2. Configurar [Herramientas](tools_integration.md)
3. Explorar [Ejemplos](../examples/api_h2h.md)

## Recursos

### Documentación

- [Guía de Instalación](../getting-started/installation.md)
- [Configuración](../getting-started/configuration.md)
- [Ejemplos](../examples/api_h2h.md)

### Herramientas

- [Browser Action](../tools/browser.md)
- [Tavily AI](../tools/tavily.md)
- [MCP Tools](../tools/mcp.md)

### Referencias

- [API Reference](../reference/api.md)
- [CLI Reference](../reference/cli.md)
- [Configuration Reference](../reference/configuration.md)