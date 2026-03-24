import flet as ft
import os

# =========================
# MODELO DE DATOS COMPLETO
# =========================
productos = [
    {"id": 1, "nombre": "Laptop Gamer", "precio": 25000, "ruta_imagen": "laptop.png"},
    {"id": 2, "nombre": "Smartphone", "precio": 15000, "ruta_imagen": "telefono.png"},
    {"id": 3, "nombre": "Audífonos", "precio": 1200, "ruta_imagen": "audifonos.png"},
    {"id": 4, "nombre": "Teclado", "precio": 900, "ruta_imagen": "teclado.png"},
    {"id": 5, "nombre": "Mouse", "precio": 700, "ruta_imagen": "mouse.png"}
]

def main(page: ft.Page):
    page.title = "Tienda Oficial"
    page.padding = 20
    page.scroll = "adaptive" # Simplificado para evitar errores de versión

    carrito = []
    lista_carrito = ft.Column()
    total_text = ft.Text("Total: $0", size=20, weight="bold")

    def agregar(p):
        carrito.append(p)
        lista_carrito.controls.append(ft.Text(f"• {p['nombre']} - ${p['precio']}"))
        total_text.value = f"Total: ${sum(item['precio'] for item in carrito)}"
        page.update()

    galeria = ft.Row(wrap=True, spacing=20)

    for p in productos:
        galeria.controls.append(
            ft.Container(
                content=ft.Column([
                    # Quitamos 'fit=ft.ImageFit.CONTAIN' para evitar el error rosa
                    ft.Image(src=p["ruta_imagen"], width=150, height=150),
                    ft.Text(p["nombre"], weight="bold"),
                    ft.Text(f"${p['precio']}"),
                    ft.ElevatedButton("Agregar", on_click=lambda e, prod=p: agregar(prod))
                ]),
                padding=10, border=ft.border.all(1, "grey400"), border_radius=10
            )
        )

    page.add(
        ft.Text("Mi Tienda Tecnológica", size=30, weight="bold"),
        galeria,
        ft.Divider(),
        ft.Text("Carrito de Compras", size=20),
        lista_carrito,
        total_text
    )

if __name__ == "__main__":
    # Configuraciones vitales para Render
    port = int(os.getenv("PORT", 8550))
    ft.app(
        target=main,
        view=None, # Deja que Flet decida la mejor vista web automáticamente
        assets_dir="assets",
        port=port,
        host="0.0.0.0"
    )