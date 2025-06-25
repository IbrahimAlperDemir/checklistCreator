from openpyxl import Workbook
from openpyxl.styles import Font, Alignment
from datetime import datetime

def save_to_checklist(test_data: list, filename: str = "Test_Checklist.xlsx", revision: str = "A"):
    wb = Workbook()
    ws = wb.active
    ws.title = "Test Checklist"

    # Başlığı YALNIZCA eklemeden önce sayfa boşsa ekle
    if ws.max_row == 1 and ws.max_column == 1 and ws["A1"].value is None:
        headers = ["NO", "TEST KOŞULU", "TEST AÇIKLAMASI", "TEST SENARYOSU", "BEKLENEN DURUM"]
        ws.append(headers)

        # Stil uygula
        for col in ws.iter_cols(min_row=1, max_row=1):
            for cell in col:
                cell.font = Font(bold=True)
                cell.alignment = Alignment(horizontal="center")

    # Verileri ekle
    for idx, row in enumerate(test_data, 1):
        ws.append([
            idx,
            row.get("condition", ""),
            row.get("description", ""),
            row.get("steps", ""),
            row.get("expected", "")
        ])

    # Dosyayı kaydet
    wb.save(filename)
