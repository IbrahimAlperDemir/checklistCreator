# 1️⃣ testcase_app.py
import streamlit as st
from generate_test_cases import generate_test_cases
from save_to_checklist import save_to_checklist

st.title("🧪 Test Case Checklist Oluşturucu")

st.markdown("Aşağıdaki bilgileri doldurarak test case checklist'i oluşturabilirsiniz:")

with st.form("testcase_form"):
    feature_name = st.text_input("1. Özellik Adı")
    test_purpose = st.text_area("2. Testin Amacı")
    test_type = st.selectbox("3. Test Tipi", ["Fonksiyonel", "Performans", "Güvenlik", "Kullanılabilirlik", "Uyumluluk"])
    steps = st.text_area("4. Test Adımları")
    expected = st.text_area("5. Beklenen Sonuçlar")
    revision = st.text_input("Revizyon", value="A")

    submitted = st.form_submit_button("✅ Test Checklist Oluştur")

if submitted:
    data = {
        "name": feature_name,
        "purpose": test_purpose,
        "type": test_type,
        "steps": steps,
        "expected": expected
    }
    checklist = generate_test_cases(data)
    filename = f"Test_Checklist_{feature_name.replace(' ', '_')}.xlsx"
    save_to_checklist(checklist, filename, revision=revision)

    with open(filename, "rb") as file:
        st.success("✅ Excel dosyası oluşturuldu!")
        st.download_button(
            label="📥 Excel olarak indir",
            data=file,
            file_name=filename,
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
