import streamlit as st
from generate_test_cases import generate_test_cases
from save_to_checklist import save_to_checklist
import os

st.set_page_config(page_title="Test Checklist Oluşturucu", layout="wide")
st.title("✅ Test Checklist Oluşturucu")

with st.form("testcase_form"):
    feature_name = st.text_input("1. Özellik Adı")
    test_purpose = st.text_area("2. Testin Amacı")
    test_type = st.selectbox("3. Test Tipi", ["Fonksiyonel", "Performans", "Güvenlik", "Kullanılabilirlik", "Uyumluluk"])
    steps = st.text_area("4. Test Adımları")
    expected = st.text_area("5. Beklenen Sonuçlar")
    revision = st.text_input("Revizyon", value="A")
    submitted = st.form_submit_button("✅ Test Checklist Oluştur")

if submitted:
    with st.spinner("Checklist oluşturuluyor..."):
        data = {
            "feature_name": feature_name,
            "test_purpose": test_purpose,
            "test_type": test_type,
            "steps": steps,
            "expected": expected,
        }
        checklist = generate_test_cases(data)
        filename = "Test_Checklist.xlsx"
        save_to_checklist(checklist, filename, revision=revision)

        with open(filename, "rb") as file:
            st.success("📄 Excel dosyası hazır!")
            st.download_button(
                label="📥 Excel olarak indir",
                data=file,
                file_name=filename,
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
