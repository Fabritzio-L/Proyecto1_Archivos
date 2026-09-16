import tkinter as tk
from tkinter import ttk, colorchooser, filedialog, messagebox
from gestor_config import GestorConfiguracion

class AplicacionPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Proyecto 1 - Manejo de Archivos")
        self.geometry("600x400")
        
        self.gestor = GestorConfiguracion()
        
        self.config_actual = self.gestor.cargar_configuracion()
        
        self.lbl_bienvenida = tk.Label(self, text=f"Bienvenido, {self.config_actual['nombre_usuario']}", font=("Arial", 14))
        self.lbl_bienvenida.pack(expand=True)

        self.crear_menus()

    def crear_menus(self):
        barra_menu = tk.Menu(self)

        menu_archivo = tk.Menu(barra_menu, tearoff=0)
        menu_archivo.add_command(label="Nuevo")
        menu_archivo.add_command(label="Abrir")
        menu_archivo.add_separator()
        menu_archivo.add_command(label="Salir", command=self.quit)
        barra_menu.add_cascade(label="Archivo", menu=menu_archivo)

        menu_edicion = tk.Menu(barra_menu, tearoff=0)
        menu_edicion.add_command(label="Copiar")
        menu_edicion.add_command(label="Pegar")
        barra_menu.add_cascade(label="Edición", menu=menu_edicion)

        menu_ver = tk.Menu(barra_menu, tearoff=0)
        menu_ver.add_command(label="Aumentar")
        menu_ver.add_command(label="Alejar")
        barra_menu.add_cascade(label="Ver", menu=menu_ver)

        menu_settings = tk.Menu(barra_menu, tearoff=0)
        menu_settings.add_command(label="Abrir Configuraciones", command=self.abrir_settings)
        barra_menu.add_cascade(label="Configuraciones", menu=menu_settings)

        self.config(menu=barra_menu)

    def abrir_settings(self):
        VentanaSettings(self, self.gestor, self.config_actual)
        
    def actualizar_interfaz(self):
        self.lbl_bienvenida.config(text=f"Bienvenido, {self.config_actual["nombre_usuario"]}")


class VentanaSettings(tk.Toplevel):
    def __init__(self, parent, gestor, config_actual):
        super().__init__(parent)
        self.parent = parent
        self.gestor = gestor
        self.title("Configuración de Usuario")
        self.geometry("450x400")
        self.resizable(False, False)
        self.grab_set() 
        
        self.var_nombre = tk.StringVar(value=config_actual.get("nombre_usuario", ""))
        self.var_tema = tk.StringVar(value=config_actual.get("tema", "claro"))
        self.var_idioma = tk.StringVar(value=config_actual.get("idioma", "es/es-ES"))
        self.var_fuente = tk.IntVar(value=config_actual.get("tamano_fuente", 12))
        
        self.color_menu_hex = config_actual.get("color_menu", "#ffffff")
        self.color_letra_hex = config_actual.get("color_letra", "#000000")
        self.ruta_foto = config_actual.get("ruta_foto", "")

        self.crear_widgets()

    def crear_widgets(self):
        marco = ttk.Frame(self, padding=20)
        marco.pack(fill=tk.BOTH, expand=True)

        ttk.Label(marco, text="Nombre de usuario:").grid(row=0, column=0, sticky=tk.W, pady=5)
        ttk.Entry(marco, textvariable=self.var_nombre, width=30).grid(row=0, column=1, pady=5, sticky=tk.W)

        ttk.Label(marco, text="Tema interfaz:").grid(row=1, column=0, sticky=tk.W, pady=5)
        combo_tema = ttk.Combobox(marco, textvariable=self.var_tema, values=["claro", "oscuro"], state="readonly")
        combo_tema.grid(row=1, column=1, pady=5, sticky=tk.W)

        ttk.Label(marco, text="Idioma:").grid(row=2, column=0, sticky=tk.W, pady=5)
        combo_idioma = ttk.Combobox(marco, textvariable=self.var_idioma, values=["es/es-ES", "en/en-US"], state="readonly")
        combo_idioma.grid(row=2, column=1, pady=5, sticky=tk.W)

        ttk.Label(marco, text="Tamaño fuente:").grid(row=3, column=0, sticky=tk.W, pady=5)
        ttk.Spinbox(marco, from_=8, to=72, textvariable=self.var_fuente, width=10).grid(row=3, column=1, pady=5, sticky=tk.W)

        ttk.Label(marco, text="Color barra menú:").grid(row=4, column=0, sticky=tk.W, pady=5)
        self.btn_color_menu = ttk.Button(marco, text=self.color_menu_hex, command=self.elegir_color_menu)
        self.btn_color_menu.grid(row=4, column=1, pady=5, sticky=tk.W)

        ttk.Label(marco, text="Color de letra:").grid(row=5, column=0, sticky=tk.W, pady=5)
        self.btn_color_letra = ttk.Button(marco, text=self.color_letra_hex, command=self.elegir_color_letra)
        self.btn_color_letra.grid(row=5, column=1, pady=5, sticky=tk.W)

        ttk.Label(marco, text="Foto de perfil:").grid(row=6, column=0, sticky=tk.W, pady=5)
        self.btn_foto = ttk.Button(marco, text="Seleccionar Imagen", command=self.elegir_foto)
        self.btn_foto.grid(row=6, column=1, pady=5, sticky=tk.W)
        
        texto_ruta = self.ruta_foto.split("/")[-1] if self.ruta_foto else "Sin seleccionar..."
        self.lbl_ruta_foto = ttk.Label(marco, text=texto_ruta, foreground="gray")
        self.lbl_ruta_foto.grid(row=7, column=1, sticky=tk.W)

        ttk.Separator(marco, orient=tk.HORIZONTAL).grid(row=8, column=0, columnspan=2, sticky="ew", pady=15)
        btn_guardar = ttk.Button(marco, text="Guardar Configuración", command=self.guardar_configuracion)
        btn_guardar.grid(row=9, column=0, columnspan=2)

    def elegir_color_menu(self):
        color = colorchooser.askcolor(title="Selecciona el color del menú")
        if color[1]:
            self.color_menu_hex = color[1]
            self.btn_color_menu.config(text=self.color_menu_hex)

    def elegir_color_letra(self):
        color = colorchooser.askcolor(title="Selecciona el color de la letra")
        if color[1]:
            self.color_letra_hex = color[1]
            self.btn_color_letra.config(text=self.color_letra_hex)

    def elegir_foto(self):
        ruta = filedialog.askopenfilename(
            title="Seleccionar foto de perfil",
            filetypes=[("Imágenes", "*.png *.jpg *.jpeg"), ("Todos los archivos", "*.*")]
        )
        if ruta:
            self.ruta_foto = ruta
            self.lbl_ruta_foto.config(text=ruta.split("/")[-1])

    def guardar_configuracion(self):
        nuevos_datos = {
            "nombre_usuario": self.var_nombre.get(),
            "tema": self.var_tema.get(),
            "idioma": self.var_idioma.get(),
            "tamano_fuente": self.var_fuente.get(),
            "color_menu": self.color_menu_hex,
            "color_letra": self.color_letra_hex,
            "ruta_foto": self.ruta_foto
        }
        
        exito = self.gestor.guardar_configuracion(nuevos_datos)
        
        if exito:
            self.parent.config_actual = nuevos_datos
            self.parent.actualizar_interfaz()
            messagebox.showinfo("Éxito", "Configuración guardada de manera segura.")
            self.destroy()
        else:
            messagebox.showerror("Error", "No se pudo guardar la configuración. Revisa los permisos.")
