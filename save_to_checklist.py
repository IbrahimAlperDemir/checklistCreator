from openpyxl import Workbook
from openpyxl.styles import Font, Alignment
from datetime import datetime


def save_to_checklist(test_cases: list, filename: str, revision: str = "A"):
    wb = Workbook()
    ws = wb.active
    ws.title = "Test Checklist"

    # Üst bilgi (form sabit başlıkları)
    ws["A1"] = "Form Adı:"
    ws["B1"] = "Test Case Checklist"
    ws["A2"] = "Revizyon:"
    ws["B2"] = revision
    ws["A3"] = "Tarih:"
    ws["B3"] = datetime.today().strftime("%d.%m.%Y")

    # Boşluk satır
    ws.append([])

    # Başlıklar
    headers = ["NO", "TEST KOŞULU", "TEST AÇIKLAMASI", "TEST SENARYOSU", "BEKLENEN DURUM"]
    ws.append(headers)

    # Stil uygula
    for col in ws.iter_cols(min_row=5, max_row=5, min_col=1, max_col=len(headers)):
        for cell in col:
            cell.font = Font(bold=True)
            cell.alignment = Alignment(horizontal="center")

    # Satırları ekle
    for i, case in enumerate(test_cases, start=1):
        ws.append([
            i,
            case["condition"],
            case["description"],
            case["steps"],
            case["expected"]
        ])

    wb.save(filename)
    print(f"✅ Excel checklist kaydedildi: {filename}")
