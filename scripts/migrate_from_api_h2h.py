#!/usr/bin/env python3
"""
Script para migrar desde el proyecto API-H2H a la estructura de Cline LLM Methodology.
"""

import os
import shutil
import json
from pathlib import Path
import logging
from typing import Dict, List, Optional

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class MigrationConfig:
    """Configuración de la migración."""
    
    def __init__(self, source_dir: str, target_dir: str):
        self.source_dir = Path(source_dir)
        self.target_dir = Path(target_dir)
        self.docs_mapping = {
            "adr": "docs/adr",
            "migration": "docs/migration",
            "prompt_llm": "docs/methodology",
            "analysis": "docs/analysis",
            "guides": "docs/guides"
        }
        self.test_mapping = {
            "unit": "tests/unit",
            "integration": "tests/integration",
            "xml": "tests/xml"
        }

class MigrationTool:
    """Herramienta para migrar el proyecto."""
    
    def __init__(self, config: MigrationConfig):
        self.config = config
        self.errors: List[str] = []
        self.warnings: List[str] = []

    def validate_source(self) -> bool:
        """Validar directorio fuente."""
        if not self.config.source_dir.exists():
            self.errors.append(f"Directorio fuente no existe: {self.config.source_dir}")
            return False
        
        required_files = ["pyproject.toml", "src", "tests"]
        for file in required_files:
            if not (self.config.source_dir / file).exists():
                self.errors.append(f"Archivo/directorio requerido no encontrado: {file}")
                return False
        
        return True

    def prepare_target(self) -> bool:
        """Preparar directorio destino."""
        try:
            self.config.target_dir.mkdir(parents=True, exist_ok=True)
            return True
        except Exception as e:
            self.errors.append(f"Error preparando directorio destino: {e}")
            return False

    def migrate_docs(self) -> bool:
        """Migrar documentación."""
        try:
            source_docs = self.config.source_dir / "docs"
            if not source_docs.exists():
                self.warnings.append("No se encontró directorio de documentación")
                return True

            for source, target in self.config.docs_mapping.items():
                source_path = source_docs / source
                target_path = self.config.target_dir / target
                
                if source_path.exists():
                    target_path.mkdir(parents=True, exist_ok=True)
                    shutil.copytree(source_path, target_path, dirs_exist_ok=True)
                    logger.info(f"Migrada documentación: {source} -> {target}")
            
            return True
        except Exception as e:
            self.errors.append(f"Error migrando documentación: {e}")
            return False

    def migrate_tests(self) -> bool:
        """Migrar pruebas."""
        try:
            source_tests = self.config.source_dir / "tests"
            if not source_tests.exists():
                self.warnings.append("No se encontró directorio de pruebas")
                return True

            for source, target in self.config.test_mapping.items():
                source_path = source_tests / source
                target_path = self.config.target_dir / target
                
                if source_path.exists():
                    target_path.mkdir(parents=True, exist_ok=True)
                    shutil.copytree(source_path, target_path, dirs_exist_ok=True)
                    logger.info(f"Migradas pruebas: {source} -> {target}")
            
            return True
        except Exception as e:
            self.errors.append(f"Error migrando pruebas: {e}")
            return False

    def migrate_source(self) -> bool:
        """Migrar código fuente."""
        try:
            source_src = self.config.source_dir / "src"
            target_src = self.config.target_dir / "src"
            
            if not source_src.exists():
                self.errors.append("No se encontró directorio src")
                return False

            target_src.mkdir(parents=True, exist_ok=True)
            shutil.copytree(source_src, target_src, dirs_exist_ok=True)
            logger.info("Migrado código fuente")
            
            return True
        except Exception as e:
            self.errors.append(f"Error migrando código fuente: {e}")
            return False

    def migrate_config(self) -> bool:
        """Migrar archivos de configuración."""
        try:
            config_files = [
                "pyproject.toml",
                "pytest.ini",
                ".env.example",
                ".gitignore",
                "README.md"
            ]
            
            for file in config_files:
                source_file = self.config.source_dir / file
                target_file = self.config.target_dir / file
                
                if source_file.exists():
                    shutil.copy2(source_file, target_file)
                    logger.info(f"Migrado archivo de configuración: {file}")
            
            return True
        except Exception as e:
            self.errors.append(f"Error migrando configuración: {e}")
            return False

    def update_dependencies(self) -> bool:
        """Actualizar dependencias en pyproject.toml."""
        try:
            pyproject_path = self.config.target_dir / "pyproject.toml"
            if not pyproject_path.exists():
                self.errors.append("No se encontró pyproject.toml")
                return False

            with open(pyproject_path, 'r') as f:
                content = f.read()

            # Agregar nuevas dependencias
            new_deps = {
                "cline-llm-methodology": "^1.0.0",
                "mkdocs": "^1.5.0",
                "mkdocs-material": "^9.0.0"
            }

            # TODO: Parsear y actualizar TOML correctamente
            # Por ahora solo agregamos un comentario
            with open(pyproject_path, 'a') as f:
                f.write("\n# TODO: Agregar dependencias de Cline LLM Methodology:\n")
                for dep, ver in new_deps.items():
                    f.write(f"# {dep} = \"{ver}\"\n")

            return True
        except Exception as e:
            self.errors.append(f"Error actualizando dependencias: {e}")
            return False

    def create_migration_report(self) -> Dict:
        """Crear reporte de migración."""
        return {
            "success": len(self.errors) == 0,
            "errors": self.errors,
            "warnings": self.warnings,
            "source": str(self.config.source_dir),
            "target": str(self.config.target_dir),
            "timestamp": str(Path.ctime(Path.cwd()))
        }

    def run(self) -> bool:
        """Ejecutar migración completa."""
        steps = [
            ("Validando fuente", self.validate_source),
            ("Preparando destino", self.prepare_target),
            ("Migrando documentación", self.migrate_docs),
            ("Migrando pruebas", self.migrate_tests),
            ("Migrando código fuente", self.migrate_source),
            ("Migrando configuración", self.migrate_config),
            ("Actualizando dependencias", self.update_dependencies)
        ]

        success = True
        for desc, step in steps:
            logger.info(f"Iniciando: {desc}")
            if not step():
                success = False
                logger.error(f"Error en: {desc}")
                break
            logger.info(f"Completado: {desc}")

        report = self.create_migration_report()
        report_path = self.config.target_dir / "migration_report.json"
        
        with open(report_path, 'w') as f:
            json.dump(report, f, indent=2)

        return success

def main():
    """Función principal."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Migrar proyecto API-H2H a Cline LLM Methodology"
    )
    parser.add_argument(
        "source",
        help="Directorio del proyecto API-H2H"
    )
    parser.add_argument(
        "target",
        help="Directorio destino para el nuevo proyecto"
    )
    
    args = parser.parse_args()
    
    config = MigrationConfig(args.source, args.target)
    tool = MigrationTool(config)
    
    if tool.run():
        logger.info("Migración completada exitosamente")
        return 0
    else:
        logger.error("La migración falló")
        return 1

if __name__ == "__main__":
    exit(main())