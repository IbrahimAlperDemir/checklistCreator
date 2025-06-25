from openpyxl import Workbook
from openpyxl.utils import get_column_letter
from openpyxl.styles import Alignment
import re

def parse_test_cases(text: str):
    # Tablo yapısını satır satır parçala
    lines = text.strip().split("\n")
    parsed = []
    for line in lines:
        parts = [p.strip() for p in re.split(r"\||\t", line) if p.strip()]
        if len(parts) >= 5:
            parsed.append(parts[:5])
    return parsed

def save_to_checklist(text: str, filename: str = "Test_Case_Checklist.xlsx", revision: str = "A"):
    test_cases = parse_test_cases(text)
    wb = Workbook()
    ws = wb.active
    ws.title = "Test Cases"

    # Başlık
    headers = ["NO", "TEST KOŞULU", "TEST AÇIKLAMASI", "TEST SENARYOSU", "BEKLENEN DURUM"]
    ws.append(headers)

    for row in test_cases:
        ws.append(row)

    # Genişlik ve hizalama
    for col in ws.columns:
        max_length = max(len(str(cell.value)) if cell.value else 0 for cell in col)
        col_letter = get_column_letter(col[0].column)
        ws.column_dimensions[col_letter].width = max(15, min(max_length + 5, 50))
        for cell in col:
            cell.alignment = Alignment(wrap_text=True, vertical='top')

    wb.save(filename)
    print(f"✅ Excel dosyası '{filename}' olarak kaydedildi.")
