from openpyxl import Workbook
from openpyxl.styles import Font
from datetime import datetime

def save_to_checklist(test_cases: list, filename: str = "Test_Checklist.xlsx", revision: str = "A") -> None:
    wb = Workbook()
    ws = wb.active
    ws.title = "Test Checklist"

    # 📌 Üst Bilgi
    ws["A1"] = "Form Adı:"
    ws["B1"] = "Test Case Checklist"

    ws["A2"] = "Form Numarası:"
    ws["B2"] = "FRM-TEST-001"

    ws["A3"] = "Versiyon:"
    ws["B3"] = "1.0"

    ws["A4"] = "Hazırlayan:"
    ws["B4"] = "Otomatik AI Sistem"

    ws["A5"] = "Revizyon:"
    ws["B5"] = revision

    ws["A6"] = "Tarih:"
    ws["B6"] = datetime.today().strftime("%d.%m.%Y")

    # 📄 Başlıklar
    headers = ["NO", "TEST KOŞULU", "TEST AÇIKLAMASI", "TEST SENARYOSU", "BEKLENEN DURUM"]
    ws.append([])  # boş satır
    ws.append(headers)

    for cell in ws[8]:  # başlıklar satırı (8. satır çünkü 6 satır üst bilgi + 1 boşluk)
        cell.font = Font(bold=True)

    # 📋 Test Verileri
    for i, case in enumerate(test_cases, start=1):
        ws.append([
            str(i),
            case.get("condition", ""),
            case.get("description", ""),
            case.get("steps", ""),
            case.get("expected", "")
        ])

    # Kaydet
    wb.save(filename)
    print(f"✅ '{filename}' başarıyla kaydedildi.")
