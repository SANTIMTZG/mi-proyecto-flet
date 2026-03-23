import flet as ft
import os  # VITAL: Render usa variables de entorno para el puerto

# =========================
# MODELO DE DATOS
# =========================
productos = [
    {"id": 1, "nombre": "Laptop Gamer", "descripcion": "Laptop potente", "precio": 25000, "ruta_imagen": "laptop.png"},
    {"id": 2, "nombre": "Smartphone", "descripcion": "Teléfono moderno", "precio": 15000, "ruta_imagen": "telefono.png"},
    {"id": 3, "nombre": "Audífonos", "descripcion": "Inalámbricos", "precio": 1200, "ruta_imagen": "audifonos.png"}
]

# =========================
# INTERFAZ PRINCIPAL
# =========================
def main(page: ft.Page):
    page.title = "Tienda Web - Proyecto Integrador"
    page.bgcolor = ft.Colors.GREY_100
    page.scroll = ft.ScrollMode.ADAPTIVE

    carrito = []
    total_text = ft.Text("Total: $0", size=24, weight="bold")
    lista_carrito = ft.Column()

    def agregar_al_carrito(producto):
        carrito.append(producto)
        lista_carrito.controls.append(ft.Text(f"• {producto['nombre']} - ${producto['precio']:,}"))
        total = sum(p["precio"] for p in carrito)
        total_text.value = f"Total: ${total:,}"
        page.update()

    # Creación de tarjetas
    for p in productos:
        page.add(
            ft.Container(
                content=ft.Column([
                    ft.Text(p["nombre"], weight="bold"),
                    ft.ElevatedButton("Agregar", on_click=lambda e, prod=p: agregar_al_carrito(prod))
                ]),
                padding=10, border=ft.border.all(1, ft.Colors.GREY_400), border_radius=10
            )
        )
    
    page.add(ft.Divider(), ft.Text("Tu Carrito:", size=20, weight="bold"), lista_carrito, total_text)

# =========================
# CONFIGURACIÓN DE RED (PARA RENDER)
# =========================
if __name__ == "__main__":
    # Render asigna dinámicamente un puerto. Si no existe, usamos el 8550.
    port = int(os.getenv("PORT", 8550))
    
    # IMPORTANTE: Usamos ft.app con view=ft.AppView.WEB_BROWSER y host="0.0.0.0"
    ft.app(
        target=main,
        view=ft.AppView.WEB_BROWSER,
        port=port,
        host="0.0.0.0"  # Permite que Render vea la app desde afuera
    )