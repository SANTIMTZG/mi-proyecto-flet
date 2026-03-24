import flet as ft
import os

# 1. DATOS DE PRODUCTOS
productos_datos = [
    {"nombre": "Laptop Gamer", "precio": 25000, "imagen": "Laptop Gamer.png"},
    {"nombre": "Smartphone", "precio": 15000, "imagen": "Smartphone.png"},
    {"nombre": "Audífonos", "precio": 1200, "imagen": "Audífonos.png"},
    {"nombre": "Teclado RGB", "precio": 900, "imagen": "Teclado.png"},
    {"nombre": "Mouse Pro", "precio": 700, "imagen": "Mouse.png"}
]

def main(page: ft.Page):
    page.title = "Tienda Tecnológica"
    page.scroll = "adaptive"
    page.theme_mode = ft.ThemeMode.LIGHT
    
    carrito = []
    lista_compra = ft.Column()
    total_txt = ft.Text("Total: $0", size=25, weight="bold")

    def actualizar_ui():
        lista_compra.controls.clear()
        for index, item in enumerate(carrito):
            lista_compra.controls.append(
                ft.Row([
                    ft.Text(f"• {item['nombre']} - ${item['precio']}"),
                    ft.IconButton(
                        icon=ft.icons.DELETE_OUTLINE,
                        icon_color="red",
                        on_click=lambda e, i=index: eliminar_item(i)
                    )
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
            )
        # ESTA LÍNEA DEBE ESTAR ALINEADA CON EL 'for'
        total = sum(p['precio'] for p in carrito)
        total_txt.value = f"Total: ${total}"
        page.update()

    def eliminar_item(index):
        carrito.pop(index)
        actualizar_ui()

    def agregar_al_carrito(prod):
        carrito.append(prod)
        actualizar_ui()

    # --- DISEÑO DE LA GALERÍA ---
    galeria = ft.Row(wrap=True, spacing=20)
    for p in productos_datos:
        galeria.controls.append(
            ft.Container(
                content=ft.Column([
                    ft.Image(src=p["imagen"], width=140, height=140),
                    ft.Text(p["nombre"], weight="bold"),
                    ft.Text(f"${p['precio']}"),
                    ft.ElevatedButton(
                        "Agregar", 
                        icon=ft.icons.ADD_SHOPPING_CART,
                        on_click=lambda e, prod=p: agregar_al_carrito(prod)
                    )
                ], horizontal_alignment="center"),
                padding=15, border=ft.border.all(1, "grey300"), border_radius=10, width=180
            )
        )

    page.add(
        ft.Text("Mi Tienda Tecnológica 🚀", size=32, weight="bold"),
        galeria,
        ft.Divider(height=40),
        ft.Container(
            content=ft.Column([
                ft.Text("Carrito de Compras", size=24, weight="bold"),
                lista_compra,
                ft.Divider(),
                total_txt
            ]),
            padding=20, bgcolor="grey100", border_radius=10
        )
    )

if __name__ == "__main__":
    # Render usa el puerto 10000 por defecto
    port = int(os.getenv("PORT", 10000))
    ft.app(target=main, assets_dir="assets", port=port, host="0.0.0.0")