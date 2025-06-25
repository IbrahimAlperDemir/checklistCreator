from openpyxl import Workbook
from openpyxl.styles import Font, Alignment
from datetime import datetime

def save_to_checklist(test_cases, filename="Test_Checklist.xlsx", revision="A"):
    wb = Workbook()
    ws = wb.active
    ws.title = "Test Checklist"

    # Başlık satırı
    headers = ["NO", "TEST KOŞULU", "TEST AÇIKLAMASI", "TEST SENARYOSU", "BEKLENEN DURUM"]
    ws.append(headers)

    # Stil
    bold_font = Font(bold=True)
    center_align = Alignment(horizontal="center", vertical="center", wrap_text=True)

    for col in ws.iter_cols(min_row=1, max_row=1, min_col=1, max_col=len(headers)):
        for cell in col:
            cell.font = bold_font
            cell.alignment = center_align

    # Satırları yaz
    for idx, case in enumerate(test_cases, start=1):
        ws.append([
            idx,
            case.get("condition", ""),     # condition artık yoksa "" döner
            case["description"],
            case["steps"],
            case["expected"]
        ])

    # Alt bilgi
    ws.append([])
    ws.append([f"Revizyon: {revision}", f"Tarih: {datetime.today().strftime('%d.%m.%Y')}"])

    wb.save(filename)
