import flet as ft
import os

# =========================
# 1. MODELO DE DATOS (Nombres exactos de GitHub)
# =========================
# Se han ajustado los nombres para que coincidan con image_e561be.png
productos_datos = [
    {"n": "Laptop Gamer", "p": 25000, "i": "Laptop Gamer.png"},
    {"n": "Smartphone", "p": 15000, "i": "Smartphone.png"},
    {"n": "Audífonos", "p": 1200, "i": "Audífonos.png"},
    {"n": "Teclado RGB", "p": 900, "i": "Teclado.png"},
    {"n": "Mouse Pro", "p": 700, "i": "Mouse.png"}
]

def main(page: ft.Page):
    page.title = "Tienda Tecnológica Final"
    page.padding = 20
    page.theme_mode = ft.ThemeMode.LIGHT
    page.scroll = "adaptive"

    carrito = []
    lista_compra = ft.Column()
    total_txt = ft.Text("Total: $0", size=25, weight="bold")

    # =========================
    # FUNCIONES DEL CARRITO
    # =========================
    def actualizar_interfaz_carrito():
        lista_compra.controls.clear()
        for index, item in enumerate(carrito):
            lista_compra.controls.append(
                ft.Row([
                    ft.Text(f"• {item['n']} - ${item['p']}"),
                    ft.IconButton(
                        icon=ft.icons.DELETE_OUTLINE,
                        icon_color="red",
                        tooltip="Eliminar producto",
                        on_click=lambda e, i=index: eliminar_del_carrito(i)
                    )
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
            )
        total = sum(item['p'] for item in carrito)
        total_txt.value = f"Total: ${total}"
        page.update()

    def agregar_al_carrito(prod):
        carrito.append(prod)
        actualizar_interfaz_carrito()

    def eliminar_del_carrito(index):
        carrito.pop(index)
        actualizar_interfaz_carrito()

    # =========================
    # DISEÑO DE LA GALERÍA
    # =========================
    galeria = ft.Row(wrap=True, spacing=20)

    for p in productos_datos:
        galeria.controls.append(
            ft.Container(
                content=ft.Column([
                    # Usamos los nombres de archivo exactos de tu captura
                    ft.Image(src=p["i"], width=140, height=140),
                    ft.Text(p["n"], weight="bold"),
                    ft.Text(f"${p['p']}"),
                    ft.ElevatedButton(
                        "Agregar", 
                        icon=ft.icons.ADD_SHOPPING_CART,
                        on_click=lambda e, prod=p: agregar_al_carrito(prod)
                    )
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                padding=15, 
                border=ft.border.all(1, "grey300"), 
                border_radius=10,
                width=180
            )
        )

    # =========================
    # ESTRUCTURA DE LA PÁGINA
    # =========================
    page.add(
        ft.Text("Catálogo de Productos 🚀", size=32, weight="bold"),
        galeria,
        ft.Divider(height=40),
        ft.Container(
            content=ft.Column([
                ft.Text("Tu Carrito de Compras", size=24, weight="bold"),
                lista_compra,
                ft.Divider(),
                total_txt
            ]),
            padding=20,
            bgcolor="grey100",
            border_radius=10
        )
    )

# =========================
# CONFIGURACIÓN PARA RENDER
# =========================
if __name__ == "__main__":
    # Importante: host 0.0.0.0 y puerto dinámico para evitar 'Port scan timeout'
    port = int(os.getenv("PORT", 8550))
    ft.app(
        target=main,
        assets_dir="assets", # Flet buscará aquí tus imágenes de GitHub
        port=port,
        host="0.0.0.0"
    )