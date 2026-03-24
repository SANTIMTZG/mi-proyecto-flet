import flet as ft
import os

# 1. DATOS DE PRODUCTOS
productos_datos = [
    {"n": "Laptop Gamer", "p": 25000, "i": "Laptop Gamer.png"},
    {"n": "Smartphone", "p": 15000, "i": "Smartphone.png"},
    {"n": "Audífonos", "p": 1200, "i": "Audífonos.png"},
    {"n": "Teclado RGB", "p": 900, "i": "Teclado.png"},
    {"n": "Mouse Pro", "p": 700, "i": "Mouse.png"}
]

def main(page: ft.Page):
    page.title = "Tienda Final"
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
                    ft.Text(f"• {item['n']} - ${item['p']}"),
                    ft.IconButton(
                        icon=ft.icons.DELETE_OUTLINE,
                        icon_color="red",
                        on_click=lambda e, i=index: eliminar(i)
                    )
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
            )
        total_txt.value = f"Total: ${sum(p['p'] for p in carrito)}"
        page.update()

    def eliminar(idx):
        carrito.pop(idx)
        actualizar_ui()

    galeria = ft.Row(wrap=True, spacing=20)
    for p in productos_datos:
        galeria.controls.append(
            ft.Container(
                content=ft.Column([
                    ft.Image(src=p["i"], width=140, height=140),
                    ft.Text(p["n"], weight="bold"),
                    ft.Text(f"${p['p']}"),
                    ft.ElevatedButton("Agregar", on_click=lambda e, pr=p: (carrito.append(pr), actualizar_ui()))
                ], horizontal_alignment="center"),
                padding=15, border=ft.border.all(1, "grey300"), border_radius=10, width=180
            )
        )

    page.add(
        ft.Text("Mi Catálogo Tecnológico 🚀", size=32, weight="bold"),
        galeria,
        ft.Divider(),
        ft.Text("Carrito de Compras", size=24),
        lista_compra,
        total_txt
    )

if __name__ == "__main__":
    # CONFIGURACIÓN CRÍTICA PARA RENDER
    # Usamos el puerto que Render asigna o el 10000 que es el estándar de Render
    puerto = int(os.getenv("PORT", 10000))
    ft.app(
        target=main,
        view=None,
        assets_dir="assets",
        port=puerto,
        host="0.0.0.0" # IMPORTANTE: 0.0.0.0 permite conexiones externas
    )