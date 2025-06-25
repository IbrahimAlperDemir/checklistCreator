from openpyxl import Workbook
from openpyxl.utils import get_column_letter
from datetime import datetime
import os

def save_to_checklist(text: str, filename: str = "Test_Checklist.xlsx", revision: str = "A"):
    wb = Workbook()
    ws = wb.active
    ws.title = "Test Cases"

    # Başlık bilgileri
    ws["A1"] = "Form Adı:"
    ws["B1"] = "Test Checklist"
    ws["A2"] = "Form Numarası:"
    ws["B2"] = "FRM-TST-001"
    ws["A3"] = "Versiyon:"
    ws["B3"] = revision
    ws["A4"] = "Hazırlayan:"
    ws["B4"] = "Otomatik AI Sistem"
    ws["A5"] = "Tarih:"
    ws["B5"] = datetime.today().strftime("%d.%m.%Y")

    # Boşluk bırakmak için satır
    row_offset = 7

    # Sütun başlıkları
    headers = ["NO", "TEST KOŞULU", "TEST AÇIKLAMASI", "TEST SENARYOSU", "BEKLENEN DURUM"]
    for col_index, header in enumerate(headers, start=1):
        cell = ws.cell(row=row_offset, column=col_index, value=header)

    # Test adımlarını satırlara bölerek işle
    test_rows = []
    for i, group in enumerate(text.strip().split("\n\n"), start=1):
        lines = group.strip().split("\n")
        if len(lines) >= 4:
            condition = lines[0].strip("-* ")
            explanation = lines[1].strip("-* ")
            steps = lines[2].strip("-* ")
            expected = lines[3].strip("-* ")
            test_rows.append([i, condition, explanation, steps, expected])

    for row_index, row_data in enumerate(test_rows, start=row_offset + 1):
        for col_index, value in enumerate(row_data, start=1):
            ws.cell(row=row_index, column=col_index, value=value)

    # Sütun genişliği ayarı
    for col_index in range(1, len(headers) + 1):
        col_letter = get_column_letter(col_index)
        ws.column_dimensions[col_letter].width = 25

    wb.save(filename)
    print(f"✅ '{filename}' başarıyla kaydedildi.")
