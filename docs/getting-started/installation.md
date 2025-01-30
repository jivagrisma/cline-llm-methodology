# Guía de Instalación

Esta guía te ayudará a instalar y configurar la Metodología Cline LLM en tu entorno de desarrollo.

## Requisitos Previos

- Python 3.11 o superior
- pip o poetry para gestión de paquetes
- Git (opcional, pero recomendado)
- VSCode con la extensión Cline instalada

## Instalación

### Usando pip

```bash
# Instalar el paquete
pip install cline-llm-methodology

# Verificar la instalación
llm-setup --version
```

### Usando Poetry

```bash
# Crear nuevo proyecto
poetry new mi-proyecto
cd mi-proyecto

# Agregar dependencia
poetry add cline-llm-methodology

# Activar entorno virtual
poetry shell
```

### Desde el Código Fuente

```bash
# Clonar repositorio
git clone https://github.com/jivagrisma/cline-llm-methodology.git
cd cline-llm-methodology

# Instalar dependencias
poetry install

# Instalar en modo desarrollo
poetry install --develop
```

## Configuración

### 1. Configuración del Entorno

Crea un archivo `.env` basado en el ejemplo proporcionado:

```bash
cp .env.example .env
```

Edita el archivo `.env` con tus configuraciones:

```ini
# Configuración básica
DEBUG=false
LOG_LEVEL=INFO

# Configuración de herramientas
BROWSER_RESOLUTION=900x600
TAVILY_API_KEY=your-api-key-here
```

### 2. Configuración de VSCode

1. Instala la extensión Cline desde el marketplace de VSCode
2. Abre la configuración de VSCode (Ctrl+,)
3. Busca "Cline" y configura:
   - MCP Tools: Enabled
   - Browser Action: Enabled

### 3. Configuración de Pre-commit Hooks

```bash
# Instalar pre-commit
pip install pre-commit

# Instalar hooks
pre-commit install

# Ejecutar hooks en todos los archivos
pre-commit run --all-files
```

## Verificación

Verifica que todo esté correctamente instalado:

```bash
# Verificar CLI
llm-setup --help

# Verificar configuración
llm-setup validate

# Ejecutar pruebas
pytest
```

## Estructura del Proyecto

Después de la instalación, tu proyecto debería tener esta estructura:

```
mi-proyecto/
├── docs/
│   ├── adr/
│   └── methodology/
├── src/
├── tests/
│   ├── unit/
│   └── integration/
└── tools/
```

## Solución de Problemas

### Error: Command 'llm-setup' not found

Asegúrate de que:
1. El paquete está instalado (`pip list | grep cline-llm-methodology`)
2. El directorio de scripts de Python está en tu PATH
3. El entorno virtual está activado (si usas uno)

### Error: No se pueden importar módulos

Verifica que:
1. Estás en el directorio correcto
2. El entorno virtual está activado
3. Todas las dependencias están instaladas

### Error: Fallo en pre-commit hooks

1. Actualiza pre-commit: `pre-commit autoupdate`
2. Limpia la caché: `pre-commit clean`
3. Reinstala los hooks: `pre-commit install`

## Siguientes Pasos

1. Lee la [Guía de Inicio Rápido](quick-start.md)
2. Revisa la [Documentación de la Metodología](../methodology/llm_methodology.md)
3. Explora los [Ejemplos](../examples/api_h2h.md)

## Recursos Adicionales

- [Documentación de Cline](https://cline.readthedocs.io/)
- [Repositorio en GitHub](https://github.com/jivagrisma/cline-llm-methodology)
- [Canal de Discord](https://discord.gg/cline-community)

## Soporte

Si encuentras problemas durante la instalación:

1. Revisa las [Issues conocidas](https://github.com/jivagrisma/cline-llm-methodology/issues)
2. Busca en las [Discusiones](https://github.com/jivagrisma/cline-llm-methodology/discussions)
3. Abre una nueva issue si el problema persiste