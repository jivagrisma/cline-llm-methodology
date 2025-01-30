# Cline LLM Methodology

Herramientas de automatización y metodología para el desarrollo de proyectos usando LLM en VSCode con Cline.

## Descripción General

La Metodología Cline LLM proporciona un conjunto estructurado de herramientas y prácticas para:

- Automatizar la configuración de proyectos
- Integrar herramientas de desarrollo
- Gestionar el contexto del proyecto
- Facilitar el desarrollo iterativo
- Mantener la consistencia en la documentación

## Características Principales

### 🚀 Configuración Automatizada

```bash
# Iniciar nuevo proyecto
llm-setup init

# Configurar proyecto existente
llm-setup setup config.json
```

### 🔧 Integración de Herramientas

- Browser Action para pruebas de interfaz
- Tavily AI para búsqueda técnica
- MCP Tools para extensibilidad

### 📝 Gestión de Documentación

- Generación automática de estructura
- Plantillas predefinidas
- Integración con MkDocs

### 🔄 Desarrollo Iterativo

- Flujo de trabajo estructurado
- Validación continua
- Pruebas automatizadas

## Instalación

```bash
# Usando pip
pip install cline-llm-methodology

# Usando poetry
poetry add cline-llm-methodology
```

## Inicio Rápido

1. Crear nuevo proyecto:
```bash
llm-setup init
```

2. Configurar el proyecto:
```bash
llm-setup setup config.json
```

3. Iniciar desarrollo:
```bash
llm-setup validate
```

## Estructura del Proyecto

```
proyecto/
├── docs/               # Documentación
│   ├── adr/           # Decisiones de arquitectura
│   └── methodology/   # Documentación de metodología
├── src/               # Código fuente
├── tests/             # Pruebas
└── tools/             # Herramientas y scripts
```

## Ejemplos

Consulta el directorio `examples/` para ver implementaciones de referencia:

- [API-H2H](examples/api_h2h.md): Implementación de referencia original
- [Más ejemplos próximamente...]

## Contribuir

¡Las contribuciones son bienvenidas! Por favor, revisa nuestra [guía de contribución](contributing/guidelines.md).

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo [LICENSE](https://github.com/jivagrisma/cline-llm-methodology/blob/main/LICENSE) para más detalles.

## Soporte

- 📚 [Documentación](https://jivagrisma.github.io/cline-llm-methodology)
- 💬 [Discusiones](https://github.com/jivagrisma/cline-llm-methodology/discussions)
- 🐛 [Issues](https://github.com/jivagrisma/cline-llm-methodology/issues)

## Estado del Proyecto

![Tests](https://github.com/jivagrisma/cline-llm-methodology/workflows/CI/badge.svg)
![PyPI version](https://badge.fury.io/py/cline-llm-methodology.svg)
![License](https://img.shields.io/github/license/jivagrisma/cline-llm-methodology)
![Python versions](https://img.shields.io/pypi/pyversions/cline-llm-methodology.svg)

## Agradecimientos

- Equipo de Cline por la plataforma base
- Contribuidores del proyecto API-H2H por la implementación inicial
- Comunidad de desarrolladores por su retroalimentación y sugerencias