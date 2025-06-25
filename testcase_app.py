# generate_testcases.py
import openai
import streamlit as st

api_key = st.secrets["OPENAI_API_KEY"]
client = openai.OpenAI(api_key=api_key)


def build_testcase_prompt(data: dict) -> str:
    return f"""
Özellik Adı: {data['feature_name']}
Amaç: {data['test_purpose']}
Test Tipi: {data['test_type']}
Ön Koşullar: {data['preconditions']}
Adımlar: {data['steps']}
Beklenen Sonuçlar: {data['expected']}

Yukarıdaki bilgilerle aşağıdaki sütunları içeren bir test checklisti hazırla:
- NO
- TEST KOŞULU
- TEST AÇIKLAMASI
- TEST SENARYOSU
- BEKLENEN DURUM

Her satır ayrı bir test case olacak şekilde yaz.
"""


def generate_test_cases(inputs: dict) -> list:
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Deneyimli bir test mühendisi gibi test checklisti hazırla."},
            {"role": "user", "content": build_testcase_prompt(inputs)}
        ],
        temperature=0.4,
    )

    content = response.choices[0].message.content.strip()
    lines = content.splitlines()

    test_cases = []
    for line in lines:
        if line.lower().startswith("no") or not line.strip():
            continue
        parts = [part.strip() for part in line.split("|")]
        if len(parts) >= 5:
            test_cases.append({
                "no": parts[0],
                "condition": parts[1],
                "description": parts[2],
                "steps": parts[3],
                "expected": parts[4]
            })
    return test_cases
