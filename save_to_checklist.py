from openpyxl import Workbook
from openpyxl.styles import Font, Alignment
from openpyxl.utils import get_column_letter
from datetime import datetime
from form_tracker import get_next_form_number

def save_to_checklist(text: str, filename: str, revision: str = "A") -> None:
    wb = Workbook()
    ws = wb.active
    ws.title = "Test Checklist"

    # 🔢 Form numarası
    form_number = get_next_form_number("testcase")

    # 📋 Üst Bilgi Satırları
    ws.append(["Form Adı", "Test Senaryo Kontrol Listesi"])
    ws.append(["Form Numarası", f"FRM-TST-{form_number}"])
    ws.append(["Revizyon", revision])
    ws.append(["Tarih", datetime.today().strftime("%d.%m.%Y")])
    ws.append([])  # boş satır

    # 📌 Başlık Satırı (yeni sütun isimleri)
    ws.append(["NO", "TEST KOŞULU", "TEST AÇIKLAMASI", "TEST SENARYOSU", "BEKLENEN DURUM"])

    # 📄 İçerik (| ile ayrılmış satırları sütunlara böl)
    for line in text.splitlines():
        if line.strip():
            if "|" in line:
                parts = [p.strip() for p in line.split("|")]
                ws.append(parts[:5] + [""] * (5 - len(parts)))  # eksik sütunları tamamla
            else:
                ws.append([line.strip()])
        else:
            ws.append([])

    # 🎨 Stil: Üst bilgi + başlık satırları kalın ve ortalanmış
    for row in ws.iter_rows(min_row=1, max_row=6):
        for cell in row:
            cell.font = Font(bold=True)
            cell.alignment = Alignment(horizontal="center")

    # 🔧 Sütun genişlikleri otomatik ayarla
    for i, col in enumerate(ws.columns, start=1):
        max_length = 0
        for cell in col:
            try:
                if cell.value:
                    max_length = max(max_length, len(str(cell.value)))
            except:
                pass
        col_letter = get_column_letter(i)
        ws.column_dimensions[col_letter].width = max_length + 5

    # 💾 Kaydet
    wb.save(filename)
    print(f"✅ '{filename}' başarıyla kaydedildi.")
