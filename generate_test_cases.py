import openai
import streamlit as st

api_key = st.secrets["OPENAI_API_KEY"]
client = openai.OpenAI(api_key=api_key)

def build_prompt(data: dict) -> str:
    return f"""
### Özellik Adı
{data['feature_name']}

### Testin Amacı
{data['test_purpose']}

### Test Tipi
{data['test_type']}

### Ön Koşullar
{data['preconditions']}

### Test Adımları
{data['steps']}

### Beklenen Sonuç
{data['expected']}

---
Bu bilgilerle aşağıdaki formatta profesyonel test senaryoları üret:

| Test Case No | Test Adımı | Beklenen Sonuç | Ön Koşul | Test Tipi |
|--------------|------------|----------------|----------|-----------|
"""

def generate_test_cases(inputs: dict) -> str:
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Profesyonel bir QA mühendisi gibi test case tablosu üret."},
            {"role": "user", "content": build_prompt(inputs)}
        ],
        temperature=0.4,
    )
    return response.choices[0].message.content.strip()
