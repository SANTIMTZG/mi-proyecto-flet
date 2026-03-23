import flet as ft

# =========================
# MODELO DE DATOS
# =========================
productos = [
    {"id": 1, "nombre": "Laptop Gamer", "descripcion": "Laptop potente", "precio": 25000, "ruta_imagen": "assets/laptop.png"},
    {"id": 2, "nombre": "Smartphone", "descripcion": "Teléfono moderno", "precio": 15000, "ruta_imagen": "assets/telefono.png"},
    {"id": 3, "nombre": "Audífonos", "descripcion": "Inalámbricos", "precio": 1200, "ruta_imagen": "assets/audifonos.png"},
    {"id": 4, "nombre": "Teclado", "descripcion": "Teclado RGB", "precio": 900, "ruta_imagen": "assets/teclado.png"},
    {"id": 5, "nombre": "Mouse", "descripcion": "Alta precisión", "precio": 700, "ruta_imagen": "assets/mouse.png"}
]

# =========================
# COMPONENTE REUTILIZABLE
# =========================
class ProductoCard(ft.Container):
    def __init__(self, producto, agregar_callback):
        super().__init__()

        self.producto = producto

        self.width = 250
        self.padding = 10
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
                    fit="cover"
                ),

                ft.Text(producto["nombre"], weight="bold", size=16),

                ft.Text(producto["descripcion"], size=12, color=ft.Colors.GREY),

                ft.Text(f"${producto['precio']}", color=ft.Colors.GREEN, size=14),

                ft.Row(
                    alignment="spaceBetween",
                    controls=[
                        ft.Text("❤"),
                        ft.ElevatedButton(
                            "Agregar",
                            on_click=lambda e: agregar_callback(self.producto)
                        )
                    ]
                )
            ]
        )

# =========================
# INTERFAZ PRINCIPAL
# =========================
def main(page: ft.Page):
    page.title = "Tienda con Carrito"
    page.bgcolor = ft.Colors.GREY_200

    carrito = []
    total_text = ft.Text("Total: $0", size=20, weight="bold")
    lista_carrito = ft.Column()

    # Función para agregar productos
    def agregar_al_carrito(producto):
        carrito.append(producto)

        lista_carrito.controls.append(
            ft.Text(f"{producto['nombre']} - ${producto['precio']}")
        )

        total = sum(p["precio"] for p in carrito)
        total_text.value = f"Total: ${total}"

        page.update()

    # Crear tarjetas
    tarjetas = [
        ProductoCard(p, agregar_al_carrito) for p in productos
    ]

    # Layout principal
    page.add(
        ft.Row(
            controls=[
                # Productos
                ft.Column(
                    controls=[
                        ft.Text("Productos", size=25, weight="bold"),
                        ft.Row(controls=tarjetas, wrap=True)
                    ],
                    expand=2
                ),

                # Carrito
                ft.Container(
                    width=300,
                    padding=10,
                    bgcolor=ft.Colors.WHITE,
                    content=ft.Column(
                        controls=[
                            ft.Text("Carrito 🛒", size=20, weight="bold"),
                            lista_carrito,
                            ft.Divider(),
                            total_text
                        ]
                    )
                )
            ]
        )
    )

# =========================
# EJECUCIÓN
# =========================
ft.app(target=main, view="web_browser")