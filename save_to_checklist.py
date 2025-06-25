from openpyxl import Workbook
from openpyxl.styles import Font, Alignment
from datetime import datetime

def save_to_checklist(text: str, filename: str = "Test_Checklist.xlsx", revision: str = "A") -> None:
    wb = Workbook()
    ws = wb.active
    ws.title = "Test Cases"

    # 🔰 Başlık bilgileri
    ws["A1"] = "TEST CHECKLIST FORMU"
    ws["A1"].font = Font(bold=True, size=14)
    ws.merge_cells("A1:E1")

    ws["A2"] = "Form No:"
    ws["B2"] = "FRM-QA-001"
    ws["A3"] = "Revizyon:"
    ws["B3"] = revision
    ws["A4"] = "Tarih:"
    ws["B4"] = datetime.today().strftime("%d.%m.%Y")

    for cell in ["A2", "A3", "A4"]:
        ws[cell].font = Font(bold=True)

    # 📌 İçerik başlıkları
    headers = ["NO", "TEST KOŞULU", "TEST AÇIKLAMASI", "TEST SENARYOSU", "BEKLENEN DURUM"]
    ws.append([])
    ws.append(headers)
    for col in ws.iter_cols(min_row=6, max_row=6, min_col=1, max_col=5):
        for cell in col:
            cell.font = Font(bold=True)
            cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

    # 📤 Satırları ekle
    lines = text.strip().split("\n")
    start_index = 1 if "NO" in lines[0] else 0  # Başlık varsa atla
    for line in lines[start_index:]:
        parts = [p.strip() for p in line.split("|")]
        if len(parts) == 5:
            ws.append(parts)

    # Sütun genişlikleri
    column_widths = [5, 25, 25, 30, 30]
    for i, width in enumerate(column_widths, start=1):
        ws.column_dimensions[chr(64 + i)].width = width

    wb.save(filename)
