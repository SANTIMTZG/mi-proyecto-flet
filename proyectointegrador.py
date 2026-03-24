import flet as ft
import os

# 1. DATOS (Nombres exactos de tu GitHub)
productos_datos = [
    {"n": "Laptop Gamer", "p": 25000, "i": "Laptop Gamer.png"},
    {"n": "Smartphone", "p": 15000, "i": "Smartphone.png"},
    {"n": "Audífonos", "p": 1200, "i": "Audífonos.png"},
    {"n": "Teclado RGB", "p": 900, "i": "Teclado.png"},
    {"n": "Mouse Pro", "p": 700, "i": "Mouse.png"}
]

def main(page: ft.Page):
    page.title = "Tienda Tecnológica"
    page.padding = 20
    page.theme_mode = ft.ThemeMode.LIGHT
    page.scroll = "adaptive"

    carrito = []
    lista_compra = ft.Column()
    total_txt = ft.Text("Total: $0", size=25, weight="bold")

    # --- FUNCIONES DEL CARRITO ---
    def actualizar_carrito_ui():
        lista_compra.controls.clear()
        for index, item in enumerate(carrito):
            lista_compra.controls.append(
                ft.Row([
                    ft.Text(f"• {item['n']} - ${item['p']}"),
                    ft.IconButton(
                        icon=ft.icons.DELETE_FOREVER,
                        icon_color="red",
                        on_click=lambda e, i=index: eliminar_del_carrito(i)
                    )
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
            )
        total = sum(p['p'] for p in carrito)
        total_txt.value = f"Total: ${total}"
        page.update()

    def agregar_al_carrito(prod):
        carrito.append(prod)
        actualizar_carrito_ui()

    def eliminar_del_carrito(index):
        carrito.pop(index)
        actualizar_carrito_ui()

    # --- DISEÑO DE LA GALERÍA ---
    galeria = ft.Row(wrap=True, spacing=20)

    for p in productos_datos:
        galeria.controls.append(
            ft.Container(
                content=ft.Column([
                    ft.Image(src=p["i"], width=140, height=140),
                    ft.Text(p["n"], weight="bold"),
                    ft.Text(f"${p['p']}"),
                    ft.ElevatedButton(
                        "Agregar", 
                        icon=ft.icons.ADD_SHOPPING_CART,
                        on_click=lambda e, prod=p: agregar_al_carrito(prod)
                    )
                ], horizontal_alignment="center"),
                padding=15, 
                border=ft.border.all(1, "grey300"), 
                border_radius=10,
                width=180
            )
        )

    # --- AGREGAR A LA PÁGINA ---
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
    port = int(os.getenv("PORT", 8550))
    ft.app(target=main, assets_dir="assets", port=port, host="0.0.0.0")