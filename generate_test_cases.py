from openai import OpenAI
import streamlit as st

api_key = st.secrets["OPENAI_API_KEY"]
client = OpenAI(api_key=api_key)

def build_test_prompt(inputs: dict) -> str:
    return f"""
### Özellik Adı
{inputs['feature_name']}

### Testin Amacı
{inputs['test_purpose']}

### Test Tipi
{inputs['test_type']}

### Ön Koşullar
{inputs['preconditions']}

### Test Adımları
{inputs['steps']}

### Beklenen Sonuçlar
{inputs['expected']}

---
Yukarıdaki bilgilerle aşağıdaki alanlara uygun olarak test case checklist oluştur:
- NO
- TEST KOŞULU
- TEST AÇIKLAMASI
- TEST SENARYOSU
- BEKLENEN DURUM

Sadece tablo formatında ve her satırda tek test olacak şekilde oluştur.
"""

def generate_test_cases(inputs: dict) -> str:
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Tecrübeli bir QA uzmanı olarak profesyonel test case checklist'i oluştur."},
            {"role": "user", "content": build_test_prompt(inputs)}
        ],
        temperature=0.3
    )
    return response.choices[0].message.content.strip()
