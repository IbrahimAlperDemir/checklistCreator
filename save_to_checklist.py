from openpyxl import Workbook
from openpyxl.styles import Font
from datetime import datetime

def save_to_checklist(test_cases: list, filename: str, revision: str = "A") -> None:
    wb = Workbook()
    ws = wb.active
    ws.title = "Test Checklist"

    # Üst Bilgi
    ws["A1"] = "Form Adı:"
    ws["B1"] = "Test Senaryosu Kontrol Listesi"
    ws["A2"] = "Form No:"
    ws["B2"] = "FRM-TST-001"
    ws["A3"] = "Revizyon:"
    ws["B3"] = revision
    ws["A4"] = "Tarih:"
    ws["B4"] = datetime.today().strftime("%d.%m.%Y")

    # Başlıklar
    headers = ["NO", "TEST KOŞULU", "TEST AÇIKLAMASI", "TEST SENARYOSU", "BEKLENEN DURUM"]
    ws.append([])
    ws.append(headers)
    for cell in ws[6]:  # Başlık satırı
        cell.font = Font(bold=True)

    # Veri Ekleme
    for i, case in enumerate(test_cases, start=1):
        ws.append([
            str(i),
            case["condition"],
            case["description"],
            case["steps"],
            case["expected"]
        ])

    wb.save(filename)
