from openpyxl import Workbook
from openpyxl.styles import Font, Alignment
from datetime import datetime

def save_to_checklist(text: str, filename="Test_Checklist.xlsx", revision="A"):
    wb = Workbook()
    ws = wb.active
    ws.title = "Test Checklist"

    headers = ["NO", "TEST KOŞULU", "TEST AÇIKLAMASI", "TEST SENARYOSU", "BEKLENEN DURUM"]
    ws.append(headers)

    bold_font = Font(bold=True)
    center_align = Alignment(horizontal="center", vertical="center", wrap_text=True)

    for col in ws.iter_cols(min_row=1, max_row=1, max_col=len(headers)):
        for cell in col:
            cell.font = bold_font
            cell.alignment = center_align

    # Her test case bloğunu ayır
    for i, group in enumerate(text.strip().split("\n\n"), start=1):
        lines = group.strip().split("\n")
        if len(lines) >= 4:
            ws.append([
                i,
                lines[0].strip(),
                lines[1].strip(),
                lines[2].strip(),
                lines[3].strip()
            ])

    ws.append([])
    ws.append([f"Revizyon: {revision}", f"Tarih: {datetime.today().strftime('%d.%m.%Y')}"])

    wb.save(filename)
