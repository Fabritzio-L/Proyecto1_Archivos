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

    def cargar_configuracion(self):
        try:
            with open(self.archivo_final, "r", encoding="utf-8") as archivo:
                configuracion = json.load(archivo)
                print("Configuración cargada exitosamente")
                return configuracion
                
        except FileNotFoundError:
            print("Aviso: Archivo de configuración ausente. Cargando valores por defecto.")
            return self.configuracion_por_defecto.copy()
        except json.JSONDecodeError:
            print("Aviso: Archivo de configuración corrupto o con formato inválido. Cargando valores por defecto.")
            return self.configuracion_por_defecto.copy()
            
        except PermissionError:
            print("Error: Falta de permisos de lectura. Cargando valores por defecto.")
            return self.configuracion_por_defecto.copy()
            
        except Exception as e:
            print(f"Error al leer: {e}. Cargando valores por defecto.")
            return self.configuracion_por_defecto.copy()

    def guardar_configuracion(self, nuevos_datos):
        try:
            with open(self.archivo_temporal, "w", encoding="utf-8") as archivo:
                json.dump(nuevos_datos,
                        archivo,
                        indent=4, 
                        ensure_ascii=False)
            
            if os.path.exists(self.archivo_final):
                os.replace(self.archivo_final, self.archivo_respaldo)
                
            os.replace(self.archivo_temporal, self.archivo_final)
            print("Configuración guardada de manera segura")
            return True
            
        except PermissionError:
            print("Error: Falta de permisos de escritura. No se pudo guardar la configuración")
            if os.path.exists(self.archivo_temporal):
                try:
                    os.remove(self.archivo_temporal)
                except:
                    pass
            return False
            
        except Exception as e:
            print(f"Error inesperado al guardar {e}")
            return False