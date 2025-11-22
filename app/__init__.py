"""
Paquete de la aplicacion.
Exporta la instancia `app` para facilitar imports en tests.
"""
from .app import app  # re-exportar la app Flask como `app`

__all__ = ["app"]
