import openai
import streamlit as st

# Streamlit secrets'dan API anahtarını al
api_key = st.secrets["OPENAI_API_KEY"]
client = openai.OpenAI(api_key=api_key)

def build_testcase_prompt(data: dict) -> str:
    return f"""
### Özellik Adı
{data['name']}

### Özelliğin Amacı
{data['purpose']}

### Özellik Nasıl Çalışır?
{data['how_it_works']}

---
Yukarıdaki bilgileri kullanarak aşağıdaki formatta en az 3 test case üret:

NO | TEST KOŞULU | TEST AÇIKLAMASI | TEST SENARYOSU | BEKLENEN DURUM
1 | Ürün enerjilendirilmelidir | Zaman Erteleme Testi | Ürün açılır, zaman erteleme tuşuna basılır | Zaman erteleme aktif olur

Sadece tablo dön, başka açıklama verme.
"""

def generate_test_cases(data: dict) -> list:
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Bir test mühendisi gibi davranarak test senaryoları oluştur."},
            {"role": "user", "content": build_testcase_prompt(data)}
        ],
        temperature=0.3,
    )

    output = response.choices[0].message.content.strip()
    lines = output.splitlines()

    # Başlık satırını atla, sadece test case satırlarını al
    rows = [line for line in lines if not line.lower().startswith("no") and "|" in line]

    parsed = []
    for line in rows:
        parts = [part.strip() for part in line.split("|")]
        if len(parts) >= 5:
            parsed.append({
                "no": parts[0],
                "condition": parts[1],
                "description": parts[2],
                "scenario": parts[3],
                "expected": parts[4]
            })

    return parsed
