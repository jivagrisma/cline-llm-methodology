# Guía de Inicio Rápido

Esta guía te ayudará a comenzar con la Metodología Cline LLM en minutos.

## Instalación Rápida

```bash
# Instalar el paquete
pip install cline-llm-methodology

# Verificar instalación
llm-setup --version
```

## Crear Nuevo Proyecto

### 1. Inicializar Proyecto

```bash
# Crear nuevo proyecto
llm-setup init

# Seguir el asistente interactivo para configurar:
# - Nombre del proyecto
# - Tipo de proyecto
# - Tecnologías a utilizar
```

### 2. Configuración Básica

```bash
# Copiar archivo de ejemplo
cp .env.example .env

# Editar configuración
# - DEBUG=false
# - LOG_LEVEL=INFO
```

### 3. Verificar Configuración

```bash
# Validar configuración
llm-setup validate
```

## Primeros Pasos

### 1. Estructura del Proyecto

Tu proyecto tendrá esta estructura:

```
mi-proyecto/
├── docs/               # Documentación
├── src/               # Código fuente
├── tests/             # Pruebas
└── tools/             # Herramientas
```

### 2. Comandos Básicos

```bash
# Ver ayuda
llm-setup --help

# Validar proyecto
llm-setup validate

# Ejecutar pruebas
pytest
```

## Ejemplos Prácticos

### 1. Crear Documentación

```bash
# Generar estructura de documentación
llm-setup docs init

# Generar sitio de documentación
mkdocs serve
```

### 2. Integrar Herramientas

```python
# En tu código
from cline_llm_methodology import setup

# Configurar proyecto
config = setup.ProjectConfig(
    name="mi-proyecto",
    type="api",
    technologies=["python", "fastapi"]
)

# Inicializar setup
setup_manager = setup.LLMMethodologySetup(config)
setup_manager.run()
```

### 3. Usar Browser Action

```python
from cline_llm_methodology.tools import browser

# Lanzar navegador
browser.launch("http://localhost:3000")

# Realizar acciones
browser.click(450, 300)
browser.type("Texto de prueba")
```

## Flujo de Trabajo Recomendado

1. **Planificación**
   - Definir objetivos del proyecto
   - Identificar tecnologías necesarias
   - Establecer estructura base

2. **Desarrollo**
   - Seguir metodología LLM
   - Usar herramientas integradas
   - Mantener documentación actualizada

3. **Pruebas**
   - Ejecutar pruebas unitarias
   - Validar integración
   - Verificar documentación

4. **Despliegue**
   - Validar configuración
   - Generar documentación
   - Desplegar cambios

## Mejores Prácticas

1. **Documentación**
   - Mantener README actualizado
   - Documentar decisiones (ADRs)
   - Incluir ejemplos prácticos

2. **Código**
   - Seguir estándares de código
   - Usar tipos estáticos
   - Mantener cobertura de pruebas

3. **Herramientas**
   - Configurar pre-commit hooks
   - Usar validación automática
   - Mantener dependencias actualizadas

## Solución Rápida de Problemas

### Error: Comando no encontrado
```bash
# Verificar instalación
pip list | grep cline-llm-methodology

# Reinstalar si es necesario
pip install --force-reinstall cline-llm-methodology
```

### Error: Fallo en validación
```bash
# Verificar configuración
llm-setup validate --verbose

# Corregir problemas reportados
llm-setup fix
```

## Siguientes Pasos

1. Lee la [Documentación Completa](../methodology/llm_methodology.md)
2. Explora los [Ejemplos](../examples/api_h2h.md)
3. Únete a la [Comunidad](https://discord.gg/cline-community)

## Recursos Adicionales

- [Documentación Detallada](https://jivagrisma.github.io/cline-llm-methodology)
- [Repositorio GitHub](https://github.com/jivagrisma/cline-llm-methodology)
- [Canal de Discord](https://discord.gg/cline-community)