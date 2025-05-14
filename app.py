import flet as ft
import flet_fastapi

from database import CARS


async def main(page: ft.Page):
    data_table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("marca")),
            ft.DataColumn(ft.Text("modelo")),
            ft.DataColumn(ft.Text("ano"), numeric=True),
        ],
    )

    for car in CARS:
        data_table.columns.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(car.get("marca"))),
                    ft.DataCell(ft.Text(car.get("modelo"))),
                    ft.DataCell(ft.Text(car.get("ano"))),
                ],
            ),
        )

    await page.add_async(
        data_table,
    )


app = flet_fastapi.app(main)