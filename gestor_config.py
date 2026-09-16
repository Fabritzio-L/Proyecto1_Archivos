import json
import os

class GestorConfiguracion:
    def __init__(self):
        self.archivo_final = "config.json"
        self.archivo_temporal = "config.tmp"
        self.archivo_respaldo = "config.bak"

        # Valores por defecto
        self.configuracion_por_defecto = {
            "nombre_usuario": "Usuario Predeterminado",
            "tema": "claro",
            "idioma": "es/es-ES",
            "tamano_fuente": 12,
            "color_menu": "#ffffff",
            "color_letra": "#000000",
            "ruta_foto": ""
        }

