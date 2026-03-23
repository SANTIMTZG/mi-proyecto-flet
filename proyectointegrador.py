import flet as ft
import os  # VITAL: Para que Render asigne el puerto de red correctamente

# =========================
# MODELO DE DATOS
# =========================
productos = [
    {"id": 1, "nombre": "Laptop Gamer", "descripcion": "Laptop potente", "precio": 25000, "ruta_imagen": "laptop.png"},
    {"id": 2, "nombre": "Smartphone", "descripcion": "Teléfono moderno", "precio": 15000, "ruta_imagen": "telefono.png"},
    {"id": 3, "nombre": "Audífonos", "descripcion": "Inalámbricos", "precio": 1200, "ruta_imagen": "audifonos.png"},
    {"id": 4, "nombre": "Teclado", "descripcion": "Teclado RGB", "precio": 900, "ruta_imagen": "teclado.png"},
    {"id": 5, "nombre": "Mouse", "descripcion": "Alta precisión", "precio": 700, "ruta_imagen": "mouse.png"}
]

# =========================
# COMPONENTE REUTILIZABLE
# =========================
class ProductoCard(ft.Container):
    def __init__(self, producto, agregar_callback):
        super().__init__()

        self.producto = producto
        self.width = 250
        self.padding = 15
        self.border_radius = 15
        self.bgcolor = ft.Colors.WHITE
        self.shadow = ft.BoxShadow(
            blur_radius=10,
            color=ft.Colors.BLACK12,
            offset=ft.Offset(2, 2)
        )

        self.content = ft.Column(
            controls=[
                ft.Image(
                    src=producto["ruta_imagen"],
                    width=200,
                    height=150,
                    fit=ft.ImageFit.CONTAIN,
                    error_content=ft.Icon(ft.Icons.IMAGE_NOT_SUPPORTED, size=40)
                ),
                ft.Text(producto["nombre"], weight="bold", size=18),
                ft.Text(producto["descripcion"], size=13, color=ft.Colors.GREY_700),
                ft.Text(f"${producto['precio']:,}", color=ft.Colors.GREEN_700, size=16, weight="bold"),
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.IconButton(icon=ft.Icons.FAVORITE_BORDER, icon_color=ft.Colors.PINK),
                        ft.ElevatedButton(
                            "Agregar",
                            on_click=lambda e: agregar_callback(self.producto),
                            style=ft.ButtonStyle(color=ft.Colors.WHITE, bgcolor=ft.Colors.BLUE_600)
                        )
                    ]
                )
            ]
        )

# =========================
# INTERFAZ PRINCIPAL
# =========================
def main(page: ft.Page):
    page.title = "Mi Tienda Web - Proyecto Integrador"
    page.bgcolor = ft.Colors.GREY_100
    page.theme_mode = ft.ThemeMode.LIGHT
    page.scroll = ft.ScrollMode.ADAPTIVE

    carrito = []
    total_text = ft.Text("Total: $0", size=24, weight="bold", color=ft.Colors.BLUE_900)
    lista_carrito = ft.Column(scroll=ft.ScrollMode.AUTO, height=400)

    def agregar_al_carrito(producto):
        carrito.append(producto)
        lista_carrito.controls.append(
            ft.ListTile(
                leading=ft.Icon(ft.Icons.SHOPPING_BAG, color=ft.Colors.BLUE_400),
                title=ft.Text(f"{producto['nombre']}"),
                subtitle=ft.Text(f"${producto['precio']:,}"),
                trailing=ft.IconButton(
                    ft.Icons.DELETE_OUTLINE, 
                    icon_color=ft.Colors.RED_400,
                    on_click=lambda e, p=producto: eliminar_del_carrito(e, p)
                )
            )
        )
        actualizar_total()
        page.update()

    def eliminar_del_carrito(e, producto):
        # Esta es una mejora para que tu proyecto sea más funcional
        carrito.remove(producto)
        # Buscamos el control en la lista y lo quitamos
        for control in lista_carrito.controls[:]:
            if control.title.value == producto['nombre']:
                lista_carrito.controls.remove(control)
                break
        actualizar_total()
        page.update()

    def actualizar_total():
        total = sum(p["precio"] for p in carrito)
        total_text.value = f"Total: ${total:,}"

    tarjetas = [ProductoCard(p, agregar_al_carrito) for p in productos]

    # Layout Responsivo
    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    ft.Text("TecnoShop 🚀", size=40, weight="bold", color=ft.Colors.BLUE_800),
                    ft.Row(
                        vertical_alignment=ft.CrossAxisAlignment.START,
                        controls=[
                            # Galería de productos
                            ft.Column(
                                expand=3,
                                controls=[
                                    ft.Text("Catálogo de Productos", size=20, weight="w500"),
                                    ft.Row(controls=tarjetas, wrap=True, spacing=20)
                                ]
                            ),
                            # Panel del Carrito
                            ft.Container(
                                expand=1,
                                padding=20,
                                bgcolor=ft.Colors.WHITE,
                                border_radius=20,
                                border=ft.border.all(1, ft.Colors.GREY_300),
                                content=ft.Column(
                                    controls=[
                                        ft.Row([ft.Icon(ft.Icons.SHOPPING_CART), ft.Text("Tu Carrito", size=22, weight="bold")]),
                                        ft.Divider(),
                                        lista_carrito,
                                        ft.Divider(),
                                        total_text,
                                        ft.ElevatedButton(
                                            "Pagar ahora", 
                                            icon=ft.Icons.CHECKOUT,
                                            width=300, 
                                            height=50,
                                            style=ft.ButtonStyle(bgcolor=ft.Colors.GREEN_600, color=ft.Colors.WHITE)
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                ]
            )
        )
    )

# =========================
# CONFIGURACIÓN PARA RENDER
# =========================
if __name__ == "__main__":
    # Estas líneas resuelven los errores de puerto y vista que tenías en Render
    ft.app(
        target=main,
        view=ft.AppView.WEB_BROWSER,
        assets_dir="assets",
        port=int(os.getenv("PORT", 8550))
    )