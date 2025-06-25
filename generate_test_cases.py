# generate_test_cases.py
import openai
import streamlit as st

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
Bu bilgilerden yola çıkarak aşağıdaki formatta test senaryoları oluştur:

NO | TEST KOŞULU | TEST AÇIKLAMASI | TEST SENARYOSU | BEKLENEN DURUM
"""

def generate_test_cases(inputs: dict) -> str:
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Profesyonel bir test uzmanı olarak test case checklist oluştur."},
            {"role": "user", "content": build_testcase_prompt(inputs)}
        ],
        temperature=0.3,
    )
    return response.choices[0].message.content.strip()
