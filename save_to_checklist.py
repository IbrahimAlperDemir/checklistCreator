from openpyxl import Workbook
from openpyxl.styles import Font, Alignment
from datetime import datetime
from form_tracker import get_next_form_number

def save_to_checklist(content: str, filename: str = "Test_Case_Listesi.xlsx", revision: str = "A") -> None:
    wb = Workbook()
    ws = wb.active
    ws.title = "Test Cases"

    # Üst Bilgi
    ws.merge_cells("A1:E1")
    ws["A1"] = f"FRM-TST-{revision} | Test Checklist | {datetime.today().strftime('%d.%m.%Y')}"
    ws["A1"].font = Font(bold=True, size=12)
    ws["A1"].alignment = Alignment(horizontal="center")

    row_start = 3  # veri tablosu bu satırdan başlar

    # Satırları hazırla
    lines = content.strip().splitlines()
    if not lines or "|" not in lines[0]:
        raise ValueError("GPT'den gelen çıktı uygun formatta değil.")

    headers = [cell.strip() for cell in lines[0].split("|") if cell.strip()]
    ws.append(headers)

    for row in lines[2:]:  # başlık ve ayırıcıyı geç
        if "|" in row:
            cells = [cell.strip() for cell in row.split("|") if cell.strip()]
            if len(cells) == len(headers):
                ws.append(cells)

    # Stil
    for col in ws.columns:
        max_len = max(len(str(cell.value)) if cell.value else 0 for cell in col)
        col_letter = col[0].column_letter
        ws.column_dimensions[col_letter].width = max_len + 5

    # Kaydet
    wb.save(filename)
    print(f"✅ '{filename}' başarıyla kaydedildi.")
