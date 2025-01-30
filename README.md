# Cline LLM Methodology

Metodología y herramientas para desarrollo de proyectos con LLM en VSCode usando Cline.

## Descripción

Este proyecto proporciona una metodología estructurada y herramientas automatizadas para el desarrollo de proyectos usando LLM (Large Language Models) en VSCode con Cline. La metodología incluye:

- Estructura de documentación estandarizada
- Integración de herramientas (Browser Action, Tavily AI, MCP Tools)
- Scripts de automatización
- Mejores prácticas y guías

## Instalación

```bash
pip install cline-llm-methodology
```

## Uso Rápido

```python
from cline_llm_methodology import setup_project

# Crear nuevo proyecto
setup_project("mi-proyecto", {
    "type": "api",
    "technologies": ["python", "fastapi"],
    "base_structure": "standard"
})
```

## Estructura del Proyecto

```
proyecto/
├── docs/
│   ├── adr/              # Architecture Decision Records
│   ├── prompt_llm/       # Documentación LLM
│   ├── analysis/         # Análisis técnicos
│   └── guides/          # Guías técnicas
├── src/                 # Código fuente
├── tests/              # Pruebas
└── tools/              # Herramientas y scripts
```

## Características

- 🚀 Setup automatizado de proyectos
- 📚 Documentación estructurada
- 🔧 Integración de herramientas
- 🧪 Testing incluido
- 📝 Plantillas predefinidas

## Documentación

La documentación completa está disponible en los siguientes archivos:

- [Metodología Base](docs/methodology/llm_methodology.md)
- [Integración de Herramientas](docs/methodology/tools_integration.md)
- [Uso de Tavily AI](docs/methodology/tavily_integration.md)
- [Inicialización de Proyectos](docs/methodology/project_initialization.md)

## Ejemplos

Revisa el directorio `examples/` para ver casos de uso reales:

- [API-H2H](examples/api_h2h/): Integración bancaria Host-to-Host

## Desarrollo

### Requisitos

- Python 3.11.11
- Poetry
- Git

### Setup

```bash
# Clonar repositorio
git clone https://github.com/jivagrisma/cline-llm-methodology.git
cd cline-llm-methodology

# Instalar dependencias
poetry install

# Activar entorno virtual
poetry shell

# Ejecutar tests
pytest
```

## Contribución

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/amazing-feature`)
3. Commit tus cambios (`git commit -m 'Add amazing feature'`)
4. Push a la rama (`git push origin feature/amazing-feature`)
5. Abre un Pull Request

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## Créditos

Esta metodología fue desarrollada inicialmente como parte del proyecto API-H2H, donde se implementó y validó en un caso real de integración bancaria.

## Última Actualización

- **Fecha**: 30/01/2025
- **Versión**: 1.0.0
- **Estado**: Activo