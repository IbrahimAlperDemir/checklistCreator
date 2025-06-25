from openpyxl import Workbook
from openpyxl.styles import Font, Alignment

def save_to_checklist(test_data: list, filename: str = "Test_Checklist.xlsx", revision: str = "A"):
    wb = Workbook()
    ws = wb.active
    ws.title = "Test Checklist"

    # Başlık satırı sadece bir kez eklenir
    headers = ["NO", "TEST KOŞULU", "TEST AÇIKLAMASI", "TEST SENARYOSU", "BEKLENEN DURUM"]
    ws.append(headers)

    # Stil uygula
    for col in ws.iter_cols(min_row=1, max_row=1):
        for cell in col:
            cell.font = Font(bold=True)
            cell.alignment = Alignment(horizontal="center")

    # Veriler
    for idx, line in enumerate(test_data, 1):
        # Satırı parçalara ayır
        parts = [p.strip() for p in line.split("|")]
        while len(parts) < 4:
            parts.append("")  # Eksikse boşlukla tamamla

        ws.append([idx] + parts[:4])  # Sadece ilk 4 kısmı al (koşul, açıklama, senaryo, beklenen)

    wb.save(filename)
