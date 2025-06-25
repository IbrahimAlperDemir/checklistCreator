import streamlit as st
from save_to_checklist import save_to_checklist
from datetime import datetime

st.title("✅ Test Case Checklist Oluşturucu")

st.markdown("Aşağıdaki alanları doldurarak test checklist'ini oluşturabilirsiniz:")

with st.form("testcase_form"):
    feature_name = st.text_input("1. Özellik Adı")
    test_purpose = st.text_area("2. Testin Amacı")
    test_type = st.selectbox("3. Test Tipi", ["Fonksiyonel", "Performans", "Güvenlik", "Kullanılabilirlik", "Uyumluluk"])
    preconditions = st.text_area("4. Ön Koşullar")
    steps = st.text_area("5. Test Adımları")
    expected = st.text_area("6. Beklenen Sonuçlar")
    revision = st.text_input("Revizyon", value="A")

    submitted = st.form_submit_button("✅ Test Checklist Oluştur")

if submitted:
    with st.spinner("Test checklist oluşturuluyor..."):
        filename = f"Test_Checklist_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"

        test_data = [{
            "condition": preconditions,
            "description": test_purpose,
            "steps": steps,
            "expected": expected
        }]

        save_to_checklist(test_data, filename, revision=revision)

        with open(filename, "rb") as f:
            st.success("✅ Test checklist başarıyla oluşturuldu!")
            st.download_button(
                label="📥 Excel Dosyasını İndir",
                data=f,
                file_name=filename,
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
