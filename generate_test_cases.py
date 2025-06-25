import openai
import streamlit as st

# API key güvenli şekilde alınıyor
api_key = st.secrets["OPENAI_API_KEY"]
client = openai.OpenAI(api_key=api_key)

def build_testcase_prompt(data: dict) -> str:
    return f"""
### Özellik Adı
{data['feature_name']}

### Testin Amacı
{data['test_purpose']}

### Test Tipi
{data['test_type']}

### Test Adımları
{data['steps']}

### Beklenen Sonuçlar
{data['expected']}

---

Yukarıdaki bilgilerle aşağıdaki sütunlara uygun şekilde 3 örnek test case üret:

1. NO
2. TEST KOŞULU
3. TEST AÇIKLAMASI
4. TEST SENARYOSU
5. BEKLENEN DURUM

Her bir test case için ayrı satırda olacak şekilde çıktıyı formatla. Tabloda sütun isimleri ilk satırda olsun.
"""

def generate_test_cases(inputs: dict) -> str:
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Deneyimli bir QA testi uzmanı gibi test senaryoları üret."},
            {"role": "user", "content": build_testcase_prompt(inputs)}
        ],
        temperature=0.4,
    )
    return response.choices[0].message.content.strip()
