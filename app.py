import flet as ft
import flet_fastapi


async def primeira_pagina(page: ft.Page):
    btn = ft.TextButton(
        icon=ft.icons.OPEN_IN_NEW,
        text="Acessar segunda página",
        url="/segunda-pagina/",
    )
    await page.add_async(
        ft.Text("Primeira página!"),
        btn,
    )


async def segunda_pagina(page: ft.Page):
    btn = ft.TextButton(
        icon=ft.icons.OPEN_IN_NEW,
        text="Acessar primeira página",
        url="/primeira-pagina/",
    )
    await page.add_async(
        ft.Text("Segunda página!"),
        btn,
    )


app = flet_fastapi.FastAPI()


app.mount("/primeira-pagina", flet_fastapi.app(primeira_pagina))
app.mount("/segunda-pagina", flet_fastapi.app(segunda_pagina))
