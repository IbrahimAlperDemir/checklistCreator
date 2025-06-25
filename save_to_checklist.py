from openpyxl import Workbook
from datetime import datetime

def save_to_checklist(test_data: list, filename: str = "Test_Checklist.xlsx", revision: str = "A") -> None:
    wb = Workbook()
    ws = wb.active

    # Başlıklar – sadece 1 kez yazılır
    headers = ["NO", "TEST KOŞULU", "TEST AÇIKLAMASI", "TEST SENARYOSU", "BEKLENEN DURUM"]
    ws.append(headers)

    for i, item in enumerate(test_data, start=1):
        ws.append([
            str(i),
            item.get("condition", ""),
            item.get("description", ""),
            item.get("steps", ""),
            item.get("expected", "")
        ])

    wb.save(filename)
