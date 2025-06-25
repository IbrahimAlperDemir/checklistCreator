import streamlit as st
from generate_test_cases import generate_test_cases
from save_to_checklist import save_to_checklist
from datetime import datetime

st.title("🔍 AI Destekli Test Case Checklist Oluşturucu")

st.markdown("Lütfen aşağıdaki bilgileri girin. GPT test senaryolarını otomatik oluşturacaktır:")

with st.form("testcase_form"):
    feature_name = st.text_input("1. Özellik Adı")
    test_purpose = st.text_area("2. Özelliğin amacı nedir?")
    how_it_works = st.text_area("3. Özellik nasıl çalışır?")
    revision = st.text_input("4. Revizyon", value="A")

    submitted = st.form_submit_button("🧠 Test Checklist'i Oluştur")

if submitted:
    with st.spinner("GPT ile test senaryoları oluşturuluyor..."):
        feature_data = {
            "name": feature_name,
            "purpose": test_purpose,
            "how_it_works": how_it_works,
        }

        test_cases = generate_test_cases(feature_data)  # GPT'den gelen test case listesi

        filename = f"Test_Checklist_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
        save_to_checklist(test_cases, filename, revision=revision)

        with open(filename, "rb") as f:
            st.success("✅ Test checklist başarıyla oluşturuldu!")
            st.download_button(
                label="📥 Excel olarak indir",
                data=f,
                file_name=filename,
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
